from enum import Enum, auto
import grid.cell as Cell
import pykka


class JobState(Enum):
    FULFILLED = auto()
    STARTED = auto()
    NOTSTARTED = auto()


class Job(pykka.ThreadingActor):

    def __init__(self, state: JobState, charging_point: Cell, job_cells):
        self.state = state
        self.charging_point = charging_point
        self.job_cells = []
        self.set_job_cells(job_cells)
        self.time_to_explore = 0

    def is_job_finished(self):
        return self.state == JobState.FULFILLED

    def get_first_cell(self):
        for i in range(len(self.job_cells)):
            if not self.job_cells[i].is_explored():
                return self.job_cells[i]

    def set_job_cells(self, job_cells):
        for cell in job_cells:
            cell.set_assigned(True)
        self.job_cells = job_cells
        # TO-DO: ordenar las celdas
        aux_cells = self.prioritize_cells(job_cells)
        self.job_cells = aux_cells

    def prioritize_cells(self, job_cells) -> []:
        prioritized_cells = []
        aux_cells = job_cells.copy()

        # Computing the closest cell to the charging point
        # Initial point from where the rover starts to explore
        closest_cell = self.get_closest_cell(aux_cells, prioritized_cells)
        prioritized_cells.append(closest_cell)
        cells = self.get_cells_accessible_from(closest_cell)
        cells = list(filter(lambda c: c in job_cells, cells))
        counter = 0

        while counter < len(job_cells) - 1:
            # for cell in cells:
            if closest_cell in aux_cells:
                aux_cells.remove(closest_cell)
                cells = self.get_cells_accessible_from(closest_cell)
                cells = list(filter(lambda c: c in job_cells, cells))
            # find the closest accessible cell -> sometimes it always get the same
            closest_cell = self.get_closest_cell(cells, prioritized_cells)
            # add it to the prioritized list
            if (closest_cell not in prioritized_cells) and (closest_cell in job_cells):
                prioritized_cells.append(closest_cell)
                # compute the accessible cells from closest_cell
                cells = self.get_cells_accessible_from(closest_cell)
            counter += 1

        if len(prioritized_cells) < len(job_cells):
            # Tenemos que suponer el caso de que todavía queden celdas que añadir, que no se hayan añadido todas
            rest_cells = list(filter(lambda cell: cell not in prioritized_cells, job_cells))
            next_path = self.prioritize_cells(rest_cells)
            prioritized_cells.extend(next_path)

        return prioritized_cells

    def get_cells_accessible_from(self, closest_cell):
        list_accessible_cells = []
        for i in range(len(self.job_cells)):
            if closest_cell.is_accessible(self.job_cells[i]):
                list_accessible_cells.append(self.job_cells[i])
        if closest_cell.is_accessible(self.charging_point):
            list_accessible_cells.append(self.charging_point)
        return list_accessible_cells

    def get_closest_cell(self, job_cells, prioritized):
        cells = list(filter(lambda c: c not in prioritized, job_cells))

        if len(cells) == 0:
            return None

        closest_cell = cells[0]
        cp = self.charging_point
        min_distance = closest_cell.distance_to(cp)

        for i in range(1, len(cells)):
            cell_from = cells[i]

            if cell_from not in prioritized:
                distance = cell_from.distance_to(cp)

                if distance < min_distance:
                    min_distance = distance
                    closest_cell = cell_from
                elif distance == min_distance:
                    # check coordinates
                    # choose the one that has the same x position as charging point
                    if cp.get_x() == cell_from.get_x():
                        min_distance = distance
                        closest_cell = cell_from

        return closest_cell

    def get_closest_cell_simple(self, job_cells):
        closest_cell = job_cells[0]
        cp = self.charging_point
        min_distance = closest_cell.distance_to(cp)

        for i in range(1, len(job_cells)):
            cell_from = job_cells[i]
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
