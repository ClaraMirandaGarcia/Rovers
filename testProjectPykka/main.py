from grid.grid import Grid
from planner import Planner
from rover1 import Rover as Rover1
from rover1 import State1
from fileManagement import FileManager
import time


class Main:
    def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers, max_time, name_file):

        # File output
        path_to_file = "log_files/"+name_file
        file_manager = FileManager(name_file, path_to_file)
        file_manager.open()

        # Preprocessing
        # Initialize variables
        grid = Grid(obser_rad, height, cave_wx, num_jobs, 1, name_file)

        jbs = grid.get_jobs()
        counter = 0
        file_manager.write("\n")
        file_manager.write("GRID MODELLING")
        for jb in jbs:
            for cell in jb.job_cells:
                file_manager.write("\n")
                file_manager.write("JOB: " + str(counter) + " - Cell location: " + str(cell.get_coordinate()))
            file_manager.write("\n")
            counter += 1
        file_manager.write("\n")
        # Sortear las celdas a explorar por prioridad -> TBD

        # Planner
        # El scheduler recibe los agentes, recibe los jobs, asigna (en este caso a
        # un solo agente) los trabajos. El trabajo pasa a estar fulfilled una vez que
        # todas sus celdas estén explored. JOB (fulfilled, started, not started)

        # def __init__(self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time):
        #actor_ref_1 = Rover.start(battery=100, state=ExploringState, translate_speed=2.4, exp_speed=0.1,
         #                       exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=grid, max_time=max_time,
          #                      name_rover="rover1")
        #actor_ref_2 = Rover.start(battery=90, state=ExploringState, translate_speed=2.4, exp_speed=0.1,
         #                       exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=grid, max_time=max_time,
          #                      name_rover="rover2")

        actor_ref_1 = Rover1.start(battery=100, state=State1.EXPLORING_STATE, translate_speed=0.1, exp_speed=0.05,
                                exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=grid, max_time=max_time,
                                name_rover="rover1")

        actor_ref_2 = Rover1.start(battery=100, state=State1.EXPLORING_STATE, translate_speed=0.1, exp_speed=0.05,
                                exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=grid, max_time=max_time,
                                name_rover="rover2")

        actor_ref_3 = Rover1.start(battery=100, state=State1.EXPLORING_STATE, translate_speed=0.1, exp_speed=0.05,
                                exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=grid, max_time=max_time,
                                name_rover="rover3")
        actor_ref_4 = Rover1.start(battery=300, state=State1.EXPLORING_STATE, translate_speed=0.5, exp_speed=0.1,
                                exp_bat=100, translate_bat=70, charging_time=3, grid=grid, max_time=max_time,
                                name_rover="rover4")


        #rover1 = actor_ref.proxy()

        planner_ref = Planner.start([actor_ref_1, actor_ref_2, actor_ref_3], 1, name_file, grid, max_time)
        planner = planner_ref.proxy()
        aus = grid.jobs
        planner.set_jobs(aus)
        planner.schedule()
        planner_ref.stop()
        actor_ref_1.stop()
        actor_ref_2.stop()



        # rover1 = actor_ref.proxy()
        file_manager.close()


# main = Main(0.25, 5.7, 3.3, 4, 1)
# main = Main(1, 4, 5, 3, 1)

# Cueva estrecha y la distancia
#main = Main(5, 292.1, 1, 2, 1)
#     def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers, tmax):
#main = Main(1, 5.5, 100, 4, 1, 15000)

if __name__ == "__main__":
    elapsed_time = 0 #Main(observ_rad, height, cave_wx, num_jobs, num_rovers, max_time, name_file)
    main = Main(1, 5.5, 2, 3, 3, None, "log4")
'''
    inp = input("Enter a mode (TM: maximum time mode/ AM: maximum area mode): ")

    while inp != "TM" and inp != "AM":
        print("Please, enter one of the available modes.")
        inp = input("Enter a mode (TM: maximum time mode/ AM: maximum area mode): ")

    if inp == "TM":
        name_file = input("Enter the name of the file: ")
        observ_rad = float(input("Enter the observation radio (m): "))
        height = float(input("Enter the height (m): "))
        num_jobs = int(input("Enter the num_jobs: "))
        num_rovers = int(input("Enter the num_rovers: "))
        max_time = int(input("Enter the Max_time(min): "))
        cave_wx = None
        start = time.time()
        Main(observ_rad, height, cave_wx, num_jobs, num_rovers, max_time, name_file)
        end = time.time()
        elapsed_time = end - start

    elif inp == "AM":
        name_file = input("Enter the name of the file: ")
        observ_rad = float(input("Enter the observation radio (m): "))
        height = float(input("Enter the height (m): "))
        cave_wx = float(input("Enter the cave_wx (m) "))
        num_jobs = int(input("Enter the num_jobs: "))
        num_rovers = int(input("Enter the num_rovers: "))
        max_time = None
        start = time.time()
        Main(observ_rad, height, cave_wx, num_jobs, num_rovers, max_time, name_file)
        end = time.time()
        elapsed_time = end - start

    print(f"Process finished")
    print(f"Elapsed time: {elapsed_time}")
    print(f"Output file created")
'''


