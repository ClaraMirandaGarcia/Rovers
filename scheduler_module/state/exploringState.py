from scheduler_module.state.state import State
from scheduler_module.grid.cell import Cell, CellState
import scheduler_module.state.translateState as ts
import numpy as np
import pykka


@pykka.traversable
class ExploringState(State):

    def add_time(self, cell_from, cell_to):
        distance = cell_from.distance_to(cell_to) * np.sqrt(cell_from.size)
        time = distance / self.context.exp_speed
        check_time = self.context.time_idle + self.context.time_translate + self.context.time_charging + self.context.time_exploring + time

        if self.context.max_time is not None and check_time >= self.context.max_time:
            self.context.is_max_time = True
        else:
            self.context.total_time += time
            self.context.time_exploring += time


    def add_explored_exploring(self, cell_from):
        self.context.area_explored += cell_from.real_size


    def move(self, cell: Cell) -> None:
        if self.context.location.is_cell_explored() and self.context.location.is_charging_point() and cell.get_coordinate() == self.context.location.get_coordinate():
            self.context.write_file("\t\tThe rover is currently in the charging point cell")
            self.context.write_file("\t\t"+"Location: " + str(self.context.location.get_coordinate()))
            self.context.add_movement_log(str(self.context.location.get_coordinate()))
            if self.context.location.get_coordinate() == cell.get_coordinate():
                pass
        else:

            unexplored_accessible_cells = self.context.check_cells()
            old_location = self.context.location
            cells = self.context.get_unexplored()

            if unexplored_accessible_cells and self.context.location != cell:
                c0 = cells[0]
                if cells[0].is_accessible(self.context.location) and cell.get_coordinate() == c0.get_coordinate():
                    # it is moved without battery checking ?
                    self.context.location = cells[0]
                    self.add_time(self.context.location, c0)

                elif cell.is_accessible(self.context.location):
                    self.add_time(self.context.location, cell)
                    self.context.location = cell
                else:
                    # Is not accessible -> you have to move
                    self.context.set_state(ts.TranslateState("TranslateState"))
                    self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                    self.context.move(cell)
                    # Es necesario?
                    if cell.is_accessible(self.context.location):
                        self.add_time(self.context.location, cell)
                        self.context.location = cell

            elif not unexplored_accessible_cells and self.context.location.is_cell_explored() and not self.context.job.job_fulfilled() and cell.get_coordinate() != self.context.location.get_coordinate():

                self.context.write_file("\t\tThere are no accessible unexplored cells")
                self.context.set_state(ts.TranslateState("TranslateState"))
                self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
                self.context.write_file("\t\tLocation: " + str(self.context.location.get_coordinate()))
                self.context.add_movement_log(str(self.context.location.get_coordinate()))
                self.context.move(cell)
            else:
                if cell.is_accessible(self.context.location):
                    self.context.location = cell

            if not self.context.location.is_cell_explored():
                rover = self.context
                self.context.write_file("\t\t"+"Location: "+ str(self.context.location.get_coordinate()))
                self.context.add_movement_log(str(self.context.location.get_coordinate()))

                enough_battery = rover.battery_available()
                self.context.write_file("\t\t"+"Battery: " + str(self.context.battery))

                self.add_time(self.context.location, old_location)
                self.manage_battery(cell, enough_battery)

    def manage_battery(self, cell, enough_battery):
        if enough_battery:
            self.context.location.set_state(CellState.EXPLORED, self.context.name_rover_file)
            self.battery_discharge()
            self.add_explored_exploring(self.context.location)
            self.context.add_best_cell(cell)
        else:
            self.context.recharge = True
            self.context.set_state(ts.TranslateState("TranslateState"))
            self.context.write_file("\t\t" + "Agent: Transitioning to " + str(self.context.state.__name__))
            self.context.write_file("\t\t" + "There is no enough battery to continue exploring")
            self.context.write_file("\t\t" + "Retreating to Charging Point")
            self.context.add_best_cell(cell)
            self.context.move(cell)

    def battery_discharge(self):
        new_battery = self.context.battery - self.context.exp_bat
        self.context.set_battery(new_battery)
        pass

