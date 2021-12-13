from grid.job import Job
import pykka

from state.exploringState import ExploringState


class Planner(pykka.ThreadingActor):
    """
    The scheduler receives the agents and the jobs and assign them
    accordingly to its strategy

    Output: time spent in each mode
    """

    def __init__(self, queue, deploy_time):
        super().__init__()
        self.queue = queue
        self.deploy_time = deploy_time
        self.jobs = []

    def set_jobs(self, jobs):
        self.jobs = jobs

    def get_jobs(self) -> []:
        return self.jobs

    def schedule(self):
        print("scheduling")
        aux = 0
        jobs = self.get_jobs()
        print("scheduling2")
        self.simple_strategy2(jobs)
        '''
        print("scheduling3")
        for job in jobs:
            self.simple_strategy2(job, aux)
            aux += 1
        '''

    def simple_strategy2(self, jobs):
        rover_ref = self.queue[0]
        print(type(rover_ref))
        rover = rover_ref.proxy()
        counter = 0
        for job in jobs:
            rover.set_job(job)

            if not rover_ref.is_alive():
                print(type(rover_ref))
                actor = rover_ref._actor
                rover_ref = actor.start(battery=100, state=ExploringState, max_speed=1, min_speed=1,
                                        max_bat=10, min_bat=5, charging_time=1)
            rover_ref.tell("simple_strategy") # -> rises a problem
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
                      max_bat=10, min_bat=5, charging_time=1)

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
            # rover_ref = self.queue[aux2]
            # rover = rover_ref.proxy()
            # print("Time exploring:" + str(rover.time_exploring))
            # print("Time translate:" + str(rover.time_translate))
            # print("Time charging:" + str(rover.time_charging))
            # print("Time idle:" + str(rover.time_idle))

            aux2 += 1

    def on_receive(self, message):
        if message == "simple_strategy":
            self.schedule()
        else:
            print('MESSAGE NOT MATCHED')
