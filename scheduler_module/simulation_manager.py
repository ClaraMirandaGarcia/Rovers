import os
from pathlib import Path
import json
import pykka
from scheduler_module.errors_simulation import SimError
from scheduler_module.grid.grid import Grid
from scheduler_module.planner import Planner
from scheduler_module.rover import Rover as Rover_Original
import scheduler_module.state.exploringState as es
from scheduler_module.charging_point import ChargingPoint


class SimulationManager:
    def __init__(self, sim_controller, obser_rad, height, cave_wx, num_jobs, num_rovers, queue_models, max_time):
        # Create the directory if it does not exist
        if sim_controller is not None:
            self.sim_controller = sim_controller

        # Round progress bar
        self.sim_controller.pop_up_in()
        self.__create_folder(sim_controller, "\log_files")
        # Folder for current simulation
        name_file = self.__automatic_name_file()

        path_to_folder = "\log_files\\" + name_file
        self.__create_folder(sim_controller, path_to_folder)
        path_to_file = "log_files\\" + name_file + "\\resume.txt"

        # Preprocessing
        # Initialize variables
        self.__data_0_log(path_to_file, obser_rad, height, cave_wx, num_jobs, num_rovers, max_time)
        charging_point = ChargingPoint.start(1, []).proxy()
        grid = Grid(obser_rad, height, cave_wx, num_jobs, 1, name_file, charging_point)
        self.__data_1_log(path_to_file, grid, max_time)
        self.__grid_log(path_to_file, grid)

        # Creating the references to the actors for each rover
        queue = self.__create_rovers(grid, max_time, num_rovers, queue_models, path_to_folder)

        # self.sim_controller.show_window_progress()

        # Scheduling
        aus = grid.jobs
        planner_ref = Planner.start(queue, name_file, grid, max_time, aus)
        planner_ref.ask("schedule", True)
        planner_ref.stop()
        pykka.ActorRegistry.stop_all()

        if sim_controller is not None:
            self.sim_controller.pop_up()
            # the simulation has finished
            total_time, total_space = self.__calculate_total(queue)
            self.__save_json_files(queue)
            resume = SimulationModel(total_time, total_space, len(queue), name_file)
            self.sim_controller.save_simulation(resume, queue)
            grid.update_json()
            self.__save_json_grid(grid, path_to_file)

    @staticmethod
    def __save_json_files(queue):
        for rover in queue:
            # for each actor write the file corresponding to the json.
            json_data = rover._actor.json_file
            # open file and write
            if rover._actor.name_file is not None:
                path_to_file = rover._actor.name_file + ".json"

                with open(path_to_file, 'w') as fp:
                    json.dump(json_data, fp)

    @staticmethod
    def __save_json_grid(grid, path_to_file):
        json_data = grid.json_file
        path_to_file = path_to_file + ".json"

        with open(path_to_file, 'w') as fp:
            json.dump(json_data, fp)

    @staticmethod
    def __calculate_total(queue):
        sum_time = 0
        sum_space = 0
        for rover in queue:
            sum_time = sum_time + rover._actor.total_time
            sum_space = sum_space + rover._actor.area_explored
        return sum_time, sum_space

    @staticmethod
    def __create_rovers(grid, max_time, num_rovers, queue_models, name_folder):
        queue = []
        for j in range(num_rovers):
            rover = queue_models[j]
            # auxiliar para rover original
            aux_state = es.ExploringState("ExploringState")
            actor_ref_j = Rover_Original.start(battery=rover.battery, state=aux_state,
                                               translate_speed=rover.translate_speed,
                                               exp_speed=rover.exp_speed,
                                               exp_bat=rover.exp_bat, translate_bat=rover.translate_bat,
                                               charging_time=rover.charging_time, grid=grid, max_time=max_time,
                                               name_rover=rover.name_rover, name_folder=name_folder,
                                               name_rover_file=rover.name_rover_file)
            queue.append(actor_ref_j)
        return queue

    def __data_0_log(self, path, obser_rad, height, cave_wx, num_jobs, num_rovers, max_time):
        f = open(path, "a")
        f.write("\n")
        f.write("Fixed parameters:" + "\n")
        num_jobs = str(num_jobs)
        num_rovers = str(num_rovers)
        f.write("\tNumber of jobs: " + num_jobs + "\n")
        f.write("\tNumber of rovers: " + num_rovers + "\n")
        f.write("\tObservation radio: " + "{:.2f}".format(obser_rad) + "\n")
        f.write("\n")
        f.write("Initial data:" + "\n")
        if max_time is None:
            f.write("\tMode selected: MAX_AREA" + "\n")
            f.write("\tHeight: " + "{:.2f}".format(height) + "\n")
            f.write("\tWidth: " + "{:.2f}".format(cave_wx) + "\n")
        else:
            f.write("\tMode selected: MAX_TIME" + "\n")
            f.write("\tHeight: " + "{:.2f}".format(height) + "\n")
            f.write("\tMaximum time: " + "{:.2f}".format(max_time) + "\n")

        f.close()

    def __data_1_log(self, path, grid, max_time):
        f = open(path, "a")
        f.write("\n")
        f.write("Processed data:" + "\n")
        explore_capacity = str(grid.explore_capacity)
        f.write("\tExplore capacity: " + explore_capacity + "\n")
        if max_time is None:
            f.write("\tHeight: " + "{:.2f}".format(grid.new_height) + "\n")
            f.write("\tWidth: " + "{:.2f}".format(grid.new_width) + "\n")
        else:
            f.write("\tHeight: " + "{:.2f}".format(grid.new_height) + "\n")
            f.write("\tMaximum time: " + "{:.2f}".format(max_time) + "\n")

        f.close()

    @staticmethod
    def __grid_log(path, grid):
        f = open(path, "a")
        jbs = grid.get_jobs()
        counter = 0
        f.write("\n")
        f.write("Grid Model:")
        for jb in jbs:
            f.write("\n")
            f.write("\tJob " + str(counter) + ":")
            counter1 = 0
            for cell in jb.job_cells:
                f.write("\n")
                f.write("\t\tCell: " + str(counter1) + " - Cell location: " + str(cell.get_coordinate()) + " - Cell "
                                                                                                           "area: "
                                                                                                           "" + "{:.2f}".format(
                    cell.real_size))
                counter1 = counter1 + 1
            f.write("\n")
            counter += 1
        f.write("\n")
        f.close()

    def __create_folder(self, sim_controller, name_folder):
        path = os.getcwd() + name_folder
        access_rights = 0o755
        try:
            if not os.path.exists(path):
                os.mkdir(path, access_rights)
        except OSError as error:
            message = "Creation of the directory %s failed" % path
            error = SimError("Directory creation error", message)
            if sim_controller is not None:
                self.sim_controller.pop_up(error.get_motive(), error.get_message())

    @staticmethod
    def __automatic_name_file():
        cwd = os.getcwd() + "\\log_files"
        paths = sorted(Path(cwd).iterdir(), key=os.path.getmtime)
        if len(paths) > 0:
            last_sim_name = paths[len(paths) - 1]
            last_sim_name = last_sim_name.stem
            last_sim_name = last_sim_name.split("_")
            last_sim_name = last_sim_name[1]
            try:
                num = int(last_sim_name)
                num = num + 1
                return "sim_" + str(num)
            except Exception:
                print("ERROR")
        else:
            return "sim_1"  # get num


class SimulationModel:
    def __init__(self, total_time, total_space, num_rovers, log_file_name):
        self.name = log_file_name.split(".")[0]
        self.total_time = total_time
        self.total_space = total_space
        self.num_rovers = num_rovers
        # get
        current_path = os.getcwd()
        self.log_file_name = current_path + "\\" + "log_files" + "\\" + log_file_name
