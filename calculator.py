class Calculator:
    __expression: list
    __priority = ["/", "*", "+", "-"]

    def get_expression(self) -> list:
        return self.__expression
    def get_priority(self) -> list:
        return self.__priority

    def set_expression(self, value) -> None:
        self.__expression = value
    def set_priority(self, value) -> None:
        self.__priority = value

    def error(self):
        return ValueError('Informe uma expressão válida!')
    
    def result(self) -> float:
        numeric_expression = self.get_expression()
        priority = self.get_priority()
        total = float(numeric_expression[0])
        number_position = 2
        expression_position = 1
        
        for sinal in priority:
            while number_position < len(numeric_expression):
                element = numeric_expression[expression_position]
                try:
                    number_ant = float(numeric_expression[expression_position-1])
                    number_pos = float(numeric_expression[expression_position+1])
                except ValueError:
                    self.error()
                
                if sinal == element:
                    print("Solução: ", number_ant, element, number_pos)
                    if element == "+":
                        total = number_ant + number_pos
                    elif element == "-":
                        total = number_ant - number_pos
                    elif element == "/":
                        if element == 0:
                            self.error()
                        total = number_ant / number_pos
                    elif element == "*":
                        total = number_ant * number_pos
                    else:
                        self.error()
                    print("Resultado:", total, "\n")
                    print("numeric_expression: ", numeric_expression[expression_position])
                    numeric_expression.remove(expression_position)
                    numeric_expression.remove(expression_position)
                    numeric_expression.remove(expression_position)
                    numeric_expression.insert(expression_position-1, total)
                expression_position += 2
                number_position += 2
        total = numeric_expression[0]
        return total