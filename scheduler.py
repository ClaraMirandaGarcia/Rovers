from grid.job import Job


class Scheduler:
    '''
    Output: time spent in each mode
    '''
    def __init__(self, numAgents, queue):
        self.numAgents = numAgents
        self.queue = queue

    def schedule(self, jobs):
        print("scheduling")
        aux = 0
        for job in jobs:
            self.simple_strategy(job, aux)
            aux += 1

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
            print("Time iddle:" + str(agent.time_iddle))

            aux2 += 1
