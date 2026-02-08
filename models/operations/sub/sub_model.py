from functools import reduce
from models.base_operation import BaseOperation

class SubOperation(BaseOperation):

    def execute(self, numbers: list[float]) -> float:
        return reduce(lambda x, y: x - y, numbers)
