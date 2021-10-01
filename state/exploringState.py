from state.state import State
from grid.cell import Cell, CellState


class ExploringState(State):

    def explore(self, cell: Cell) -> None:
        cell.set_state(CellState.EXPLORED)
