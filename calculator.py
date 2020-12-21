class Calculator:
    expression: list

    def get_expression(self) -> list:
        return self.expression
    def set_expression(self, value) -> None:
        self.expression = value

    def result(self) -> float:
        numeric_expression = self.get_expression()
        total = float(numeric_expression[0])
        number_position = 2
        expression_position = 1
        
        while number_position < len(numeric_expression):
            element = numeric_expression[expression_position]
            number = float(numeric_expression[number_position])

            if isinstance(number, float):
                return ValueError('Informe uma expressão válida!')
            print(total, element, number)
            if element == "+":
                total = total + number
            elif element == "-":
                total = total - number
            elif element == "/":
                total = total / number
            elif element == "*":
                total = total * number
            else:
                print("Digite uma expressão válida!")
            print("Resultado:", total, "\n")
            expression_position += 2
            number_position += 2
        return total