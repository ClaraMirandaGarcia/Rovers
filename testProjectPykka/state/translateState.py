from state.state import State
from grid.cell import Cell, CellState
from state.chargingState import ChargingState
import state.exploringState as s


class TranslateState(State):
    def move(self, cell: Cell) -> None:
        self.context.time_translate += 1

        if self.context.recharge:

            if cell.is_charging_point():
                self.to_charge(self, cell)

            else:
                path = self.context.best_known_path
                print(path)
                self.retreat(self, cell, path)
        else:
            # necesita volver desde el punto de carga hasta la celda
            print("GOING BACK TO EXPLORING POINT")
            #self.go_to_cell(self, cell)
            goal_cell = self.context.job.get_first_cell()

            if cell == goal_cell:
                # it has reached the point to explore
                self.context.set_state(s.ExploringState)
                self.context.move(cell)

            else:
                # avanzar desde la posición actual por el best_known_path hasta goal_cell
                path = self.context.best_known_path
                # find current position in best_known_path, advance one more
                current_index = path.index(cell)
                cell = path[current_index-1]
                print("KKKKKKKKKKKKLKLK", cell.get_coordinate())
                self.context.move(cell)
        cell.set_state(CellState.EXPLORED)
        # gasto de batería:
        #   dado por el usuario

    #def go_to_cell(self, cell):
     #   print("GOING BACK TO EXPLORE")
      #  cells = self.context.best_known_path

        # for cell in len(cells):
    def to_charge(self, cell):

        print("NEXT TO CHARGING POINT")
        print(cell.get_coordinate())
        print("IF CHARGING POINT FREE -> change state")
        # Set state -> Idle
        self.context.set_state(ChargingState)
        self.context.move(cell)

    def retreat(self, cell,  best_known_path):
        print("------------------------------RETREATING------------------------")
        print("AAAAAAA")
        print(cell.get_coordinate())
        cells = best_known_path
        cell = cells[len(best_known_path)-1]
        print(cell.get_coordinate())
        self.battery_discharge(self)
        self.context.move(cell)

    def battery_discharge(self):
        new_battery = self.context.battery - self.context.translate_bat
        self.context.set_battery(new_battery)
        pass
