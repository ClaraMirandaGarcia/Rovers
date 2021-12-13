from enum import Enum, auto
import grid.cell as Cell


class JobState(Enum):
    FULFILLED = auto()
    STARTED = auto()
    NOTSTARTED = auto()


class Job:

    def __init__(self, state: JobState, charging_point: Cell, job_cells):
        self.state = state
        self.charging_point = charging_point
        self.job_cells = []
        self.set_job_cells(job_cells)
        self.time_to_explore = 0

    def set_job_cells(self, job_cells):
        for cell in job_cells:
            cell.set_assigned(True)
        self.job_cells = job_cells
        #TO-DO: ordenar las celdas
        aux_cells = self.prioritize_cells(job_cells)
        self.job_cells = aux_cells

    def prioritize_cells(self, job_cells)->[]:
        prioritized_cells = []
        aux_cells = job_cells
        # Computing the closest cell to the charging point
        # Initial point from where the rover starts to explore
        closest_cell = self.get_closest_cell(aux_cells)
        prioritized_cells.append(closest_cell)

        for cell in aux_cells:
            if cell not in prioritized_cells:
                # compute the accessible cells from closest_cell
                cells = self.get_cells_accessible_from(closest_cell)
                # find the closest accessible cell
                closest_cell = self.get_closest_cell(cells)
                # add it to the prioritized list
                prioritized_cells.append(closest_cell)
        return prioritized_cells

    def get_cells_accessible_from(self, closest_cell):
        list_accessible_cells = []
        for i in range(len(self.job_cells)):
            if closest_cell.is_accessible(self.job_cells[i]):
                list_accessible_cells.append(self.job_cells[i])
        return list_accessible_cells

    def get_closest_cell(self, job_cells):
        closest_cell = job_cells[0]
        cp = self.charging_point

        min_distance = closest_cell.distance_to(cp)

        for cell_from in job_cells:
            distance = cell_from.distance_to(cp)

            if distance < min_distance:
                min_distance = distance
                closest_cell = cell_from

        return closest_cell

    def job_started(self) -> bool:
        cells_explored = False
        for cell in self.job_cells:
            if cell.is_explored():
                cells_explored = True
        return cells_explored

    def job_fulfilled(self) -> bool:
        job_fulfilled = True
        for cell in self.job_cells:
            if not cell.is_explored():
                job_fulfilled = False
        return job_fulfilled

    def change_state(self):
        fulfilled = self.job_fulfilled()
        started = self.job_started()

        if fulfilled:
            self.set_job_state(JobState.FULFILLED)
        elif started:
            self.set_job_state(JobState.STARTED)
        else:
            self.set_job_state(JobState.NOTSTARTED)

    def set_job_state(self, state):
        self.state = state

    def get_job_state(self) -> JobState:
        return self.state

    def set_time_to_explore(self, time_to_explore):
        self.time_to_explore = time_to_explore

    def set_charging_point(self, charging_point):
        self.charging_point = charging_point

    def get_charging_point(self):
        return self.charging_point

