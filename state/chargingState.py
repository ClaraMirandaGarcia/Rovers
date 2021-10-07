from state.state import State
from grid.cell import Cell, CellState

class ChargingState(State):

    def explore(self, cell: Cell) -> None:
        print("CHARGING")
        self.battery_charge(self)
        if self.context.battery == 100:
            # Si tiene un trabajo/celda asignado -> Translate State
            print("CONTINUE TO EXPLORE")
            self.context.recharge = False
            # self.context.set_state(TranslateState)
            # Si no lo tiene asignado -> Iddle State

        pass

    # Tenemos el tiempo que tarda en cargarse el robot al 100 a partir de 0 i guess

    def battery_charge(self):
        new_battery = self.context.charging_time
        new_battery = 100
        self.context.set_battery(new_battery)
        pass


