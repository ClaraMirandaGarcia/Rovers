from enum import Enum, auto


class CellState(Enum):
    EXPLORED = auto()
    UNEXPLORED = auto()


class Cell:
    def __init__(self, state: CellState, size: int):
        self.state = state
        self.size = size
        self.assigned = False

    def is_explored(self) -> bool:
        if self.state.EXPLORED:
            return True
        return False

    def set_state(self, state: CellState):
        self.state = state

    def set_assigned(self, assigned: bool):
        self.assigned = assigned

    def is_assigned(self) -> bool:
        return self.assigned
