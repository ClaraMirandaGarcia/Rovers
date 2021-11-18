from grid.cell import Cell, CellState
from grid.job import Job, JobState
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
        area = height * width
        num_cells = area / explore_capacity
        cells = self.calculate_cells(area, explore_capacity)

        job_cells = num_cells / num_jobs
        aux_job = 0
        while aux_job < num_jobs:
            cells_in_job = self.cells_for_job(cells, job_cells)
            print("Job: " + str(aux_job) + " has: " + str(len(cells_in_job)) + " assigned cells")
            self.add_job(Job(JobState.NOTSTARTED, cells_in_job))
            aux_job += 1

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
