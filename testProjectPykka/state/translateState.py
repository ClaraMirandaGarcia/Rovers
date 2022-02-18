from state.state import State
from grid.cell import Cell, CellState
from state.chargingState import ChargingState
import state.exploringState as s
import numpy as np


class TranslateState(State):
    def add_time(self, cell_origin, cell_to):
        # t = distancia(localización, celda a la que me voy a mover) / velocidad
        distance = cell_origin.distance_to(cell_to) * np.sqrt(cell_origin.size)
        time = distance / self.context.translate_speed
        check_time = self.context.time_idle + self.context.time_translate + self.context.time_charging + self.context.time_exploring + time

        if self.context.max_time is not None and check_time >= self.context.max_time:
            self.context.is_max_time = True
        else:
            self.context.total_time += time
            self.context.time_translate += time

    def manage_charging(self, cell):
        if self.context.location.is_charging_point():
            self.to_charge(self, cell)
        else:
            path = self.context.best_known_path
            self.retreat(self, cell, path)

    def move(self, cell: Cell) -> None:


        if self.context.recharge:
            self.manage_charging(self, cell)

        else:
            # primera celda sin explorar del trabajo
            goal_cell = self.context.job.get_first_cell()

            if self.context.location == cell:
                self.context.set_state(s.ExploringState)
                self.context.move(cell)

            # Checking if there are accessible unexplored cells
            elif self.context.check_cells():
                # Find accessible unexplored cell -> move there
                unexplored_cells = self.context.get_unexplored()

                if unexplored_cells[0].get_coordinate() == self.context.location.get_coordinate():
                    # Si la unica celda a explorar que queda es en la que estamos nos movemos
                    self.context.write_file("CURRENT CELL" + str(self.context.location.get_coordinate()) + "\n")
                    self.context.write_file("AVAILABLE CELL" + str(unexplored_cells[0].get_coordinate()) + "\n")
                    print("CURRENT CELL", self.context.location.get_coordinate())
                    print("AVAILABLE CELL", unexplored_cells[0].get_coordinate())
                    self.context.set_state(s.ExploringState)
                    self.context.move(unexplored_cells[0])

                elif unexplored_cells[0].get_coordinate() == cell.get_coordinate():
                    # Si la celda a explorar es la misma que la única available que queda -> exploramos la GOAL CELL
                    self.context.set_state(s.ExploringState)
                    self.context.move(goal_cell)

                elif cell.is_accessible(self.context.location):
                    # Si la celda es accesible desde donde estamos
                    self.context.write_file("CURRENT CELL" + str(self.context.location.get_coordinate()) + "\n")
                    self.context.write_file("AVAILABLE CELL" + str(unexplored_cells[0].get_coordinate()) + "\n")
                    print("CURRENT CELL", self.context.location.get_coordinate())
                    print("AVAILABLE CELL", unexplored_cells[0].get_coordinate())
                    self.context.set_state(s.ExploringState)
                    self.context.move(unexplored_cells[0])
                    self.add_time(self, self.context.location, unexplored_cells[0])

                else:
                    # comprobar si es accesible la celda cell desde mi posicion -> si no hay que moverse
                    path = self.context.best_known_path
                    cell_to = self.get_cell_to_2(self, path, cell, cell)
                    self.manage_move(self, cell, cell_to)

            elif goal_cell is not None:
                path = self.context.best_known_path
                cell_to = self.get_cell_to_2(self, path, cell, cell)
                self.manage_move(self, cell, cell_to)

    def manage_move(self, cell, cell_to):
        self.add_time(self, self.context.location, cell_to)
        self.context.write_file("Moving to: "+ str(cell.get_coordinate()) + " from: " + str(self.context.location.get_coordinate()) + "\n")
        print("Moving to: ", cell.get_coordinate(), " from: ", self.context.location.get_coordinate())
        self.context.location = cell_to
        self.context.write_file("LOCATION AFTER MOVING: " + str(self.context.location.get_coordinate()) + "\n")
        print("LOCATION AFTER MOVING: ", self.context.location.get_coordinate())
        self.context.move(cell)

    def get_cell_to(self, current_index, goal_index, path, cell, goal_cell):

        # No vale este if else -> tengo que considerar len path -1
        path_length = len(path) - 1

        # hay que ver cual es la closest accessible explored cell para llegar a la celda
        if goal_index is None and current_index < path_length:
            cell_to = path[current_index + 1]
        elif goal_index is None and current_index > path_length:
            cell_to = path[current_index - 1]
        elif goal_index is None and current_index == path_length:
            # comprobar si estás al lado?
            if cell.is_accessible(self.context.location):
                cell_to = cell
            elif goal_cell.is_accessible(self.context.location):
                cell_to = goal_cell
        elif goal_index < current_index and current_index > 0:
            cell_to = path[current_index - 1]
        else:
            cell_to = path[current_index + 1]
        return cell_to

    def get_cell_to_2(self, path, cell, goal_cell):
        '''
        :param path:
        :param cell:
        :param goal_cell:
        :return:
        '''
        aux = self.context.location.get_closest_accessible_cell(self.context.location, path, goal_cell)

        exp_cells = self.context.grid.get_explored_cells()
        cells = list(filter(lambda c: c.is_accessible(self.context.location), exp_cells))
        aux2 = self.context.location.get_closest_accessible_cell(self.context.location, cells, goal_cell)

        distance_1 = aux.distance_to(goal_cell)
        distance_2 = aux2.distance_to(goal_cell)

        if distance_1 <= distance_2:
            return aux
        else:
            return aux2

    def to_charge(self, cell):
        self.context.write_file("NEXT TO CHARGING POINT" + "\n")
        self.context.write_file(str(self.context.location.get_coordinate()) + "\n")
        print("NEXT TO CHARGING POINT")
        print(self.context.location.get_coordinate())
        # Set state -> Idle
        self.context.set_state(ChargingState)
        self.context.move(cell)

    def retreat(self, cell, best_known_path):
        self.context.write_file("RETREATING" + "\n")
        print("RETREATING")

        cells = best_known_path
        current_index = cells.index(self.context.location)
        # Calculate the distance here
        cell_origin = cells[current_index]
        cell_to = cells[current_index + 1]
        self.add_time(self, cell_origin, cell_to)

        self.context.location = cell_to
        self.battery_discharge(self)
        self.context.move(cell)

    def battery_discharge(self):
        new_battery = self.context.battery - self.context.translate_bat
        self.context.set_battery(new_battery)
        pass
