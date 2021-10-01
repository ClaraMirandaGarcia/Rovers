from abc import ABC, abstractmethod



class State(ABC):

    #Protected parameter
    #@property
    #def context(self) -> rover:
    #    return self._context

    @abstractmethod
    def explore(self, cell):
        pass
