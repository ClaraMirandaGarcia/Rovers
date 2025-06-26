from enum import Enum, auto
from coordinates import Coordinate
import numpy as np


class CellState(Enum):
    EXPLORED = auto()
    UNEXPLORED = auto()


class Cell:
    def __init__(self, state: CellState, size: int, real_size: int, accessible=False, coordinate=Coordinate):
        self.state = state
        self.size = size
        self.real_size = real_size
        self.assigned = False
        self.accessible = accessible
        self.coordinate = coordinate
        self.charging_point = False
        self.charging_point_actor = None
        self.rover_name = None

    def set_real_size(self, real_size):
        self.real_size = real_size

    def set_charging_point(self, charging_point_boolean, charging_point_actor):
        self.charging_point = charging_point_boolean
        self.charging_point_actor = charging_point_actor

    def is_charging_point(self):
        return self.charging_point

    @staticmethod
    def get_closest_accessible_cell(from_cell, path, goal_cell):
        '''
        Gets the cell to move to from a certain cell within a path that allows to reach a goal_cell
        '''
        cells = list(filter(lambda c: c.is_accessible(from_cell), path))
        min_distance = from_cell.distance_to(goal_cell)
        cell_to = from_cell

        for cell in cells:
            dis_aux = cell.distance_to(goal_cell)
            if dis_aux <= min_distance:
                cell_to = cell
                min_distance = dis_aux

        if cell_to == from_cell:
            if from_cell in path:
                index_cell = path.index(from_cell)

                if goal_cell.is_accessible(from_cell):
                    cell_to = goal_cell
                elif len(cells) == 1 and cells[0].is_accessible(cell_to):
                    cell_to = cells[0]
                elif len(cells) > 1 and index_cell is not None:
                    cell_to = path[index_cell - 1]

        return cell_to

    def is_accessible(self, from_cell) -> bool:
        '''
        Returns whether the passed cell is accessible from this cell
        '''
        from_cell_x = from_cell.get_x()
        from_cell_y = from_cell.get_y()
        current_cell_x = self.get_x()
        current_cell_y = self.get_y()

        condition1 = ((from_cell_x == current_cell_x) and (from_cell_y == current_cell_y + 1)) or (
                (from_cell_x == current_cell_x) and (from_cell_y == current_cell_y - 1)
        )

        condition2 = ((from_cell_y == current_cell_y) and (from_cell_x == current_cell_x + 1)) or (
                (from_cell_y == current_cell_y) and (from_cell_x == current_cell_x - 1)
        )

        condition = condition1 or condition2

        if condition:
            return True
        return False

    def distance_to(self, cell_to):
        '''
        Returns the distance from this cell to another.
        '''
        dx = (self.get_x() - cell_to.get_x()) ** 2
        dy = (self.get_y() - cell_to.get_y()) ** 2
        distance = np.sqrt(dx + dy)
        return distance

    def set_state(self, state: CellState, name_rover):
        self.state = state
        self.set_rover_explored(name_rover)

    def get_cell_state(self) -> CellState:
        return self.state

    def is_cell_explored(self):
        if self.state == CellState.EXPLORED:
            return True
        return False

    def set_rover_explored(self, rover_name):
        self.rover_name = rover_name

    def rover_explored(self):
        return self.rover_name

    def set_assigned(self, assigned: bool):
        self.assigned = assigned

    def is_assigned(self) -> bool:
        return self.assigned

    def set_accessible(self, accessible):
        self.accessible = accessible

    def set_coordinate(self, coordinate):
        self.coordinate = coordinate

    def get_coordinate(self) -> Coordinate:
        return self.coordinate

    def get_x(self):
        return self.get_coordinate().x

    def get_y(self):
        return self.get_coordinate().y
