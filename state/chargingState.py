from state.state import State
from grid.cell import Cell
from state.iddleState import IddleState


class ChargingState(State):

    def explore(self, cell: Cell) -> None:
        print("CHARGING")

        battery_aux = self.context.get_battery()

        while battery_aux != 100:
            self.battery_charge(self)
            battery_aux = self.context.get_battery()
            if battery_aux == 100:
                # Si tiene un trabajo/celda asignado -> Translate State
                print("CONTINUE TO EXPLORE")
                self.context.recharge = False
                self.context.set_state(IddleState)
                self.context.explore(cell)
                # Si no lo tiene asignado -> Iddle State

        pass

    # Tenemos el tiempo que tarda en cargarse el robot al 100 a partir de 0 i guess

    def battery_charge(self):
        time_to_charge = self.context.charging_time
        new_battery = 10 + self.context.battery
        self.context.set_battery(new_battery)
        print("NEW BATTERY "+str(self.context.battery))
        pass


