from state.state import State
from grid.cell import Cell, CellState


class IddleState(State):

    def explore(self, cell: Cell) -> None:
        pass
