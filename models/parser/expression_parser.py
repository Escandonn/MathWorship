from models.operations.add.add_model import AddOperation
from models.operations.sub.sub_model import SubOperation
from models.operations.mul.mul_model import MulOperation
from models.operations.div.div_model import DivOperation


class ExpressionParser:

    def __init__(self):
        self.ops = {
            '+': AddOperation(),
            '-': SubOperation(),
            '*': MulOperation(),
            '/': DivOperation(),
        }
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }

    def to_postfix(self, expression: str):
        stack = []
        output = []

        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

        for token in tokens:
            if token.isnumeric():
                output.append(float(token))

            elif token in self.ops:
                while (stack and stack[-1] != '(' and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)

            elif token == '(':
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())

        return output

    def evaluate_postfix(self, postfix):
        stack = []

        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                result = self.ops[token].execute([a, b])
                stack.append(result)

        return stack[0]

    def evaluate(self, expression: str):
        postfix = self.to_postfix(expression)
        return self.evaluate_postfix(postfix)
