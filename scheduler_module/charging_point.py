import pykka
import scheduler_module.state.chargingState as cs
from queue import PriorityQueue


class ChargingPoint(pykka.ThreadingActor):

    def __init__(self, rover_capacity, queue):

        self.rover_capacity = rover_capacity
        self.queue = PriorityQueue()
        if len(queue) > 0:
            self.queue = self.prioritize(queue)
            self.charge()
        super().__init__()

    @staticmethod
    def prioritize(queue):
        rovers = PriorityQueue()
        for rover in queue:
            rovers.put(rover.battery, rover)
        return rovers

    # new rover -> add rover -> prioritize by battery level
    def set_rover(self, rover):
        self.queue.put((rover.battery, rover))
        self.charge()

    # charge rover
    def charge(self):
        queue = self.queue.get()
        rover = queue[1]
        rover.write_file("\t\tAgent: Transitioning to Charging State")
        rover.set_state(cs.ChargingState("ChargingState"))

        rover.move(rover.cell)

        x = self.queue
        y = x.queue
        if len(y) > 0:
            self.charge()

