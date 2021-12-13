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

    def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time):
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

        self.time_exploring = 0
        self.time_translate = 0
        self.time_idle = 0
        self.time_charging = 0

    def set_state(self, new_state):
        print(f"Agent: Transitioning to {new_state.__name__}")
        self.state = new_state
        self.state.set_context(self.state, context=self)

    def move(self, cell: Cell):
        self.state.move(self.state, cell)

    def move_to(self, cell: Cell):
        self.state.explore(self, cell)

    def battery_available(self, limit=10, move_cost=10) -> bool:
        # if battery needed to return to charging point < battery left
        battery_spent = 100 - self.get_battery()
        if (battery_spent + limit + move_cost) >= self.get_battery():
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
        self.best_known_path.append(best_cell)

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
            self.move(cell)
            self.job.change_state()
            print("Cell state: " + cell.get_cell_state().name)
            print("Job state: " + self.job.get_job_state().name)



        print("FINALLY")
        print(self.job.get_job_state())

    def on_receive(self, message):
        if message == "simple_strategy":
            self.simple_strategy()
        else:
            print('MESSAGE NOT MATCHED')
