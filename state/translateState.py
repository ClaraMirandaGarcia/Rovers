from state.state import State
from grid.cell import Cell, CellState
from state.chargingState import ChargingState
import state.exploringState as s


class TranslateState(State):
    def explore(self, cell: Cell) -> None:
        if self.context.recharge:
            self.retreat(self)
        else:
            # necesita volver desde el punto de carga hasta la celda
            print("GOING BACk TO EXPLORING POINT")
            self.go_to_cell(self, cell)
            self.context.set_state(s.ExploringState)
            self.context.explore(cell)
        cell.set_state(CellState.EXPLORED)
        # gasto de batería:
        #   dado por el usuario

    def go_to_cell(self, cell):
        print("GOING BACK TO EXPLORE")
        cells = self.context.best_known_path

        # for cell in len(cells):

    def retreat(self):
        print("------------------------------RETREATING------------------------")
        cells = self.context.get_best_path()
        aux = len(cells) - 1

        while aux >= 0:
            cell = cells[aux]
            self.battery_discharge(self)
            if aux == 0:
                print("NEXT TO CHARGING POINT")
                print("IF CHARGING POINT FREE -> change state")
                # Set state -> Iddle
                self.context.set_state(ChargingState)
                self.context.explore(cell)
            aux = aux - 1

    def battery_discharge(self):
        new_battery = self.context.battery - self.context.min_bat
        self.context.set_battery(new_battery)
        pass
