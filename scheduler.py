from grid.job import Job


class Scheduler:
    '''
    Output: time spent in each mode
    '''
    def __init__(self, numAgents, areaToExplore, queue):
        self.numAgents = numAgents
        self.areaToExplore = areaToExplore
        self.queue = queue

    def schedule(self, jobs):
        print("scheduling")
        for job in jobs:
            self.simple_strategy(job)

        # Asignar la celda al robot -> que el robot la explore a menos
        #                              que se quede sin batería. Cuando 
        #                               la termine de explorar: modo Iddle

    def simple_strategy(self, job: Job):
        aux = 0
        num_agent = len(self.queue)

        while aux < num_agent:

            agent = self.queue[aux]
            aux += 1
            for cell in job.job_cells:
                agent.explore(cell)
                job.change_state()
