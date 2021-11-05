from grid.grid import Grid
from scheduler import Scheduler
from rover import Rover
from state.exploringState import ExploringState


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

        rover = Rover(battery=100, state=ExploringState, max_speed=1, min_speed=1,
                      max_bat=10, min_bat=5, charging_time=1)
        scheduler = Scheduler([rover])
        scheduler.schedule(grid.get_jobs())


main = Main(1, 5, 2, 2)
