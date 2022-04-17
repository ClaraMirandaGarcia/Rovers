import pykka

from grid.job import JobState
from rover1 import Rover, State1
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
        rover.set_state(State1.CHARGING_STATE)
        rover.battery = rover.battery_capacity
        rover.time_charging += rover.charging_time
        rover.write_file("BATTERY: " + str(rover.battery))

        if rover.get_battery() == rover.battery_capacity:
            rover.recharge = False
            # Si el trabajo no ha terminado->  TRANSLATE
            if rover.get_job().state != JobState.FULFILLED:
                rover.write_file("BATTERY: " + str(rover.battery))
                rover.set_state(State1.TRANSLATE_STATE)
            else:
                # Si el trabajo ha terminado -> IDLE
                rover.set_state(State1.IDLE_STATE)

        if len(self.queue.queue) > 0:
            self.charge()

