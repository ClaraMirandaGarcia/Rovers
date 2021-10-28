from state.state import State
from grid.cell import Cell
import state.translateState as s


class IddleState(State):

    def battery_discharge(self):
        pass

    def move(self, cell: Cell) -> None:
        # si el robot tiene un job asignado
        self.context.time_iddle +=1
        if self.context.is_occupied():
            # cambiar a translate state
            self.context.set_state(s.TranslateState)
            #
            self.context.move(cell)

        # si no está ocupado -> notificárselo al scheduler?

        pass
