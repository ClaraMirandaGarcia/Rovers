from state.state import State
from grid.cell import Cell, CellState
from state.translateState import TranslateState


class ExploringState(State):

    def move(self, cell: Cell) -> None:
        # check if there are accessible unexplored cells, if not -> Translate state + move(cell)

        unexplored_accessible_cells = self.context.check_cells()

        if unexplored_accessible_cells:
            self.context.location = cell
        else:
            print("There are no accessible unexplored cells")
            self.context.set_state(TranslateState)
            self.context.move(cell)

        
        # in translate state -> check the same, if there are accessible unexplored cells
        self.context.location = cell
        # check battery -> change state

        rover = self.context
        #print("LOCATION: ", rover.location.coordinate)
        print("LOCATION: ", cell.coordinate)

        enough_battery = rover.battery_available()
        print("BATTERY AVAILABLE: " + str(rover.battery))

        self.context.time_exploring += 1

        if enough_battery:
            # self.context.location = cell
            cell.set_state(CellState.EXPLORED)
            self.battery_discharge(self)
            # se tiene en cuenta si hay otro posible path que tiene menor distancia
            self.context.add_best_cell(cell)
        else:
            self.context.recharge = True
            self.context.set_state(TranslateState)
            self.context.add_best_cell(cell)
            self.context.move(cell)

    def battery_discharge(self):
        new_battery = self.context.battery - self.context.exp_bat
        self.context.set_battery(new_battery)
        pass
