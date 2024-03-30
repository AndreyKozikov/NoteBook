from abc import ABC, abstractmethod

class ExecuteOperation(ABC):
    @abstractmethod
    def execute(self, notes,  callback):
        pass
