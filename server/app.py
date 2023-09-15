#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)  # This will print the string to the console
    return string  # This will display the string in the web browser


@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(i) for i in range(number + 1))
    return numbers


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'Result: {num1} {operation} {num2} = {result}'
    else:
        return 'Invalid operation'
if __name__ == '__main__':
    app.run(port=5555, debug=True)

