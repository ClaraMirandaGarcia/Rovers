from grid.cell import Cell
from grid.job import Job


class Rover:

    # distancia mínima / velocidad máxima
    # velocidad máxima
    # velocidad mínima
    # gasto de batería máximo
    # gasto de batería mínimo
    # punto de carga -> ? que tenga atributos: available, queue (de agentes)
    # tiempo de carga (necesario para el 100%)
    # autonomy time???
    def __init__(self, battery, state, max_speed, min_speed, max_bat, min_bat, charging_time,
                 cells_second):

        self.battery = battery
        self.state = state
        self.set_state(state)
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.max_bat = max_bat
        self.min_bat = min_bat
        self.charging_time = charging_time
        self.cells_second = cells_second
        self.recharge = False
        self.best_known_path = []
        self.job = None
        self.location = None
        self.occupied = False

        self.time_exploring = 0
        self.time_translate = 0
        self.time_iddle = 0
        self.time_charging = 0

    def set_state(self, new_state):
        print(f"Agent: Transitioning to {new_state.__name__}")
        self.state = new_state
        self.state.set_context(self.state, context=self)

    def move(self, cell: Cell):
        self.state.move(self.state, cell)

    def move_to(self, cell: Cell):
        self.state.explore(self, cell)

    def battery_available(self) -> bool:
        # if battery needed to return to charging point < battery left
        battery_spent = 100 - self.battery
        if battery_spent < self.battery:
            return True
        return False

    # Calcular la máxima distancia que se puede mover con la batería
    # actual, depende del estado en el que se encuentre.
    # def maxDistance:

    # Battery
    def set_battery(self, new_battery):
        self.battery = new_battery
        pass

    def get_battery(self) -> int:
        return self.battery

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

    def simple_strategy(self):
        cell_count = 0
        for cell in self.job.job_cells:
            print("Exploring cell " + str(cell_count))
            cell_count += 1
            self.move(cell)
            self.job.change_state()
            print("Cell state: " + cell.get_cell_state().name)
            print("Job state: " + self.job.get_job_state().name)

        print("FINALLY")
        print(self.job.get_job_state())
