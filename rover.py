from state.state import State
from grid.cell import Cell


class Rover:
    def __init__(self, area, battery, state): #, speed, charging_point):

        self.battery = battery
        self.area = area
        #self.speed = speed
        #self.autonomyTime = autonomyTIme
        self.state = state

    def set_state(self, state: State):
        print(f"Agent: Transitioning to {type(state).__name__}")
        self.state.context = self

    def explore(self, cell: Cell):
        self.state.explore(self, cell)
        cell.set_state(cell.state.EXPLORED)

    def battery_available(self) -> bool:
        # if battery needed to return to charging point < battery left
        battery_spent = 100 - self.battery
        if battery_spent < self.battery:
            return True
        return False

    # Calcular la máxima distancia que se puede mover con la batería
    # actual, depende del estado en el que se encuentre.
    #def maxDistance:


