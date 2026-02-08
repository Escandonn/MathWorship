from controllers.calc_controller import CalcController

def run():
    controller = CalcController()

    expr = input("Ingrese la expresión matemática: ")
    result = controller.operate(expr)

    print("Resultado:", result)
