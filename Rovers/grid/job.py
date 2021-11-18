from enum import Enum, auto


class JobState(Enum):
    FULFILLED = auto()
    STARTED = auto()
    NOTSTARTED = auto()


class Job:
    """

    """
    def __init__(self, state: JobState, job_cells):
        self.state = state
        self.job_cells = job_cells
        self.time_to_explore = 0

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
