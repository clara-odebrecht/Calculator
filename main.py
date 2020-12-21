from calculator import Calculator

expression = input("Digite uma expresão: ")

calculator = Calculator()

print("Expressão: ", expression.strip(), "\n")
calculator.set_expression(expression.strip())

print("Total: ", calculator.result())