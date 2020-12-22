from calculator import Calculator
from textwrap import dedent

calculator = Calculator()
expression = input("Digite uma expresão numérica: ")

print("Expressão Digitada: ", expression.strip(), "\n")
calculator.set_expression(expression.strip())

print("Total: ", calculator.result())