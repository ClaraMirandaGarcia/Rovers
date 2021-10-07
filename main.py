from grid.grid import Grid
from grid.cell import Cell, CellState
from grid.job import Job, JobState
from scheduler import Scheduler
from rover import Rover
from state.exploringState import ExploringState


class Main:

    def __init__(self, explore_capacity, height, width, num_jobs):

        # Preprocessing

        # Initialize variables
        # -> Grid -> matriz formada por -> celdas { unexplored, explored }
        # -> Las celdas tienen que ser del tamaño de -> capacidad de exploración del agente

        area = height * width
        num_cells = area / explore_capacity
        cells = []

        it_var = 0
        while it_var < num_cells:
            cells.append(Cell(CellState.UNEXPLORED, explore_capacity))
            it_var += 1

        grid = Grid(cells)

        # -> Sobre este grid, se tienen que agrupar en trabajos JOBS, cuyo número está determinado
        # por el usuario.
        jobs = []
        job_cells = num_cells / num_jobs

        aux_job = 0
        while aux_job < num_jobs:
            cells_for_job = []
            aux_job += 1
            current_num_cells = 0

            for cell in cells:
                if (not cell.is_assigned()) and (current_num_cells < job_cells):
                    cell.set_assigned(True)
                    cells_for_job.append(cell)
                    current_num_cells += 1

            print("Job: "+str(aux_job)+" has: "+str(current_num_cells)+" assigned cells")
            jobs.append(Job(JobState.NOTSTARTED, cells_for_job))

        # Sortear las celdas a explorar por prioridad -> TBD

        # Scheduler
        # El scheduler recibe los agentes, recibe los jobs, asigna (en este caso a
        # un solo agente) los trabajos. El trabajo pasa a estar fulfilled una vez que
        # todas sus celdas estén explored. JOB (fulfilled, started, not started)

        agent = Rover(area, battery=100, state=ExploringState, max_speed=1, min_speed=1,
                      max_bat=10, min_bat=10, charging_time=1, cells_second=1)
        scheduler = Scheduler(1, area, [agent])
        scheduler.schedule(jobs)


main = Main(1, 5, 2, 2)
