from grid.job import Job
import pykka
from rover import Rover
from fileManagement import FileManager
from state.exploringState import ExploringState


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
        if len(self.queue) == 1:
            self.simple_strategy2(jobs)
        elif len(self.queue) == 2:
            self.simple_strategy3(jobs)
        '''
        print("scheduling3")
        for job in jobs:
            self.simple_strategy2(job, aux)
            aux += 1
        '''

    def simple_strategy3(self, jobs):
        r1 = Rover.start(battery=100, state=ExploringState, translate_speed=2.4, exp_speed=0.1,
                                  exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=self.grid, max_time=self.max_time,
                                  name_rover="rover1").proxy()
        j1 = jobs[0]
        r1.set_job(j1)
        r1.simple_strategy()
        r1.stop()

        r2 = Rover.start(battery=90, state=ExploringState, translate_speed=2.4, exp_speed=0.1,
                                  exp_bat=0.5, translate_bat=0.1, charging_time=1, grid=self.grid, max_time=self.max_time,
                                  name_rover="rover2").proxy()
        j2 = jobs[1]
        r2.set_job(j2)
        r2.simple_strategy()
        r2.stop()

    def simple_strategy33(self, jobs):

        for i in range(len(self.queue)):
            rover_ref = self.queue[i]
            print(type(rover_ref))
            rover = rover_ref.proxy()
            counter = 0
            job = jobs[i]
            rover.set_job(job)
            if not rover_ref.is_alive():
                actor = rover_ref._actor
                rover_ref = actor.start(battery=100, state=ExploringState, max_speed=1, min_speed=1,
                                        max_bat=10, min_bat=5, charging_time=1, max_time=100,
                                        name_rover="rover"+str(i))
            rover_ref.tell("simple_strategy")
            rover_ref.stop()

    def simple_strategy2(self, jobs):
        rover_ref = self.queue[0]
        print(type(rover_ref))
        rover = rover_ref.proxy()
        counter = 0
        for job in jobs:
            rover.set_job(job)

            if not rover_ref.is_alive():
                actor = rover_ref._actor
                rover_ref = actor.start(battery=100, state=ExploringState, max_speed=1, min_speed=1,
                                        max_bat=10, min_bat=5, charging_time=1, max_time=100,
                                        name_rover="rover1")

            rover_ref.tell("simple_strategy")
            counter += 1

        rover_ref.stop()

    '''
    Simple strategy modeling the jobs as "halls" and assigning each of them
    to an agent
    '''

    def simple_strategy(self, job: Job, aux_):
        aux = 0
        num_agent = len(self.queue)
        print("Exploring job: " + str(aux_))

        while aux < num_agent:
            '''Reference to the actor of the type pykka._ref.ActorRef'''
            rover_ref = self.queue[aux]
            if not rover_ref.is_alive():
                actor = rover_ref._actor
                rover_ref = actor.start(battery=100, state=ExploringState, max_speed=1, min_speed=1,
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
