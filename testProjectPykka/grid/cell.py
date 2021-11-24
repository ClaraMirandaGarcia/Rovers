from enum import Enum, auto
from coordinates import Coordinate


class CellState(Enum):
    EXPLORED = auto()
    UNEXPLORED = auto()


class Cell:
    def __init__(self, state: CellState, size: int, accessible=True, coordinate=None):
        self.state = state
        self.size = size
        self.assigned = False
        self.accessible = accessible
        self.coordinate = coordinate

    def is_explored(self) -> bool:
        if self.state == CellState.EXPLORED:
            return True
        return False

    def set_state(self, state: CellState):
        self.state = state

    def get_cell_state(self) -> CellState:
        return self.state

    def set_assigned(self, assigned: bool):
        self.assigned = assigned

    def is_assigned(self) -> bool:
        return self.assigned

    def is_accessible(self) -> bool:
        return self.accessible

    def set_accessible(self, accessible):
        self.accessible = accessible

    def set_coordinate(self, coordinate):
        self.coordinate = coordinate

    def get_coordinate(self) -> Coordinate:
        return self.coordinate
