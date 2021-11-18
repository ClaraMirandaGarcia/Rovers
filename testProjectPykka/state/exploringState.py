from state.state import State
from grid.cell import Cell, CellState
from state.translateState import TranslateState


class ExploringState(State):

    def move(self, cell: Cell) -> None:
        # check battery -> change state

        rover = self.context
        enough_battery = rover.battery_available()
        print("BATTERY AVAILABLE: " + str(rover.battery))

        self.context.time_exploring += 1

        if enough_battery:
            self.context.location = cell
            cell.set_state(CellState.EXPLORED)
            self.battery_discharge(self)
            # ahora mismo añadiremos todas las celdas que nos encontremos, ya que el espacio
            # modelado tiene forma de pasillo, solo hay una ruta de ida y vuelta.
            self.context.add_best_cell(cell)
        else:
            print("NOT ENOUGH BATTERY")
            print(self.context.get_battery())
            self.context.recharge = True
            self.context.set_state(TranslateState)
            self.context.move(cell)


    def battery_discharge(self):
        new_battery = self.context.battery - self.context.max_bat
        self.context.set_battery(new_battery)
        pass
