from grid.cell import Cell
from grid.job import Job
from fileManagement import FileManager
import pykka
from time import localtime, asctime
import threading


class Rover(pykka.ThreadingActor):
    """
    CURRENTLY IT IS NOT BEING USED.

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
        self.f.write(f"{thread_name}: {to_write}" + "\n")
        # self.f.write("ROVER: "+self.name_rover+" - "+"\n")
        self.f.write(to_write)
        self.f.close()

    def set_name_file(self, name_file):
        self.name_file = name_file

    def set_state(self, new_state):
        if self.file_manager is not None:
            self.write_file(f"Agent: Transitioning to {new_state.__name__}")
        # self.file_manager.write("Agent: Transitioning to {new_state.__name__}")
        self.state = new_state
        self.state.set_context(self.state, context=self)

    def move(self, cell: Cell):
        if self.location is None:
            self.location = cell
        self.state.move(self.state, cell)

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

        self.write_file("\n")
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

        for cell in self.job.job_cells:
            self.write_file("Exploring cell " + str(cell_count) + "\n")
            # self.file_manager.write("Exploring cell " + str(cell_count))
            cell_count += 1
            if not self.is_max_time and not self.max_time == 0:
                self.move(cell)
                self.job.change_state()
                # rises -> problem
                self.write_file("Cell state: " + cell.get_cell_state().name + "\n")
                self.write_file("Job state: " + self.job.get_job_state().name + "\n")

        self.write_file("FINISHING" + "\n")
        self.write_file(str(self.job.get_job_state()))

        self.write_file("\n")
        self.write_file("\n")
        self.write_file("RESUME" + "\n")
        self.write_file("Time exploring (min):" + "{:.2f}".format(self.time_exploring) + "\n")
        self.write_file("Time translate (min):" + "{:.2f}".format(self.time_translate) + "\n")
        self.write_file("Time charging (min):" + "{:.2f}".format(self.time_charging) + "\n")
        self.write_file("Time idle (min):" + "{:.2f}".format(self.time_idle) + "\n")
        self.write_file("---------------------------------------" + "\n")
        self.write_file("Total time calculated (min):" + "{:.2f}".format(
            self.time_idle + self.time_translate + self.time_charging + self.time_exploring) + "\n")
        self.write_file("Total explored (m^2):" + "{:.2f}".format(self.area_explored) + "\n")
        self.write_file("\n")

    def simple_strategy_area(self):
        """
            Performs a simple strategy for the rover with the jobs given.
        """
        cell_count = 0

        # Check for an accessible cell
        # If accessible then explore
        # If not then eliminate the cell for the cells of the job

        for cell in self.job.job_cells:
            self.write_file("Exploring cell " + str(cell_count) + "\n")
            # self.file_manager.write("Exploring cell " + str(cell_count))
            cell_count += 1
            self.move(cell)
            self.job.change_state()
            # rises -> problem
            self.write_file("Cell state: " + cell.get_cell_state().name + "\n")
            self.write_file("Job state: " + self.job.get_job_state().name + "\n")

        self.write_file("FINISHING" + "\n")
        self.write_file(self.job.get_job_state())
        self.write_file("\n")
        self.write_file("RESUME" + "\n")
        self.write_file("Time exploring:" + str(self.time_exploring) + "\n")
        self.write_file("Time translate:" + str(self.time_translate) + "\n")
        self.write_file("Time charging:" + str(self.time_charging) + "\n")
        self.write_file("Time idle:" + str(self.time_idle) + "\n")
        self.write_file("---------------------------------------" + "\n")
        self.write_file("Total time calculated: " +
                        str(self.time_idle + self.time_translate + self.time_charging + self.time_exploring) + "\n")
        self.write_file("Total explored: " + str(self.area_explored) + "\n")
        self.write_file("\n")

    def on_receive(self, message):
        if message == "simple_strategy":
            self.simple_strategy()
        elif message == "simple_strategy_max_time":
            self.simple_strategy_time()
        elif message == "simple_strategy_max_area":
            self.simple_strategy_area()
        else:
            print('MESSAGE NOT MATCHED')
