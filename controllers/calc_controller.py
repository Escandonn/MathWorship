from models.parser.expression_parser import ExpressionParser

class CalcController:

    def __init__(self):
        self.parser = ExpressionParser()

    def operate(self, expression: str):
        return self.parser.evaluate(expression)
