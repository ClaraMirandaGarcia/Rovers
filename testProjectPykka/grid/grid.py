from grid.cell import Cell, CellState
from grid.job import Job, JobState
from coordinates import Coordinate
import numpy as np
import pykka


class Grid(pykka.ThreadingActor):
    def __init__(self, explore_capacity, height, width, num_jobs):
        super().__init__()
        self.jobs = []
        self.preprocess(explore_capacity, height, width, num_jobs)

    def add_job(self, job):
        self.jobs.append(job)

    def get_jobs(self) -> []:
        return self.jobs

    def preprocess(self, explore_capacity, height, width, num_jobs):
        # Calculating the new height in order to
        # obtain the logic grid
        new_height = self.approximate_value(explore_capacity, height)
        new_width = self.approximate_value(explore_capacity, width)

        area = new_height * new_width

        cells = self.find_cells(new_height, new_width, explore_capacity)
        # cells = self.calculate_cells(area, explore_capacity)
        num_cells = area / explore_capacity

        jobs = self.assign_jobs(cells, num_jobs, num_cells)
        self.jobs = jobs
        '''
        job_cells = num_cells / num_jobs

        aux_job = 0
        while aux_job < num_jobs:
            cells_in_job = self.cells_for_job(cells, job_cells)
            print("Job: " + str(aux_job) + " has: " + str(len(cells_in_job)) + " assigned cells")
            self.add_job(Job(JobState.NOTSTARTED, cells_in_job))
            aux_job += 1
        '''

    def approximate_value(self, explore_capacity, value_to_approximate):
        aux = value_to_approximate // np.sqrt(explore_capacity)
        aux = aux * np.sqrt(explore_capacity)

        if aux < value_to_approximate:
            aux = self.find_next_multiple(aux, np.sqrt(explore_capacity))
        return aux

    @staticmethod
    def find_cells(new_height, new_width, explore_capacity):
        len_y = int(new_height / np.sqrt(explore_capacity))
        len_x = int(new_width / np.sqrt(explore_capacity))
        cells = np.full((len_x, len_y), Cell(CellState.UNEXPLORED, explore_capacity))

        for i in range(len_x):
            for j in range(len_y):
                coordinate = Coordinate(x=i, y=j)
                if i == 0 and j == 0:
                    # Charging Point placement
                    cells[i][j] = Cell(CellState.EXPLORED, explore_capacity, True, coordinate)
                else:
                    cells[i][j] = Cell(CellState.UNEXPLORED, explore_capacity, True, coordinate)

        return cells

    @staticmethod
    def find_next_multiple(value, multiple):
        return value + multiple

    def assign_jobs(self, cells, num_jobs, num_cells):
        aux_jobs = []

        for n in range(num_jobs):
            print("JOB ", n)
            cells_to_assign = int(num_cells // (num_jobs - n))

            print("Número de celdas para asignar")
            print(cells_to_assign)
            num_cells -= cells_to_assign
            aux_job = self.assign_cells(cells, cells_to_assign)
            aux_jobs.append(aux_job)
            # del cells[:cells_assigned]

        return aux_jobs

    @staticmethod
    def assign_cells(cells, cells_to_assign):
        aux_cells = []
        for i in range(len(cells)):
            print("X: ", i)
            pos_x = cells[i]
            pos_x = list(filter(lambda cell: not cell.is_assigned(), pos_x))
            print("Non-assigned cells: ", pos_x)

            if len(pos_x) == 0:
                print("There is no cell to assign in X:", i)

            elif cells_to_assign > len(pos_x):
                # Añadimos las celdas justas
                print("Assigning cells: ", pos_x)
                aux_cells.extend(pos_x)
                cells_to_assign -= len(pos_x)
                extra = 1

                while cells_to_assign > 0:

                    print("Cells extra to assign", cells_to_assign)
                    pos_y = cells[i + extra][-cells_to_assign:]
                    print("Assigning cells: ", pos_y)
                    for cell in range(len(pos_y)):
                        print("Coordinates of the cell ", pos_y[cell].coordinate)

                    # Añadimos las celdas extra
                    aux_cells.extend(pos_y)
                    cells_to_assign -= len(pos_y)
                    extra += 1
                # Create a job with that cell and add it to the grid.
                return Job(JobState.NOTSTARTED, aux_cells)

            else:
                print("There are enough cells")
                pos_x = pos_x[:cells_to_assign]
                print("Assigning cells ", pos_x)
                aux_cells.extend(pos_x)
                return Job(JobState.NOTSTARTED, aux_cells)

    @staticmethod
    def calculate_cells(area, explore_capacity) -> []:
        num_cells = area / explore_capacity
        cells = []

        it_var = 0
        while it_var < num_cells:
            cells.append(Cell(CellState.UNEXPLORED, explore_capacity))
            it_var += 1
        return cells

    @staticmethod
    def cells_for_job(cells, job_cells) -> []:
        cells_aux = []
        current_num_cells = 0

        for cell in cells:
            if (not cell.is_assigned()) and (current_num_cells < job_cells):
                cell.set_assigned(True)
                cells_aux.append(cell)
                current_num_cells += 1

        return cells_aux
