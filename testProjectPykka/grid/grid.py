from grid.cell import Cell, CellState
from grid.job import Job, JobState
from coordinates import Coordinate
import numpy as np
import pykka


class Grid(pykka.ThreadingActor):
    def __init__(self, obser_rad, height, cave_wx, num_jobs, num_rovers):
        super().__init__()
        self.jobs = []
        self.num_rovers = num_rovers
        self.cells = []

        self.preprocess(obser_rad, height, cave_wx, num_jobs)

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
        print("best_path")
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

    def preprocess(self, obser_rad, height, cave_wx, num_jobs):

        explore_capacity = obser_rad ** 4

        # Calculating the new height in order to
        # obtain the logic grid
        new_height = self.approximate_value(explore_capacity, height)
        new_width = self.approximate_value(explore_capacity, cave_wx)

        area = new_height * new_width

        cells = self.find_cells(new_height, new_width, explore_capacity)
        self.set_cells(cells)
        num_cells = area / explore_capacity
        jobs = self.assign_jobs(cells, num_jobs, num_cells)
        self.jobs = jobs

    def set_cells(self, cells):
        self.cells = cells

    '''
    Obtains the next multiple of the explore capacity of a value.

    @explore_capacity
    @value_to_approximate
    '''

    def approximate_value(self, explore_capacity, value_to_approximate):
        aux = value_to_approximate // np.sqrt(explore_capacity)
        aux = aux * np.sqrt(explore_capacity)

        if aux < value_to_approximate:
            aux = self.find_next_multiple(aux, np.sqrt(explore_capacity))
        return aux

    '''
    Creates the cells to explore the cave
    @new_
    '''

    @staticmethod
    def find_cells(new_height, new_width, explore_capacity):
        len_y = int(new_width / np.sqrt(explore_capacity))
        len_x = int(new_height / np.sqrt(explore_capacity))
        cells = np.full((len_x, len_y), Cell(CellState.UNEXPLORED, explore_capacity))

        for i in range(len_x):
            for j in range(len_y):
                coordinate = Coordinate(x=i, y=j)
                if i == ((len_x // 2) - 1) and j == 0:
                    # Charging Point placement
                    cells[i][j] = Cell(CellState.EXPLORED, explore_capacity, True, coordinate)
                    cells[i][j].set_charging_point(True)
                else:
                    cells[i][j] = Cell(CellState.UNEXPLORED, explore_capacity, True, coordinate)

        return cells

    def find_charging_point_placement(self) -> Cell:
        cells = self.cells
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                if cells[i][j].is_charging_point():
                    return cells[i][j]

    @staticmethod
    def find_next_multiple(value, multiple):
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

    def assign_jobs(self, cells, num_jobs, num_cells):
        aux_jobs = []
        # set cells apart to pre-explore job
        if self.num_rovers > 1:
            pre_explore_cells = self.pre_explore(cells)
            aux_jobs.append(Job(JobState.NOTSTARTED, pre_explore_cells))

        if len(cells) <= 0:
            return aux_jobs

        for n in range(num_jobs):
            cells_to_assign = int(num_cells // (num_jobs - n))
            num_cells -= cells_to_assign
            aux_cells = self.assign_cells(cells, cells_to_assign, [], 0)
            aux_job = Job(JobState.NOTSTARTED, self.find_charging_point_placement(), aux_cells)
            aux_jobs.append(aux_job)

        return aux_jobs

    def assign_cells(self, cells, cells_to_assign, aux_cells: [], it):
        for i in range(it, len(cells)+1):
            pos_x = cells[i]
            pos_x = list(filter(lambda cell: not cell.is_assigned(), pos_x))

            if len(pos_x) == 0:
                print("There is no cell to assign in X:", i)

            elif cells_to_assign > len(pos_x):
                # Añadimos las celdas justas

                for j in range(len(pos_x)):
                    pos_x[j].set_assigned(True)
                aux_cells.extend(pos_x)
                cells_to_assign -= len(pos_x)

                if cells_to_assign > 0:
                    self.assign_cells(cells, cells_to_assign, aux_cells, i+1)

                return aux_cells

            else:
                pos_x = pos_x[:cells_to_assign]
                aux_cells.extend(pos_x)
                return aux_cells

