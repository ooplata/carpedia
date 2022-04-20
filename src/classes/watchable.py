from abc import ABC, abstractmethod

class Watchable(ABC):
    def __init__(self, hasChanges = False):
        self.hasChanges = hasChanges

    @property
    def hasChanges(self):
        return self._hasChanges

    @hasChanges.setter
    def __hasChanges(self, value):
        self._hasChanges = value

    @abstractmethod
    def getChanges(self) -> object:
        ...

    @abstractmethod
    def acceptChanges(self):
        ...