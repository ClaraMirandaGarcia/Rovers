from __future__ import annotations
from abc import ABC, abstractmethod
from rover import Rover

"""
    Represents the state of the rover
"""


class State(ABC):

    @abstractmethod
    def add_time(self, cell_origin, cell_to):
        pass

    def context(self) -> Rover:
        return self.context

    def set_context(self, context: Rover):
        self.context = context

    @abstractmethod
    def move(self, cell):
        pass

    @abstractmethod
    def battery_discharge(self):
        pass
