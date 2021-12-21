from state.state import State
from grid.cell import Cell, CellState
from state.chargingState import ChargingState
import state.exploringState as s


class TranslateState(State):
    def add_time(self, cell_origin, cell_to):
        # t = distancia(localización, celda a la que me voy a mover) / velocidad
        distance = cell_origin.distance_to(cell_to) * cell_origin.size
        time = distance / self.context.translate_speed
        self.context.time_translate += time

    def move(self, cell: Cell) -> None:

        if self.context.recharge:
            if self.context.location.is_charging_point():
                self.to_charge(self, cell)
            else:
                path = self.context.best_known_path
                self.retreat(self, cell, path)
        else:
            # necesita volver desde el punto de carga hasta la celda
            print("GOING BACK TO EXPLORING")
            goal_cell = self.context.job.get_first_cell()

            # if the cell is reachable + unexplored from the current location -> explore mode + move
            if self.context.location == goal_cell or self.context.check_cells():
                # it has reached the point to explore
                self.context.set_state(s.ExploringState)
                self.context.move(cell)
            else:
                # avanzar desde la posición actual por el best_known_path hasta goal_cell
                path = self.context.best_known_path
                # find current position in best_known_path, advance one more
                current_index = path.index(self.context.location)
                goal_index = None
                if goal_cell in path:
                    goal_index = path.index(goal_cell)

                if goal_index == 0:
                    # check distance
                    cell_to = path[current_index - 1]
                    #if cell_to is not None:
                    self.add_time(self, self.context.location, cell_to)
                    self.context.location = cell_to
                else:
                    cell_to = path[current_index + 1]
                    #if cell_to is not None:
                    self.add_time(self, self.context.location, cell_to)
                    self.context.location = cell_to

                print("Moving to: ", cell.get_coordinate(), " from: ", self.context.location.get_coordinate())
                self.context.move(cell)
        cell.set_state(CellState.EXPLORED)

    def to_charge(self, cell):

        print("NEXT TO CHARGING POINT")
        print(self.context.location.get_coordinate())
        # Set state -> Idle
        self.context.set_state(ChargingState)
        self.context.move(cell)

    def retreat(self, cell,  best_known_path):
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
