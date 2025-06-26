import os

from scheduler_module.errors_simulation import SimError
from scheduler_module.grid.cell import Cell
from scheduler_module.grid.job import Job
import pykka
from time import localtime, asctime
import time as t


class Rover(pykka.ThreadingActor):
    """

    Initialize the class Rover

        @param battery: initial battery of the rover
        @param state: initial state of the rover
        @param translate_speed: maximum speed reached, translate speed.
        @param min_speed: minimum speed, exploring speed.
        @param max_battery: maximum battery usage.
        @param min_battery: minimum battery usage.
        @param charging_time:
    """

    def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time, grid,
                 max_time, name_rover, name_folder, name_rover_file):

        self.file_manager = None
        self.name_file = name_rover_file
        self.name_folder = name_folder
        # Main characteristics of the rover
        self.battery = battery
        self.battery_capacity = battery
        self.state = state
        self.set_state(state)
        self.translate_speed = translate_speed
        self.exp_speed = exp_speed
        self.translate_bat = translate_bat
        self.exp_bat = exp_bat
        self.charging_time = charging_time
        # Auxiliar
        self.recharge = False
        self.best_known_path = []
        self.job = None
        self.location = None
        self.occupied = False
        self.grid = grid
        # Total time
        self.time_exploring = 0.0
        self.time_translate = 0.0
        self.time_idle = 0.0
        self.time_charging = 0.0
        self.total_time = 0.0
        self.max_time = max_time
        self.is_max_time = False
        self.area_explored = 0.0
        self.aux_translate_counter = 0
        self.aux_explore_counter = 0
        # path_to_file = "log_files/" + grid.file_manager.name_file + name_rover
        self.name_rover = name_rover
        self.name_rover_file = name_rover_file
        self.f = None
        self.errors = []
        self.cell = None
        # JSON creation
        self.date_sim = asctime(localtime())
        self.exploration_log = []
        self.job_movements = []
        self.json_file = {"name_rover": self.name_rover,
                          "date_sim": self.date_sim,
                          "exploration_log": self.exploration_log}
        super().__init__()

    def set_name_file(self, name_file):
        self.name_file = name_file

    def set_state(self, new_state):
        '''
        Changes the state of the rover
        :param new_state: new state of the rover
        '''
        self.state = new_state
        try:
            self.state.set_context(self)
        except TypeError:
            self.state.set_context(self.state, context=self)


    def move(self, cell: Cell):
        '''
        Method that sets the cell and invokes the move method of the state
        '''
        if self.location is None:
            self.cell = cell
            self.location = cell
        self.cell = cell
        self.state.move(cell)

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

    def battery_available(self, limit=10, move_cost=10) -> bool:
        '''
            returns whether the battery available is enough to continue
        '''
        # if battery needed to return to charging point + explore two more cells< battery left
        # battery to go back
        battery_to_cp = len(self.best_known_path) * self.translate_bat
        # cost of an exploring move * 2
        cost_move_exploring = self.exp_bat * 2
        # if (battery_to_cp + limit + move_cost) >= self.get_battery():
        if (battery_to_cp + cost_move_exploring) >= self.get_battery():
            return False
        return True

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
        '''
        Adds a cell to the best known path
        :param best_cell: cell to add
        '''
        # check if there exists a path from best_cell[0] hasta -> best_cell mejor que el que hay hasta entonces
        # search for min distance path
        self.best_known_path = self.find_better_path(best_cell)
        if best_cell not in self.best_known_path:
            self.best_known_path.insert(0, best_cell)

        self.write_file("\t\t" + "Known path: ")
        for cell in self.best_known_path:
            self.write_file("\t\t\t" + str(cell.get_coordinate()))

    def find_better_path(self, current_cell: Cell):
        '''
        Finds an alternative path from a cell
        :param current_cell: cell the rover is on
        '''
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
        cell_0 = self.job.job_cells[0]
        length_job_movements = len(self.job_movements)

        self.write_file(self.job.job_name + ": ")

        if self.location is None:
            point_0 = self.grid.find_charging_point_placement()
            shortest_path = self.grid.search_path(point_0, cell_0)

            while (not self.grid.is_path_explored(shortest_path, cell_0)):
                if not self.grid.is_job_accessible():
                    message = (
                            "The exploring operation could not be performed by the rover " + self.name_rover + " due to "
                                                                                                               "the lack "
                                                                                                               "of a known, "
                                                                                                               "accesible "
                                                                                                               "path.")
                    error = SimError("Battery Capacity", message)
                    self.errors.append(error)
                    self.job.errors.append(error)
                    self.grid.error_counter = self.grid.error_counter + 1
                    self.write_file(error.get_message())
                    break
                if self.aux_explore_counter > 50:
                    message = (
                            "The exploring operation could not be performed by the rover " + self.name_rover + " due to "
                                                                                                               "the lack "
                                                                                                               "of a known, "
                                                                                                               "accesible "
                                                                                                               "path.")
                    error = SimError("Path explored", message)
                    self.errors.append(error)
                    self.job.errors.append(error)
                    self.write_file(error.get_message())
                    self.aux_explore_counter = 0
                    break
                # the path is not explored, wait and try again
                t.sleep(2.5)
                self.aux_explore_counter = self.aux_explore_counter + 2.5
                self.write_file("\t\tRover waiting for free path")

            if len(shortest_path) > 1 and self.grid.is_path_explored(shortest_path, cell_0):
                # cambiar estado a translate
                self.set_state(ts.TranslateState("TranslateState"))
                self.write_file("\t\tAgent: Transitioning to " + str(self.state.__name__))
                # set location -> CP
                self.location = point_0
                # moverse hasta cell
                self.move(cell_0)

        # Check for an accessible cell
        # If accessible then explore
        # If not then eliminate the cell for the cells of the job

        # if charging point in job_cells -> start by cp

        for cell in self.job.job_cells:
            self.write_file("\tExploring cell " + str(cell_count))
            cell_count += 1
            if not self.is_max_time and not self.max_time == 0 and len(self.errors) == 0:
                self.move(cell)
                self.job.change_state()
                self.write_file("\t\tCell state: " + cell.get_cell_state().name)
                self.write_file("\t\tJob state: " + self.job.get_job_state().name)
            else:
                self.write_file("\t\tThe maximum time has been reached")
                break

        if len(self.job_movements) > length_job_movements:
            self.add_job_log(self.job_movements[len(self.job_movements) - 1])

        self.resume()

    def on_receive(self, message):
        if message == "simple_strategy":
            self.simple_strategy()
            return "FINISHED"
        else:
            print('MESSAGE NOT MATCHED')

    def on_stop(self):
        ...  # cleanup code in same context as on_receive()
        # self.get()
        self.stop()

    def add_job_log(self, data):
        to_append = {"job": self.job.job_name,
                     "movements": self.job_movements}

        self.exploration_log.append(to_append)
        self.json_file["exploration_log"] = self.exploration_log

    def add_movement_log(self, data):
        to_append = {"location": data}
        self.job_movements.append(to_append)

    def write_file_opening(self):
        self.f = open(self.name_file, "a")
        self.f.write("Output file for the rover " + self.name_file + "\n")
        self.f.write(asctime(localtime()) + "\n")
        self.f.close()


    def write_file(self, to_write):
        '''
        Write data
        '''
        self.f = open(self.name_file, "a")
        self.f.write(to_write + "\n")
        self.f.close()


    def resume(self):
        self.write_file("\n")
        self.write_file("\tRESUME" + "\n")
        self.write_file("\tTime exploring (min):" + "{:.2f}".format(self.time_exploring))
        self.write_file("\tTime translate (min):" + "{:.2f}".format(self.time_translate))
        self.write_file("\tTime charging (min):" + "{:.2f}".format(self.time_charging))
        self.write_file("\tTime idle (min):" + "{:.2f}".format(self.time_idle))
        self.write_file("\t---------------------------------------")
        self.write_file("\tTotal time calculated (min):" + "{:.2f}".format(
            self.time_idle + self.time_translate + self.time_charging + self.time_exploring))
        self.write_file("\tTotal explored (m^2):" + "{:.2f}".format(self.area_explored))
        self.write_file("\n")


class RoverModel:
    def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time, grid,
                 max_time, name_rover, name_rover_file):
        self.file_manager = None
        self.name_file = None
        self.battery = battery
        self.state = state
        self.translate_speed = translate_speed
        self.exp_speed = exp_speed
        self.translate_bat = translate_bat
        self.exp_bat = exp_bat
        self.charging_time = charging_time
        self.grid = grid
        self.max_time = max_time
        self.is_max_time = False
        self.name_rover = name_rover
        self.name_rover_file = name_rover_file

    def set_name_rover(self, name_rover):
        self.name_rover = name_rover

import scheduler_module.state.translateState as ts
