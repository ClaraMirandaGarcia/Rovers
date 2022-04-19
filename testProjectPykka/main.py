from grid.grid import Grid
from planner import Planner
from rover1 import Rover as Rover1
from rover1 import RoverModel
from rover1 import State1
from charging_point import ChargingPoint
from fileManagement import FileManager
import time


class Main:
    def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers, queue_models, max_time, name_file):

        # File output
        path_to_file = "log_files/" + name_file
        file_manager = FileManager(name_file, path_to_file)
        file_manager.open()

        # Preprocessing
        # Initialize variables
        charging_point = ChargingPoint.start(1, []).proxy()
        grid = Grid(obser_rad, height, cave_wx, num_jobs, 1, name_file, charging_point)

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

        # Creando las referencias a los actores para cada rover
        queue = []

        for j in range(num_rovers):
            rover = queue_models[j]
            actor_ref_j = Rover1.start(battery=rover.battery, state=rover.state, translate_speed=rover.translate_speed,
                                       exp_speed=rover.exp_speed,
                                       exp_bat=rover.exp_bat, translate_bat=rover.translate_bat,
                                       charging_time=rover.charging_time, grid=grid, max_time=max_time,
                                       name_rover=rover.name_rover)
            queue.append(actor_ref_j)

        # rover1 = actor_ref.proxy()

        planner_ref = Planner.start(queue, 1, name_file, grid, max_time)
        planner = planner_ref.proxy()
        aus = grid.jobs
        planner.set_jobs(aus)
        planner.schedule()
        planner_ref.stop()

        # rover1 = actor_ref.proxy()
        # pykka.get_all(queue) # TODO: BLOCKING
        # TODO: CLEAN UP pykka.ActorRegistry.stop_all()
        file_manager.close()


# main = Main(0.25, 5.7, 3.3, 4, 1)
# main = Main(1, 4, 5, 3, 1)

# Cueva estrecha y la distancia
# main = Main(5, 292.1, 1, 2, 1)
#     def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers, tmax):
# main = Main(1, 5.5, 100, 4, 1, 15000)

if __name__ == "__main__":
    elapsed_time = 0  # Main(observ_rad, height, cave_wx, num_jobs, num_rovers, max_time, name_file)

    num_rovers = int(input("Please, select the number of rovers of the simulation: "))
    queue_models = []
    print("Please, enter whether the fleet of rovers are of the same type or not.")
    inp = input("Enter the choice (Y: yes/ N: no): ")

    for i in range(int(num_rovers)):
        # self, battery, state, translate_speed, exp_speed, exp_bat, translate_bat, charging_time, grid,
        # max_time, name_rover
        print("Rover " + str(i))
        name_rover = input("Enter the name of the rover: ")
        battery = float(input("Enter the battery (m): "))
        translate_speed = float(input("Enter the translate speed (m): "))
        translate_bat = float(input("Enter the translate battery discharge (m): "))
        exp_speed = float(input("Enter the exploration speed (m): "))
        exp_bat = float(input("Enter the exploration battery discharge (m): "))
        charging_time = float(input("Enter the charging time (m): "))

        r = RoverModel(battery=battery, state=State1.EXPLORING_STATE, translate_speed=translate_speed,
                       translate_bat=translate_bat, exp_speed=exp_speed, exp_bat=exp_bat, charging_time=charging_time,
                       grid=None, max_time=None,
                       name_rover=name_rover)
        queue_models.append(r)
        if inp == "Y":
            for z in range(num_rovers-1):
                num = z +1
                r_aux = RoverModel(battery=r.battery, state=State1.EXPLORING_STATE, translate_speed=r.translate_speed,
                       translate_bat=r.translate_bat, exp_speed=r.exp_speed, exp_bat=r.exp_bat, charging_time=r.charging_time,
                       grid=None, max_time=None,
                       name_rover=r.name_rover)
                r_aux.set_name_rover("rover"+ str(z+1))
                queue_models.append(r_aux)
            break

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
        Main(observ_rad, height, cave_wx, num_jobs, num_rovers, queue_models, max_time, name_file)
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
        Main(observ_rad, height, cave_wx, num_jobs, num_rovers, queue_models, max_time, name_file)
        end = time.time()
        elapsed_time = end - start

    print(f"Process finished")
    print(f"Elapsed time: {elapsed_time}")
    print(f"Output file created")
