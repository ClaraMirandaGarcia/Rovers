from grid.cell import Cell
from grid.job import Job
import pykka


class Rover(pykka.ThreadingActor):
    """Initialize the class Rover

        @param battery: initial battery of the rover
        @param state: initial state of the rover
        @param translate_speed: maximum speed reached, translate speed.
        @param min_speed: minimum speed, exploring speed.
        @param max_battery: maximum battery usage.
        @param min_battery: minimum battery usage.
        @param charging_time:
    """

    def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time, grid):
        super().__init__()
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

    def set_state(self, new_state):
        print(f"Agent: Transitioning to {new_state.__name__}")
        self.state = new_state
        self.state.set_context(self.state, context=self)

    def move(self, cell: Cell):
        self.location = cell
        self.state.move(self.state, cell)

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

    # Best known path
    def add_best_cell(self, best_cell: Cell):
        # check if there exists a path from best_cell[0] hasta -> best_cell mejor que el que hay hasta entonces
        # search for min distance path
        self.best_known_path = self.find_better_path(best_cell)
        if self.job.charging_point not in self.best_known_path:
            print("E")
        print("BEST KNOWN PATH")
        for cell in self.best_known_path:
            print(cell.get_coordinate())

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

    '''
    Performs a simple strategy for the rover with the jobs given.
    '''

    def simple_strategy(self):
        cell_count = 0

        # Check for an accessible cell
        # If accessible then explore
        # If not then eliminate the cell for the cells of the job

        for cell in self.job.job_cells:
            print("The cell can be accessed")
            print("Exploring cell " + str(cell_count))
            cell_count += 1
            # self.location(cell)
            self.move(cell)
            self.job.change_state()
            # rises -> problem
            print("Cell state: " + cell.get_cell_state().name)
            print("Job state: " + self.job.get_job_state().name)

        print("FINALLY")
        print(self.job.get_job_state())

    def on_receive(self, message):
        if message == "simple_strategy":
            self.simple_strategy()
        else:
            print('MESSAGE NOT MATCHED')
