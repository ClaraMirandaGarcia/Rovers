from state.state import State
from grid.cell import Cell, CellState
from state.translateState import TranslateState
import numpy as np


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

    def add_explored(self, cell_from):
        self.context.area_explored += cell_from.real_size

    def move(self, cell: Cell) -> None:
        unexplored_accessible_cells = self.context.check_cells()
        old_location = self.context.location
        cells = self.context.get_unexplored()

        if unexplored_accessible_cells and self.context.location != cell:
            c0 = cells[0]
            if cells[0].is_accessible(self.context.location) and cell.get_coordinate() == c0.get_coordinate():
                self.context.location = cells[0]
                self.add_time(self, self.context.location, c0)
                self.context.write_file("\n" + "FINISHED" + "\n")
            elif cell.is_accessible(self.context.location):
                self.add_time(self, self.context.location, cell)
                self.context.location = cell
            else:
                # Is not accessible -> you have to move
                self.context.set_state(TranslateState)
                self.context.move(cell)
                # Es necesario?
                if cell.is_accessible(self.context.location):
                    self.add_time(self, self.context.location, cell)
                    self.context.location = cell
        elif not unexplored_accessible_cells and self.context.location.is_explored() and not self.context.job.job_fulfilled:
            # No hay celdas inexploradas y ya se ha explorado la localización
            # Mirar si el trabajo ya está finalizado o no
            self.context.write_file("There are no accessible unexplored cells"+"\n")
            self.context.set_state(TranslateState)
            self.context.write_file("Location " + str(self.context.location.get_coordinate())+"\n")
            self.context.move(cell)
            self.context.write_file("Location after moving" + str(self.context.location.get_coordinate()) + "\n")
            self.context.location = cell
        else:
            self.context.location = cell
        rover = self.context
        self.context.write_file("LOCATION: " + str(rover.location.get_coordinate()))
        enough_battery = rover.battery_available()
        self.context.write_file("BATTERY AVAILABLE: " + str(rover.battery))
        self.context.time_exploring += 1

        self.add_time(self, self.context.location, old_location)
        self.manage_battery(self, cell, enough_battery)

    def manage_battery(self, cell, enough_battery):
        if enough_battery:
            self.context.location.set_state(CellState.EXPLORED)
            self.battery_discharge(self)
            self.add_explored(self, self.context.location)
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
