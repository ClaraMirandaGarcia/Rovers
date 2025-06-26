from coordinates import Coordinate
import numpy as np
import pykka
from scheduler_module.grid.cell import Cell, CellState
from scheduler_module.grid.job import JobState, Job


class Grid(pykka.ThreadingActor):
    def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers, name_file, charging_point):
        super().__init__()
        self.path_to_file = "log_files/" + name_file
        self.charging_point = charging_point
        self.jobs = []
        self.num_rovers = num_rovers
        self.cells = []
        aux_wx = cave_wx
        self.new_height = None
        self.new_width = None
        self.explore_capacity = None
        if aux_wx is None:
            aux_wx = 10
        self.__preprocess(obser_rad, height, aux_wx, num_jobs)
        self.cells_data = []
        self.json_file = {'len_x': self.cells.shape[0], 'len_y': self.cells.shape[1], 'cells_data': self.cells_data}
        self.error_counter = 0

    '''
        Obtains the next multiple of the explore capacity of a value.
    '''

    def __approximate_value(self, explore_capacity, value_to_approximate):
        v = np.sqrt(explore_capacity)
        aux = value_to_approximate // np.sqrt(explore_capacity)
        aux = aux * np.sqrt(explore_capacity)

        if aux < value_to_approximate:
            aux = self.__find_next_multiple(aux, np.sqrt(explore_capacity))
        return aux

    '''
    Creates the cells to explore the cave
    @new_
    '''

    def find_cells(self, new_height, new_width, explore_capacity, height, cave_wx):
        len_y = int(new_width / np.sqrt(explore_capacity))
        len_x = int(new_height / np.sqrt(explore_capacity))

        # check if the len_y < height
        # check if the len_x < width
        len = np.sqrt(explore_capacity)
        len_y_real = len
        len_x_real = len
        if len > height:
            len_y_real = height
        if len > cave_wx:
            len_x_real = cave_wx
        real_size = len_y_real * len_x_real
        capacity = len_y_real * len_x_real

        cells = np.full((len_x, len_y), Cell(CellState.UNEXPLORED, explore_capacity, real_size))

        num_cells = cells.size
        true_area = height * cave_wx
        resto_area = height * cave_wx
        resto_cells = num_cells
        real_size = real_size
        imaginary_area = new_height * new_width
        area_asigned = 0

        for i in range(len_x):
            for j in range(len_y):
                coordinate = Coordinate(x=i, y=j)

                if len_x == 1 and j == ((len_y // 2) - 1):
                    # Charging Point placement
                    cells[i][j] = Cell(CellState.EXPLORED, explore_capacity, real_size, True, coordinate)
                    cells[i][j].set_charging_point(True, self.charging_point)
                elif i == ((len_x // 2) - 1) and j == 0:
                    # Charging Point placement
                    cells[i][j] = Cell(CellState.EXPLORED, explore_capacity, real_size, True, coordinate)
                    cells[i][j].set_charging_point(True, self.charging_point)
                else:
                    cells[i][j] = Cell(CellState.UNEXPLORED, explore_capacity, real_size, True, coordinate)

                resto_area = resto_area - capacity
                area_asigned = area_asigned + capacity
                resto_cells = resto_cells - 1
                if (resto_area - explore_capacity) < explore_capacity and resto_cells > 0 and real_size == capacity:
                    lo_que_queda = true_area - area_asigned
                    real_size = lo_que_queda / resto_cells
                cells[i][j].set_real_size(real_size)
        return cells

    def __add_cell_data(self, cell_x, cell_y, area, is_explored, rover_name, size_cell):
        to_append = {'location':  [cell_y, cell_x],
                     'area': area,
                     'explored': is_explored,
                     'rover': rover_name,
                     'size': size_cell}
        self.cells_data.append(to_append)

    def update_json(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                cell = self.cells[i][j]
                self.__add_cell_data(cell.get_x(), cell.get_y(), cell.real_size, cell.is_cell_explored(), cell.rover_explored(), cell.size)

        self.json_file['cells_data'] = self.cells_data

    def is_job_accessible(self):
        error_counter = 0
        for j in self.jobs:
            if len(j.errors) > 0:
                error_counter = error_counter + 1

        if error_counter == len(self.jobs) - 1:
            return False
        return True

    @staticmethod
    def is_path_explored(path, cell):
        is_explored = True
        cells_filtered = list(filter(lambda c: not c.is_cell_explored() and cell != c, path))

        if len(cells_filtered) > 0:
            is_explored = False
        return is_explored

    def search_path(self, charging_point, current_cell):
        best_path = [current_cell]
        while not current_cell.is_charging_point():
            # check for accessible cells already explored
            accessible_cells = self.get_cells_accessible_from(charging_point, current_cell)
            # check min distance cell
            min_cell = self.get_closest_cell_simple(charging_point, accessible_cells)
            # append it
            best_path.append(min_cell)
            current_cell = min_cell
        return best_path

    @staticmethod
    def get_closest_cell_simple(charging_point, cells):
        closest_cell = cells[0]
        cp = charging_point
        min_distance = closest_cell.distance_to(cp)

        for i in range(1, len(cells)):
            cell_from = cells[i]
            distance = cell_from.distance_to(cp)
            if distance < min_distance:
                min_distance = distance
                closest_cell = cell_from
        return closest_cell

    def get_cells_accessible_from(self, charging_point, current_cell):
        list_accessible_cells = []
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if current_cell.is_accessible(self.cells[i][j]):
                    list_accessible_cells.append(self.cells[i][j])
        if current_cell.is_accessible(charging_point):
            list_accessible_cells.append(charging_point)
        return list_accessible_cells

    def add_job(self, job):
        self.jobs.append(job)

    def get_jobs(self) -> []:
        return self.jobs

    def __preprocess(self, obser_rad, height, cave_wx, num_jobs):

        self.explore_capacity = 2*obser_rad ** 2
        # limiting it to two decimals
        self.explore_capacity = round(self.explore_capacity, 2)
        # Calculating the new height in order to
        # obtain the logic grid
        self.new_height = self.__approximate_value(self.explore_capacity, height)
        self.new_width = self.__approximate_value(self.explore_capacity, cave_wx)
        area = self.new_height * self.new_width
        cells = self.find_cells(self.new_height, self.new_width, self.explore_capacity, height, cave_wx)
        self.set_cells(cells)
        num_cells = area / self.explore_capacity
        jobs = self.__assign_jobs(cells, num_jobs, cells.size)
        jobs = self.__priorize_jobs(jobs)
        self.jobs = jobs

    def __priorize_jobs(self, jobs):
        if jobs[0].has_cp():
            return jobs
        # else
        priorized_jobs = []
        copy_jobs= jobs.copy()

        for job in jobs:
            if job.has_cp():
                priorized_jobs.append(job)
        divisor = jobs.index(priorized_jobs[0])
        first_half = copy_jobs[:divisor]
        if priorized_jobs[0] in first_half:
            first_half.remove(priorized_jobs[0])

        second_half = copy_jobs[divisor:]
        if priorized_jobs[0] in second_half:
            second_half.remove(priorized_jobs[0])

        priorized_jobs.extend(second_half)
        if len(first_half) > 1:
            list_reversed = first_half[::-1]
            priorized_jobs.extend(list_reversed)
        else:
            priorized_jobs.extend(first_half)
        return priorized_jobs

    def set_cells(self, cells):
        self.cells = cells

    def find_charging_point_placement(self) -> Cell:
        cells = self.cells
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                if cells[i][j].is_charging_point():
                    return cells[i][j]

    @staticmethod
    def __find_next_multiple(value, multiple):
        return value + multiple

    @staticmethod
    def pre_explore(cells):
        cells_job = []
        i = 0
        while i < len(cells):
            for j in range(len(cells[i])):
                if j < 2:
                    cells_job.append(cells[i][j])
            i += 1
        return cells_job

    def __assign_jobs(self, cells, num_jobs, num_cells):
        aux_jobs = []
        aux = 0
        # set cells apart to pre-explore job
        if self.num_rovers > 1:
            pre_explore_cells = self.pre_explore(cells)
            job_name = "Job "+str(aux)
            aux_jobs.append(Job(job_name, JobState.NOTSTARTED, pre_explore_cells))
            aux += 1

        if len(cells) <= 0:
            return aux_jobs

        for n in range(num_jobs):
            cells_to_assign = int(num_cells // (num_jobs - n))
            num_cells -= cells_to_assign
            aux_cells = self.__assign_cells(cells, cells_to_assign, [], 0)
            job_name = "Job " + str(aux)
            aux_job = Job(job_name, JobState.NOTSTARTED, self.find_charging_point_placement(), aux_cells)
            aux_jobs.append(aux_job)
            aux += 1

        return aux_jobs

    def get_explored_cells(self):
        aux_list = []
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j].is_cell_explored():
                    aux_list.append(self.cells[i][j])
        return aux_list

    def __assign_cells(self, cells, cells_to_assign, aux_cells: [], it):
        for i in range(it, len(cells)+1):
            # error
            pos_x = cells[i]
            pos_x = list(filter(lambda cell: not cell.is_assigned(), pos_x))

            if len(pos_x) == 0:
                print("")

            elif cells_to_assign > len(pos_x):

                for j in range(len(pos_x)):
                    pos_x[j].set_assigned(True)
                aux_cells.extend(pos_x)
                cells_to_assign -= len(pos_x)

                if cells_to_assign > 0:
                    self.__assign_cells(cells, cells_to_assign, aux_cells, i + 1)
                return aux_cells

            else:
                pos_x = pos_x[:cells_to_assign]
                aux_cells.extend(pos_x)
                return aux_cells

