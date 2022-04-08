from grid.cell import Cell, CellState
from grid.job import Job
from fileManagement import FileManager
import pykka
from time import localtime, asctime
import threading
import numpy as np
from enum import Enum


class State1(Enum):
    EXPLORING_STATE = 1
    TRANSLATE_STATE = 2
    IDLE_STATE = 3
    CHARGING_STATE = 4


class Rover(pykka.ThreadingActor):

    def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time, grid,
                 max_time, name_rover):

        self.file_manager = None
        self.name_file = None
        self.battery = battery
        self.state = state
        self.set_state(state)
        self.translate_speed = translate_speed
        self.exp_speed = exp_speed
        self.translate_bat = translate_bat
        self.exp_bat = exp_bat
        self.charging_time = charging_time
        self.recharge = False
        self.best_known_path = []
        self.job = None
        self.location = None
        self.occupied = False
        self.grid = grid
        self.time_exploring = 0
        self.time_translate = 0
        self.time_idle = 0
        self.time_charging = 0
        self.total_time = 0
        self.max_time = max_time
        self.is_max_time = False
        self.area_explored = 0
        path_to_file = "log_files/" + grid.file_manager.name_file + name_rover
        self.name_rover = name_rover
        self.file_manager = FileManager(grid.file_manager.name_file, path_to_file)
        self.f = None
        super().__init__()

    def write_file_opening(self):
        self.f = open(self.name_file, "a")
        self.f.write("Log output for " + self.name_file + "\n")
        self.f.write(asctime(localtime()) + "\n")
        self.f.close()

    def write_file(self, to_write):
        thread_name = threading.current_thread().name
        self.f = open(self.name_file, "a")
        # self.f.write(f"{thread_name}: {to_write}"+"\n")
        self.f.write(to_write + "\n")
        self.f.close()

    def set_name_file(self, name_file):
        self.name_file = name_file

    def set_state(self, new_state):
        if self.file_manager is not None:
            self.write_file(f"Agent: Transitioning to {new_state}")
        # self.file_manager.write("Agent: Transitioning to {new_state.__name__}")
        self.state = new_state
        # self.state.set_context(self.state, context=self)

    def move(self, cell: Cell):
        if self.location is None:
            self.location = cell

        if self.state == State1.EXPLORING_STATE:
            self.move_exploring(cell)
        elif self.state == State1.CHARGING_STATE:
            self.move_charging(cell)
        elif self.state == State1.TRANSLATE_STATE:
            self.move_translate(cell)
        elif self.state == State1.IDLE_STATE:
            self.move_idle(cell)

        # self.state.move(self.state, cell)

    def check_cells(self):
        '''
        :return: True if there are accessible unexplored cells from the rover location
        '''
        accessible_cells = self.job.get_cells_accessible_from(self.location)
        unexplored_accessible_cells = list(filter(lambda a_c: not a_c.is_cell_explored(), accessible_cells))
        if len(unexplored_accessible_cells) > 0:
            return True
        else:
            return False

    def get_unexplored(self):
        '''
        :return: List of accessible unexplored cells from the rover location
        '''
        accessible_cells = self.job.get_cells_accessible_from(self.location)
        unexplored_accessible_cells = list(filter(lambda a_c: not a_c.is_cell_explored(), accessible_cells))
        return unexplored_accessible_cells

    def get_unexplored_grid(self):
        '''
        :return: List of accessible unexplored cells from the rover location
        '''
        accessible_cells = self.grid.get_cells_accessible_from(self.location)
        unexplored_accessible_cells = list(filter(lambda a_c: not a_c.is_cell_explored(), accessible_cells))
        return unexplored_accessible_cells

    def move_to(self, cell: Cell):
        self.state.explore(self, cell)

    def battery_available(self, limit=10, move_cost=10) -> bool:
        # if battery needed to return to charging point < battery left
        battery_to_cp = len(self.best_known_path) * self.translate_bat
        if (battery_to_cp + limit + move_cost) >= self.get_battery():
            return False
        return True

    # , battery, state, max_speed, min_speed, max_bat, min_bat, charging_time
    def set_properties(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time):
        self.battery = battery
        self.state = state
        self.set_state(state)
        self.translate_speed = translate_speed
        self.exp_speed = exp_speed
        self.exp_bat = exp_bat
        self.translate_bat = translate_bat
        self.charging_time = charging_time

    # Battery
    def set_battery(self, new_battery):
        self.battery = new_battery
        pass

    def get_battery(self) -> int:
        return self.battery

    # Max speed
    def set_translate_speed(self, translate_speed):
        self.translate_speed = translate_speed

    def get_translate_speed(self):
        return self.translate_speed

    # min speed
    def set_exp_speed(self, exp_speed):
        self.exp_speed = exp_speed

    def get_exp_speed(self):
        return self.exp_speed

    # max bat
    def set_exp_bat(self, exp_bat):
        self.exp_bat = exp_bat

    def get_exp_bat(self):
        return self.exp_bat

    # min bat
    def set_translate_bat(self, translate_bat):
        self.translate_bat = translate_bat

    def get_translate_bat(self):
        return self.translate_bat

    def set_is_max_time(self, is_max_time):
        self.is_max_time = is_max_time

    def get_is_max_time(self):
        return self.is_max_time

    # Best known path
    def add_best_cell(self, best_cell: Cell):
        # check if there exists a path from best_cell[0] hasta -> best_cell mejor que el que hay hasta entonces
        # search for min distance path
        self.best_known_path = self.find_better_path(best_cell)
        if best_cell not in self.best_known_path:
            self.best_known_path.insert(0, best_cell)

        self.write_file("BEST KNOWN PATH")
        for cell in self.best_known_path:
            #   self.file_manager.write(cell.get_coordinate())
            self.write_file(str(cell.get_coordinate()))
        # self.file_manager.write("\n")

    def find_better_path(self, current_cell: Cell):
        better_path = [current_cell]

        for i in range(len(self.best_known_path), 0, -1):
            if not current_cell.is_charging_point():
                # check accessible cells
                accessible_cells = self.job.get_cells_accessible_from(current_cell)
                # tienen que ser las accessible cells que estén dentro del best_known path
                cells0 = list(filter(lambda cell: (cell in self.best_known_path), accessible_cells))
                cells1 = list(filter(lambda cell: (cell not in better_path), cells0))

                if len(cells1) == 0:
                    previous_path = self.grid.search_path(self.job.charging_point, current_cell)
                    better_path = previous_path
                else:
                    # check min distance of accessible cells
                    cell_min = self.job.get_closest_cell_simple(cells1)
                    better_path.append(cell_min)
                    current_cell = cell_min
            elif current_cell.is_charging_point() and current_cell not in better_path:
                better_path.append(current_cell)

        if (len(better_path)) < (len(self.best_known_path)):
            return better_path
        return better_path

    def get_best_path(self) -> []:
        return self.best_known_path

    # The rover has a job assigned
    def set_occupied(self, occupied):
        self.occupied = occupied

    def is_occupied(self) -> bool:
        return self.occupied

    # Job scheduled
    def set_job(self, job):
        self.job = job
        self.occupied = True

    def get_job(self) -> Job:
        return self.job

    def simple_strategy(self):
        """
            Performs a simple strategy for the rover with the jobs given.
        """
        cell_count = 0

        # Check for an accessible cell
        # If accessible then explore
        # If not then eliminate the cell for the cells of the job

        # if charging point in job_cells -> start by cp

        for cell in self.job.job_cells:

            self.write_file("Exploring cell " + str(cell_count))
            # self.file_manager.write("Exploring cell " + str(cell_count))
            cell_count += 1
            if not self.is_max_time and not self.max_time == 0:
                self.move(cell)
                self.job.change_state()
                self.write_file("Cell state: " + cell.get_cell_state().name)
                self.write_file("Job state: " + self.job.get_job_state().name)
            else:
                self.write_file("MAX TIME REACHED")
                break

        self.write_file("FINISHING")
        self.write_file(str(self.job.get_job_state()))

        self.write_file("\n")
        self.write_file("\n")
        self.write_file("RESUME" + "\n")
        self.write_file("Time exploring (min):" + "{:.2f}".format(self.time_exploring))
        self.write_file("Time translate (min):" + "{:.2f}".format(self.time_translate))
        self.write_file("Time charging (min):" + "{:.2f}".format(self.time_charging))
        self.write_file("Time idle (min):" + "{:.2f}".format(self.time_idle))
        self.write_file("---------------------------------------")
        self.write_file("Total time calculated (min):" + "{:.2f}".format(
            self.time_idle + self.time_translate + self.time_charging + self.time_exploring))
        self.write_file("Total explored (m^2):" + "{:.2f}".format(self.area_explored))

    def simple_strategy_area(self):
        """
            Performs a simple strategy for the rover with the jobs given.
        """
        cell_count = 0

        # Check for an accessible cell
        # If accessible then explore
        # If not then eliminate the cell for the cells of the job

        for cell in self.job.job_cells:
            self.write_file("Exploring cell " + str(cell_count))
            # self.file_manager.write("Exploring cell " + str(cell_count))
            cell_count += 1
            self.move(cell)
            self.job.change_state()
            # rises -> problem
            self.write_file("Cell state: " + cell.get_cell_state().name)
            self.write_file("Job state: " + self.job.get_job_state().name)

        self.write_file("FINISHING")
        self.write_file(self.job.get_job_state())
        self.write_file("RESUME")
        self.write_file("Time exploring:" + str(self.time_exploring))
        self.write_file("Time translate:" + str(self.time_translate))
        self.write_file("Time charging:" + str(self.time_charging))
        self.write_file("Time idle:" + str(self.time_idle))
        self.write_file("---------------------------------------")
        self.write_file("Total time calculated: " +
                        str(self.time_idle + self.time_translate + self.time_charging + self.time_exploring))
        self.write_file("Total explored: " + str(self.area_explored))

    def on_receive(self, message):
        if message == "simple_strategy":
            self.simple_strategy()
        elif message == "simple_strategy_max_time":
            self.simple_strategy_time()
        elif message == "simple_strategy_max_area":
            self.simple_strategy_area()
        else:
            print('MESSAGE NOT MATCHED')

    # EXPLORING STATE
    def add_time_exploring(self, cell_from, cell_to):
        distance = cell_from.distance_to(cell_to) * np.sqrt(cell_from.size)
        time = distance / self.exp_speed
        check_time = self.time_idle + self.time_translate + self.time_charging + self.time_exploring + time

        if self.max_time is not None and check_time >= self.max_time:
            self.is_max_time = True
        else:
            self.total_time += time
            self.time_exploring += time

    def add_explored_exploring(self, cell_from):
        self.area_explored += cell_from.real_size

    def move_exploring(self, cell: Cell) -> None:
        unexplored_accessible_cells = self.check_cells()
        old_location = self.location
        cells = self.get_unexplored()

        if unexplored_accessible_cells and self.location != cell:
            c0 = cells[0]
            if cells[0].is_accessible(self.location) and cell.get_coordinate() == c0.get_coordinate():
                self.location = cells[0]
                self.add_time_exploring(self.location, c0)
                self.write_file("\n" + "FINISHED" + "\n")
            elif cell.is_accessible(self.location):
                self.add_time_exploring(self.location, cell)
                self.location = cell
            else:
                # Is not accessible -> you have to move
                self.set_state(State1.TRANSLATE_STATE)
                self.move(cell)
                # Es necesario?
                if cell.is_accessible(self.location):
                    self.add_time_exploring(self, self.location, cell)
                    self.location = cell
        elif not unexplored_accessible_cells and self.location.is_explored() and not self.job.job_fulfilled:
            # No hay celdas inexploradas y ya se ha explorado la localización
            # Mirar si el trabajo ya está finalizado o no
            self.write_file("There are no accessible unexplored cells")
            self.set_state(State1.TRANSLATE_STATE)
            self.write_file("Location " + str(self.location.get_coordinate()))
            self.move(cell)
            self.write_file("Location after moving" + str(self.location.get_coordinate()))
            self.location = cell
        else:
            self.location = cell
        rover = self
        self.write_file("LOCATION: " + str(rover.location.get_coordinate()))
        enough_battery = rover.battery_available()
        self.write_file("BATTERY AVAILABLE: " + str(rover.battery))
        self.time_exploring += 1

        self.add_time_exploring(self.location, old_location)
        self.manage_battery_exploring(cell, enough_battery)

    def manage_battery_exploring(self, cell, enough_battery):
        if enough_battery:
            self.location.set_state(CellState.EXPLORED)
            self.battery_discharge_exploring()
            self.add_explored_exploring(self.location)
            self.add_best_cell(cell)
        else:
            self.recharge = True
            self.set_state(State1.TRANSLATE_STATE)
            self.add_best_cell(cell)
            self.move(cell)

    def battery_discharge_exploring(self):
        new_battery = self.battery - self.exp_bat
        self.set_battery(new_battery)
        pass

    # TRANSLATE STATE
    def add_time_translate(self, cell_origin, cell_to):
        # t = distancia(localización, celda a la que me voy a mover) / velocidad
        distance = cell_origin.distance_to(cell_to) * np.sqrt(cell_origin.size)
        time = distance / self.translate_speed
        check_time = self.time_idle + self.time_translate + self.time_charging + self.time_exploring + time

        if self.max_time is not None and check_time >= self.max_time:
            self.is_max_time = True
        else:
            self.total_time += time
            self.time_translate += time

    def manage_charging_translate(self, cell):
        if self.location.is_charging_point():
            self.to_charge_translate(cell)
        else:
            path = self.best_known_path
            self.retreat_translate(cell, path)

    def move_translate(self, cell: Cell) -> None:
        if self.recharge:
            self.manage_charging_translate(cell)

        else:
            # primera celda sin explorar del trabajo
            goal_cell = self.job.get_first_cell()

            if self.location == cell:
                self.set_state(State1.EXPLORING_STATE)
                self.move(cell)

            # Checking if there are accessible unexplored cells
            elif self.check_cells():
                # Find accessible unexplored cell -> move there
                unexplored_cells = self.get_unexplored()

                if unexplored_cells[0].get_coordinate() == self.location.get_coordinate():
                    # Si la unica celda a explorar que queda es en la que estamos nos movemos
                    self.write_file("CURRENT CELL" + str(self.location.get_coordinate()))
                    self.write_file("AVAILABLE CELL" + str(unexplored_cells[0].get_coordinate()))
                    self.set_state(State1.EXPLORING_STATE)
                    self.move(unexplored_cells[0])

                elif unexplored_cells[0].get_coordinate() == cell.get_coordinate():
                    # Si la celda a explorar es la misma que la única available que queda -> exploramos la GOAL CELL
                    self.set_state(State1.EXPLORING_STATE)
                    self.move(goal_cell)

                elif cell.is_accessible(self.location):
                    # Si la celda es accesible desde donde estamos
                    self.write_file("CURRENT CELL" + str(self.location.get_coordinate()))
                    self.write_file("AVAILABLE CELL" + str(unexplored_cells[0].get_coordinate()))
                    self.set_state(State1.EXPLORING_STATE)
                    self.move(unexplored_cells[0])
                    self.add_time_translate(self.location, unexplored_cells[0])

                else:
                    # comprobar si es accesible la celda cell desde mi posicion -> si no hay que moverse
                    path = self.best_known_path
                    cell_to = self.get_cell_to_translate_2_translate(path, cell, cell)
                    self.manage_move_translate(cell, cell_to)

            elif goal_cell is not None:
                path = self.best_known_path
                cell_to = self.get_cell_to_translate_2_translate(path, cell, cell)
                self.manage_move_translate(cell, cell_to)

    def manage_move_translate(self, cell, cell_to):
        self.add_time_translate(self.location, cell_to)
        self.write_file(
            "Moving to: " + str(cell.get_coordinate()) + " from: " + str(self.location.get_coordinate()))
        self.location = cell_to
        self.write_file("LOCATION AFTER MOVING: " + str(self.location.get_coordinate()))
        self.move(cell)

    def get_cell_to_translate(self, current_index, goal_index, path, cell, goal_cell):

        # No vale este if else -> tengo que considerar len path -1
        path_length = len(path) - 1

        # hay que ver cual es la closest accessible explored cell para llegar a la celda
        if goal_index is None and current_index < path_length:
            cell_to = path[current_index + 1]
        elif goal_index is None and current_index > path_length:
            cell_to = path[current_index - 1]
        elif goal_index is None and current_index == path_length:
            # comprobar si estás al lado?
            if cell.is_accessible(self.location):
                cell_to = cell
            elif goal_cell.is_accessible(self.location):
                cell_to = goal_cell
        elif goal_index < current_index and current_index > 0:
            cell_to = path[current_index - 1]
        else:
            cell_to = path[current_index + 1]
        return cell_to

    def get_cell_to_translate_2_translate(self, path, cell, goal_cell):
        '''
        :param path:
        :param cell:
        :param goal_cell:
        :return:
        '''
        aux = self.location.get_closest_accessible_cell(self.location, path, goal_cell)

        exp_cells = self.grid.get_explored_cells()
        cells = list(filter(lambda c: c.is_accessible(self.location), exp_cells))
        aux2 = self.location.get_closest_accessible_cell(self.location, cells, goal_cell)

        distance_1 = aux.distance_to(goal_cell)
        distance_2 = aux2.distance_to(goal_cell)

        if distance_1 <= distance_2:
            return aux
        else:
            return aux2

    def to_charge_translate(self, cell):
        self.write_file("NEXT TO CHARGING POINT")
        self.write_file(str(self.location.get_coordinate()))
        # Set state -> Idle
        self.set_state(State1.CHARGING_STATE)
        self.move(cell)

    def retreat_translate(self, cell, best_known_path):
        self.write_file("retreat")
        cells = best_known_path
        current_index = cells.index(self.location)
        # Calculate the distance here
        cell_origin = cells[current_index]
        cell_to = cells[current_index + 1]
        self.add_time_translate(cell_origin, cell_to)

        self.location = cell_to
        self.battery_discharge_translate()
        self.move(cell)

    def battery_discharge_translate(self):
        new_battery = self.battery - self.translate_bat
        self.set_battery(new_battery)
        pass

    # IDLE STATE
    def move_idle(self, cell: Cell) -> None:
        self.time_idle += 1
        self.total_time += 1
        if not self.job.is_job_finished():
            # cambiar a translate state
            self.set_state(State1.TRANSLATE_STATE)
            self.move(cell)
        else:
            self.set_occupied(False)
        # si no está ocupado -> notificárselo al scheduler?
        pass

    # CHARGING STATE
    def add_time_charging(self, cell_origin, cell_to):
        self.time_charging += self.charging_time * 60
        check_time = self.time_idle + self.time_translate + self.time_charging + self.time_exploring + self.charging_time
        if self.max_time is not None and check_time >= self.max_time:
            self.is_max_time = True
        else:
            self.total_time += self.charging_time

    def battery_discharge(self):
        pass

    def move_charging(self, cell: Cell):
        battery_aux = self.get_battery()
        while battery_aux != 100:
            self.battery_charge_charging()
            battery_aux = self.get_battery()

            if battery_aux == 100:
                self.recharge = False
                self.add_time_charging(cell, cell)
                self.set_state(State1.IDLE_STATE)
                self.move(cell)

    def battery_charge_charging(self, charge_speed=10):
        time_to_charge = self.charging_time
        # self.time_charging += time_to_charge

        new_battery = charge_speed + self.get_battery()
        if new_battery > 100:
            aux = 100 - new_battery
            new_battery = new_battery + aux
        self.set_battery(new_battery)
