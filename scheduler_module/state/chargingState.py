import pykka

from scheduler_module.state.state import State
from scheduler_module.grid.cell import Cell


@pykka.traversable
class ChargingState(State):

    def add_time(self, cell_origin, cell_to):
        self.context.time_charging += self.context.charging_time * 60
        check_time = self.context.time_idle + self.context.time_translate + self.context.time_charging + self.context.time_exploring + self.context.charging_time
        if self.context.max_time is not None and check_time >= self.context.max_time:
            self.context.is_max_time = True
        else:
            self.context.total_time += self.context.charging_time

    def battery_discharge(self):
        pass

    def move(self, cell: Cell):
        rover = self.context
        rover.battery = rover.battery_capacity
        rover.time_charging += rover.charging_time
        rover.recharge = False
        self.context.write_file("\t\t"+"Battery recharged to : " + str(self.context.battery))


    def battery_charge(self, charge_speed=10):
        time_to_charge = self.context.charging_time
        # self.context.time_charging += time_to_charge

        new_battery = charge_speed + self.context.get_battery()
        if new_battery > self.context.battery_capacity:
            aux = self.context.battery_capacity - new_battery
            new_battery = new_battery + aux
        self.context.set_battery(new_battery)
