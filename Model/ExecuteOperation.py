from abc import ABC, abstractmethod

class ExecuteOperation(ABC):
    @abstractmethod
    def execute(self, *args):
        pass
