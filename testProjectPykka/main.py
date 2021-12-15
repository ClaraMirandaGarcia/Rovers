from grid.grid import Grid
from grid.cell import Cell
from grid.cell import CellState
from planner import Planner
from rover import Rover
from coordinates import Coordinate

from state.exploringState import ExploringState
import pykka


class Main:
    def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers):
        # Preprocessing
        # Initialize variables
        grid = Grid(obser_rad, height, cave_wx, num_jobs, num_rovers)

        jbs = grid.get_jobs()
        counter = 0
        for jb in jbs:
            for cell in jb.job_cells:
                print("JOB: ", counter, " - Cell location: ", cell.get_coordinate())
            counter +=1

        # Sortear las celdas a explorar por prioridad -> TBD

        # Planner
        # El scheduler recibe los agentes, recibe los jobs, asigna (en este caso a
        # un solo agente) los trabajos. El trabajo pasa a estar fulfilled una vez que
        # todas sus celdas estén explored. JOB (fulfilled, started, not started)

        #def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time):
        actor_ref = Rover.start(battery=100, state=ExploringState, translate_speed=1, exp_speed=1,
                      exp_bat=10, translate_bat=5, charging_time=1, grid=grid)

        rover1 = actor_ref.proxy()

        planner_ref = Planner.start([actor_ref], 1)
        planner = planner_ref.proxy()
        planner.set_jobs(grid.get_jobs())
        planner.schedule()
        planner_ref.stop()
        actor_ref.stop()



#main = Main(0.25, 5.7, 3.3, 4, 1)
#main = Main(1, 4, 5, 3, 1)
main = Main(1, 5.5, 2, 1, 1)

