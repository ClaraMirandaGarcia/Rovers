import pykka

from scheduler_module.errors_simulation import SimError
from scheduler_module.state.state import State
import scheduler_module.state.translateState as s
from scheduler_module.grid.cell import Cell


@pykka.traversable
class IdleState(State):

    def add_time(self, cell_origin, cell_to):
        pass

    def battery_discharge(self):
        pass

    def move(self, cell: Cell) -> None:
        self.context.time_idle += 1
        self.context.total_time += 1

        if not self.context.job.is_job_finished():
            if self.check_enough_battery():
                # cambiar a translate state
                self.context.set_state(s.TranslateState("TranslateState"))
                self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                self.context.move(cell)
            else:
                message = (
                        "The exploring operation could not be performed by the rover " + self.name_rover + " due to its "
                                                                                                           "battery "
                                                                                                           "capacity.")
                error = SimError("Battery Capacity", message)
                self.context.errors.append(error)
                self.context.write_file(error.get_message())
        else:
            self.context.set_occupied(False)

    def check_enough_battery(self):
        capacity = self.context.battery_capacity

        move_cost_trans = self.context.translate_bat
        move_cost_exp = self.context.exp_bat

        cost_move_path = len(self.context.best_known_path) * move_cost_trans
        total_cost = cost_move_path * 2

        if total_cost >= capacity:
            return False
        return True

