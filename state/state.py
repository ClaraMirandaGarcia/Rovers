from __future__ import annotations
from abc import ABC, abstractmethod
from rover import Rover


class State(ABC):

    #@property
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
