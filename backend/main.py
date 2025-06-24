from flask import Flask,request, jsonify
from sympy import symbols, sympify, lambdify
import numpy as np
from flask_cors import CORS
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": "http://127.0.0.1:5500",
        "methods": ["POST", "OPTIONS"]
    }
})


@app.route('/left_sum', methods=['POST'])
def left_sum():
    data = request.get_json()
    x = symbols('x')                      # define variable
    expr_str = data['expr']                  # get expression string from request
    expr = sympify(expr_str)                 # convert string to sympy expression
    f = lambdify(x, expr, modules='numpy') 
    a        = float(data['a'])
    b        = float(data['b'])
    n        = int(data.get('n', 100))
    delta_x = (b-a)/n
    sums = []
    for i in range(n):
        sums.append(delta_x * f(a + i * delta_x))
    return jsonify({"approx": sum(sums)})
@app.route('/right_sum', methods=['POST'])
def right_sum():
    data = request.get_json()
    x = symbols('x')                      # define variable
    expr_str = data['expr']                  # get expression string from request
    expr = sympify(expr_str)                 # convert string to sympy expression
    f = lambdify(x, expr, modules='numpy') 
    a        = float(data['a'])
    b        = float(data['b'])
    n        = int(data.get('n', 100))
    delta_x = (b-a)/n
    sums = []
    for i in range(n):
        sums.append(delta_x * f(a + (i + 1) * delta_x))
    return jsonify({"approx": sum(sums)})
@app.route('/center_sum', methods=['POST'])
def center_sum():
    data = request.get_json()
    x = symbols('x')                      # define variable
    expr_str = data['expr']                  # get expression string from request
    expr = sympify(expr_str)                 # convert string to sympy expression
    f = lambdify(x, expr, modules='numpy') 
    a        = float(data['a'])
    b        = float(data['b'])
    n        = int(data.get('n', 100))
    delta_x = (b-a)/n
    sums = []
    for i in range(n):
        sums.append(delta_x * f(a + (i+ 0.5) * delta_x))
    return jsonify({"approx": sum(sums)})
@app.route('/trap_sum', methods=['POST'])
def trap_sum():
    data = request.get_json()
    x = symbols('x')                      # define variable
    expr_str = data['expr']                  # get expression string from request
    expr = sympify(expr_str)                 # convert string to sympy expression
    f = lambdify(x, expr, modules='numpy') 
    a        = float(data['a'])
    b        = float(data['b'])
    n        = int(data.get('n', 100))
    delta_x = (b-a)/n
    sums = []
    for i in range(n):
        sums.append((delta_x/2) *(1 if i == 0 or i == n -1 else 2) * f(a + i * delta_x))
    return jsonify({"approx": sum(sums)})


if __name__ == "__main__":
    app.run(debug = True)