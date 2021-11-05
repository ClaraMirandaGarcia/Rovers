from grid.job import Job


class Scheduler:
    """
    The scheduler receives the agents and the jobs and assign them
    accordingly to its strategy

    Output: time spent in each mode
    """
    def __init__(self, queue):
        self.queue = queue

    def schedule(self, jobs):
        print("scheduling")
        aux = 0
        for job in jobs:
            self.simple_strategy(job, aux)
            aux += 1

    '''
    Simple strategy modeling the jobs as "halls" and assigning each of them
    to an agent
    '''
    def simple_strategy(self, job: Job, aux_):
        aux = 0
        num_agent = len(self.queue)
        print("Exploring job: " + str(aux_))

        while aux < num_agent:
            agent = self.queue[aux]
            agent.set_job(job)
            agent.simple_strategy()
            aux += 1
        aux2 = 0

        while aux2 < num_agent:
            agent = self.queue[aux2]
            print("Time exploring:" + str(agent.time_exploring))
            print("Time translate:" + str(agent.time_translate))
            print("Time charging:" + str(agent.time_charging))
            print("Time idle:" + str(agent.time_idle))

            aux2 += 1
