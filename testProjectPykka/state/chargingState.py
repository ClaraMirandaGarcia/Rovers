from state.state import State
from grid.cell import Cell
from state.idleState import IdleState


class ChargingState(State):

    def add_time(self, cell_origin, cell_to):
        self.context.time_charging += self.context.charging_time

    def battery_discharge(self):
        pass

    def move(self, cell: Cell):

        battery_aux = self.context.get_battery()
        while battery_aux != 100:
            self.battery_charge(self)
            battery_aux = self.context.get_battery()

            if battery_aux == 100:
                self.context.recharge = False
                self.add_time(self, cell, cell)
                self.context.set_state(IdleState)
                self.context.move(cell)

    def battery_charge(self, charge_speed=10):
        time_to_charge = self.context.charging_time
        self.context.time_charging += time_to_charge

        new_battery = charge_speed + self.context.get_battery()
        if new_battery > 100:
            aux = 100 - new_battery
            new_battery = new_battery + aux
        self.context.set_battery(new_battery)
