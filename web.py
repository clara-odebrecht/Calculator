# pip3 install flask
# which python3

# Flask tem que estar dentro da pasta do python, se nao
# ele n reconhece

from flask import Flask
from calculator import Calculator

# __name__ pega o nome atual do arquivo
app = Flask(__name__) # classe construtora

@app.route('/')
def index():
    expression = '3+9-4/8*1'.strip()
    calculator = Calculator()
    calculator.set_expression(expression)
    results = calculator.result()
    title = '<h1> Calculadora </h1>'
    calcultate = f'''
            <input value="{expression}" />
            <h3>Resultado: {results}</h3>
            <h4><a href="/">Voltar</a></h4>
        '''
    return f'{title} {calcultate}'

app.run()