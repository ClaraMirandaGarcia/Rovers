import pykka
from fileManagement import FileManager
from rover1 import State1
import time


class Planner(pykka.ThreadingActor):
    """
    The scheduler receives the agents and the jobs and assign them
    accordingly to its strategy

    Output: time spent in each mode
    """

    def __init__(self, queue, deploy_time, name_file, grid, max_time):
        super().__init__()
        self.queue = queue
        self.deploy_time = deploy_time
        self.jobs = []
        path_to_file = "log_files/" + name_file
        self.file_manager = FileManager(name_file, path_to_file)
        self.grid = grid
        self.max_time = max_time

    def set_jobs(self, jobs):
        self.jobs = jobs

    def get_jobs(self) -> []:
        return self.jobs

    def schedule(self):
        print("scheduling")
        aux = 0
        jobs = self.get_jobs()
        self.simple_strategy(jobs)
        print("HERE")
        time.sleep(15)
        print("HI")
        pykka.ActorRegistry.stop_all()

    def simple_strategy(self, jobs):
        queue = self.queue
        jobs_left = jobs.copy()

        while len(jobs_left) > 0:
            for i in range(len(queue)):
                agent = queue[i]
                r = agent.proxy()
                position = len(jobs) - len(jobs_left)

                if position >= 0:
                    j = jobs[len(jobs)-len(jobs_left)]
                    if j in jobs_left:
                        r.set_name_file("log_files/"+agent._actor.name_rover)
                        r.set_job(j)
                        jobs_left.remove(j)
                        r.write_file_opening()
                        r.simple_strategy()
                        # se para
                        r.set_state(State1.TRANSLATE_STATE)

                else:
                    break
            r.stop()
            print("__________-")

        pykka.ActorRegistry.stop_all()

    def on_receive(self, message):
        if message == "simple_strategy":
            self.schedule()
        else:
            print('MESSAGE NOT MATCHED')
