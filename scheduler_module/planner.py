import pykka


class Planner(pykka.ThreadingActor):
    """
    The scheduler_module receives the agents and the jobs and assign them
    accordingly to its strategy
    Output: time spent in each mode
    """

    def __init__(self, queue, name_file, grid, max_time, jobs):
        super().__init__()
        self.__queue = queue
        self.__jobs = []
        self.__jobs = jobs
        path_to_file = "log_files\\" + name_file + "\\resume.txt"
        self.__path_to_file = "log_files\\" + name_file
        self.__grid = grid
        self.__max_time = max_time
        self.__if_finished = False

    def set_jobs(self, jobs):
        self.__jobs = jobs

    def get_jobs(self) -> []:
        return self.__jobs

    def schedule(self):
        aux = 0
        jobs = self.get_jobs()
        self._simple_strategy(jobs)

    def _simple_strategy(self, jobs):
        queue = self.__queue
        jobs_left = jobs.copy()
        r = None

        while len(jobs_left) > 0:
            for i in range(len(queue)):
                agent = queue[i]
                r = agent.proxy()
                position = len(jobs) - len(jobs_left)

                if position >= 0 and len(jobs_left) > 0:
                    j = jobs[len(jobs) - len(jobs_left)]
                    if j in jobs_left:
                        path_to_file = self.__path_to_file + "\\"
                        r.set_name_file(path_to_file + agent._actor.name_rover_file)
                        r.set_job(j)
                        jobs_left.remove(j)
                        r.write_file_opening()
                        r.simple_strategy()
                else:
                    break
            r.stop()
        self.__if_finished = True

    def on_receive(self, message):
        if message == "simple_strategy":
            self.schedule()
        elif message == "schedule":
            self.schedule()
            return "FINISHED"
        else:
            print('MESSAGE NOT MATCHED')
