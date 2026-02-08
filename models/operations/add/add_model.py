from models.base_operation import BaseOperation

class AddOperation(BaseOperation):

    def execute(self, numbers: list[float]) -> float:
        return sum(numbers)
