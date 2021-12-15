from state.state import State
from grid.cell import Cell
import state.translateState as s


class IdleState(State):

    def battery_discharge(self):
        pass

    def move(self, cell: Cell) -> None:
        # si el robot tiene un job asignado
        self.context.time_idle +=1
        if not self.context.job.is_job_finished():
            # cambiar a translate state
            self.context.set_state(s.TranslateState)
            self.context.move(cell)
        else:
            self.context.set_occupied(False)

        # si no está ocupado -> notificárselo al scheduler?

        pass
