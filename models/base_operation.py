from abc import ABC, abstractmethod

class BaseOperation(ABC):

    @abstractmethod
    def execute(self, numbers: list[float]) -> float:
        pass
