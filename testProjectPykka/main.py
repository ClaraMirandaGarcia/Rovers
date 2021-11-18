from grid.grid import Grid
from scheduler import Scheduler
from rover import Rover
from state.exploringState import ExploringState
import pykka


class Main:
    def __init__(self, explore_capacity, height, width, num_jobs):
        # Preprocessing

        # Initialize variables
        grid = Grid(explore_capacity, height, width, num_jobs)

        # Sortear las celdas a explorar por prioridad -> TBD

        # Scheduler
        # El scheduler recibe los agentes, recibe los jobs, asigna (en este caso a
        # un solo agente) los trabajos. El trabajo pasa a estar fulfilled una vez que
        # todas sus celdas estén explored. JOB (fulfilled, started, not started)

        actor_ref = Rover.start(battery=100, state=ExploringState, max_speed=1, min_speed=1,
                      max_bat=10, min_bat=5, charging_time=1)

        rover1 = actor_ref.proxy()
        scheduler_ref = Scheduler.start([actor_ref])
        scheduler = scheduler_ref.proxy()
        scheduler.set_jobs(grid.get_jobs())
        scheduler.schedule()
        #scheduler_ref.tell("simple_strategy")
        scheduler_ref.stop()
        actor_ref.stop()


main = Main(1, 5, 2, 2)

