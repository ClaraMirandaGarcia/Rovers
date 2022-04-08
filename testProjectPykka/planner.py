from grid.job import Job
import pykka
from rover1 import State1 as state
from rover1 import Rover as Rover1
from fileManagement import FileManager


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

    def simple_strategy(self, jobs):
        queue = self.queue
        aux_jobs = jobs
        jobs_left = jobs.copy()

        while len(jobs_left) > 0:
            for i in range(len(queue)):
                agent = queue[i]
                r = agent.proxy()
                j = jobs[i]
                r.set_name_file("log_files/"+agent._actor.name_rover)
                r.set_job(j)
                jobs_left.remove(j)
                r.write_file_opening()
                r.simple_strategy()
                r.stop()
                agent.stop()

        # Cosas que pueden pasar -> más trabajos que rovers
        #                        -> más rovers que trabajos

    '''
    Simple strategy modeling the jobs as "halls" and assigning each of them
    to an agent
    '''

    def simple_strategy_version1(self, job: Job, aux_):
        aux = 0
        num_agent = len(self.queue)
        print("Exploring job: " + str(aux_))

        while aux < num_agent:
            '''Reference to the actor of the type pykka._ref.ActorRef'''
            rover_ref = self.queue[aux]
            if not rover_ref.is_alive():
                actor = rover_ref._actor
                rover_ref = actor.start(battery=100, state=state.EXPLORING_STATE, max_speed=1, min_speed=1,
                      max_bat=10, min_bat=5, charging_time=1, max_time=100, name_rover="rover1")

            try:
                '''Wrapping the reference to represent the rover'''
                rover = rover_ref.proxy()
            except pykka.ActorDeadError:
                print("ActorDeadError")

            '''Setting the job to explore'''
            rover.set_job(job)
            '''Sending the message to perform a simple strategy with the rover'''
            rover_ref.tell("simple_strategy")
            rover_ref.stop()
            aux += 1

        aux2 = 0
        while aux2 < num_agent:
            rover_ref = self.queue[aux2]
            rover = rover_ref.proxy()


            aux2 += 1

    def on_receive(self, message):
        if message == "simple_strategy":
            self.schedule()
        else:
            print('MESSAGE NOT MATCHED')
