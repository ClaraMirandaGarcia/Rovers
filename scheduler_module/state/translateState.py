import scheduler_module.state.idleState as ist
from scheduler_module.errors_simulation import SimError
from scheduler_module.state.state import State
from scheduler_module.grid.cell import Cell
import scheduler_module.state.exploringState as es
import numpy as np
import pykka
import time

@pykka.traversable
class TranslateState(State):
    def add_time(self, cell_origin, cell_to):
        # t = distancia(localización, celda a la que me voy a mover) / velocidad
        distance = cell_origin.distance_to(cell_to) * np.sqrt(cell_origin.size)
        time_to_add = distance / self.context.translate_speed
        check_time = self.context.time_idle + self.context.time_translate + self.context.time_charging \
                     + self.context.time_exploring + time_to_add

        if self.context.max_time is not None and check_time >= self.context.max_time:
            self.context.is_max_time = True

        else:
            self.context.total_time = self.context.total_time + time_to_add
            self.context.time_translate = self.context.time_translate + time_to_add

    def manage_charging(self, cell):
        if self.context.location.is_charging_point():
            self.to_charge(cell)
        else:
            path = self.context.best_known_path
            self.retreat(cell, path)

    def move(self, cell: Cell) -> None:
        if self.check_enough_battery():
            if self.context.recharge:
                self.manage_charging(cell)

            else:
                # primera celda sin explorar del trabajo
                goal_cell = self.context.job.get_first_cell()

                if self.context.location == cell:
                    self.context.set_state(es.ExploringState("ExploringState"))
                    self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                    self.context.move(cell)
                # Checking if there are accessible unexplored cells
                elif self.context.check_cells():
                    # Find accessible unexplored cell -> move there
                    unexplored_cells = self.context.get_unexplored()

                    if unexplored_cells[0].get_coordinate() == self.context.location.get_coordinate():
                        # Si la unica celda a explorar que queda es en la que estamos nos movemos
                        self.context.write_file(
                            "\t\t" + "Current Cell:" + str(self.context.location.get_coordinate()) + "\n")
                        self.context.write_file(
                            "\t\t" + "Available Cell: " + str(unexplored_cells[0].get_coordinate()) + "\n")

                        self.context.set_state(es.ExploringState("ExploringState"))
                        self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                        self.context.move(unexplored_cells[0])

                    elif unexplored_cells[0].get_coordinate() == cell.get_coordinate():
                        self.context.set_state(es.ExploringState("ExploringState"))
                        self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                        self.context.move(goal_cell)

                    elif cell.is_accessible(self.context.location):
                        # Si la celda es accesible desde donde estamos
                        self.context.write_file(
                            "\t\t" + "Current Cell:" + str(self.context.location.get_coordinate()) + "\n")
                        self.context.write_file(
                            "\t\t" + "Available Cell: " + str(unexplored_cells[0].get_coordinate()) + "\n")

                        self.context.set_state(es.ExploringState("ExploringState"))
                        self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                        self.context.move(unexplored_cells[0])
                        self.add_time(self.context.location, unexplored_cells[0])

                    else:
                        # comprobar si es accesible la celda cell desde mi posicion -> si no hay que moverse
                        path = self.context.best_known_path
                        cell_to, continue_sim = self.get_cell_to_2(path, cell, cell)
                        self.context.aux_translate_counter = 0
                        if continue_sim:
                            self.manage_move(cell, cell_to)
                        else:
                            pass

                elif goal_cell is not None:
                    path = self.context.best_known_path
                    cell_to, continue_sim = self.get_cell_to_2(path, cell, cell)
                    self.context.aux_translate_counter = 0
                    if continue_sim:
                        self.manage_move(cell, cell_to)
                    else:
                        pass
        else:
            message = (
                    "The exploring operation could not be performed by the rover " + self.context.name_rover + " due to its "
                                                                                                       " battery "
                                                                                                       " capacity.")
            error = SimError("Battery Capacity", message)
            self.context.errors.append(error)
            self.context.job.errors.append(error)
            self.context.write_file(error.get_message())


    def check_enough_battery(self):
        capacity = self.context.battery_capacity
        move_cost_trans = self.context.translate_bat

        cost_move_path = len(self.context.best_known_path) * move_cost_trans
        total_cost = cost_move_path * 2
        move_cost_exp = self.context.exp_bat

        if total_cost + move_cost_exp >= capacity:
            return False
        return True

    def battery_available(self, limit=10, move_cost=10) -> bool:
        # if battery needed to return to charging point < battery left esto es desde estado exploración
        battery_to_cp = len(self.best_known_path) * self.translate_bat
        if (battery_to_cp + limit + move_cost) >= self.get_battery():
            return False
        return True

    def manage_move(self, cell, cell_to):
        # comprobar si existe un camino conocido entre cell y cell_to
        self.add_time(self.context.location, cell_to)
        self.context.write_file("\t\t" +
                                    "Moving to cell: " + str(cell.get_coordinate()) +
                                    " from cell: " + str(self.context.location.get_coordinate()) + "\n")
        self.context.location = cell_to
        self.context.write_file("\t\t" + " Location: " + str(self.context.location.get_coordinate()))
        self.context.move(cell)

    def get_cell_to_2_inf(self, path, cell, goal_cell):
        '''
        :param path:
        :param cell:
        :param goal_cell:
        :return:
        '''
        available = True
        aux = self.context.location.get_closest_accessible_cell(self.context.location, path, goal_cell)
        exp_cells = self.context.grid.get_explored_cells()
        cells = list(filter(lambda c: c.is_accessible(self.context.location), exp_cells))
        aux2 = self.context.location.get_closest_accessible_cell(self.context.location, cells, goal_cell)

        # The cell can not be itself
        if aux2 == self.context.location:
            self.context.write_file("\t\tReturn path is not accessible")
            #time.sleep(1)

            # the path is not explored, wait and try again
            self.context.aux_translate_counter = self.context.aux_translate_counter + 1
            if (self.context.aux_translate_counter > 35):
                self.context.write_file("\t\tThe path is not explored, there are unexplored cells in the simulation")
                self.context.write_file("\t\tAborting simulation")
                message = (
                        "The exploring operation could not be performed by the rover " + self.context.name_rover + " due to "
                                                                                                           "the lack "
                                                                                                           "of a known, "
                                                                                                           "accesible "
                                                                                                           "path.")
                error = SimError("Battery Capacity", message)
                self.context.errors.append(error)
                self.context.job.errors.append(error)
                self.context.write_file(error.get_message())

                available = False
                return aux2, available

            if self.context.aux_translate_counter <= 35:
                self.get_cell_to_2(path, cell, goal_cell)
        if self.context.aux_translate_counter < 35:

            distance_1 = aux.distance_to(goal_cell)
            distance_2 = aux2.distance_to(goal_cell)

            if distance_1 <= distance_2:
                return aux, True
            else:
                return aux2, True

    def get_cell_to_2(self, path, cell, goal_cell):
        '''
        :param path:
        :param cell:
        :param goal_cell:
        :return:
        '''
        available = True
        aux = self.context.location.get_closest_accessible_cell(self.context.location, path, goal_cell)
        exp_cells = self.context.grid.get_explored_cells()
        cells = list(filter(lambda c: c.is_accessible(self.context.location), exp_cells))
        aux2 = self.context.location.get_closest_accessible_cell(self.context.location, cells, goal_cell)

        # The cell can not be itself
        if aux2 != self.context.location and not self.context.aux_translate_counter > 0:
            distance_1 = aux.distance_to(goal_cell)
            distance_2 = aux2.distance_to(goal_cell)

            if distance_1 <= distance_2:
                return aux, True
            else:
                return aux2, True
        else:
            while aux2 == self.context.location:
                self.context.write_file("\t\tReturn path is not accessible")
                # time.sleep(1)
                # the path is not explored, wait and try again
                self.context.aux_translate_counter = self.context.aux_translate_counter + 1
                if aux2 != self.context.location and not self.context.aux_translate_counter > 0:
                    distance_1 = aux.distance_to(goal_cell)
                    distance_2 = aux2.distance_to(goal_cell)

                    if distance_1 <= distance_2:
                        return aux, True
                    else:
                        return aux2, True

                if self.context.aux_translate_counter > 35:
                    self.context.write_file(
                        "\t\tThe path is not explored, there are unexplored cells in the simulation")
                    self.context.write_file("\t\tAborting simulation")
                    message = (
                            "The exploring operation could not be performed by the rover " + self.context.name_rover + " due to "
                                                                                                                       "the lack "
                                                                                                                       "of a known, "
                                                                                                                       "accesible "
                                                                                                                       "path.")
                    error = SimError("Battery Capacity", message)
                    self.context.errors.append(error)
                    self.context.job.errors.append(error)
                    self.context.grid.error_counter = self.grid.error_counter + 1
                    self.context.write_file(error.get_message())

                    available = False
                    return aux2, available




    def to_charge(self, cell):
        self.context.write_file("\t\t"+"Location: "+ str(self.context.location.get_coordinate())+"next to charging ")
        self.context.add_movement_log(str(self.context.location.get_coordinate()))
        self.context.write_file("\t\t"+"next to charging point")
        # Set state -> Idle

        self.context.set_state(ist.IdleState("IdleState"))
        self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
        # Charging + block
        rover = self.context
        self.context.grid.charging_point.set_rover(rover).get()
        # checking the battery -> change state
        self.context.set_state(TranslateState('TranslateState'))
        self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
        self.context.move(cell)

    def retreat(self, cell, best_known_path):
        self.context.write_file("\t\t" + "Current location: " + str(self.context.location.get_coordinate()) + " moving to Charging Point" + "\n")
        cells = best_known_path
        current_index = cells.index(self.context.location)
        # Calculate the distance here
        cell_origin = cells[current_index]
        cell_to = None
        if len(cells) == 1:
            cell_to = self.context.job.charging_point
        else:
            try:
                cell_to = cells[current_index + 1]
            except IndexError:
                cell_to = self.context.job.charging_point

        self.add_time(cell_origin, cell_to)
        self.context.location = cell_to
        self.context.add_movement_log(str(self.context.location.get_coordinate()))
        self.battery_discharge()
        self.context.move(cell)

    def battery_discharge(self):
        new_battery = self.context.battery - self.context.translate_bat
        self.context.set_battery(new_battery)
        pass
