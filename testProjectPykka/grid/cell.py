from enum import Enum, auto
from coordinates import Coordinate
import numpy as np

class CellState(Enum):
    EXPLORED = auto()
    UNEXPLORED = auto()


class Cell:
    def __init__(self, state: CellState, size: int, accessible=False, coordinate=Coordinate):
        self.state = state
        self.size = size
        self.assigned = False
        self.accessible = accessible
        self.coordinate = coordinate
        self.charging_point = False

    def is_explored(self) -> bool:
        if self.state == CellState.EXPLORED:
            return True
        return False

    def set_charging_point(self, charging_point):
        self.charging_point = charging_point

    def is_charging_point(self):
        return self.charging_point

    def is_accessible(self, from_cell) -> bool:
        # Se dice que es accesible si pertenece al mismo trabajo
        # Una celda es accesible desde otra si es colindante a la misma
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
        dx = (self.get_x() - cell_to.get_x()) ** 2
        dy = (self.get_y() - cell_to.get_y()) ** 2
        distance = np.sqrt(dx+dy)
        return distance

    def set_state(self, state: CellState):
        self.state = state

    def get_cell_state(self) -> CellState:
        return self.state

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
