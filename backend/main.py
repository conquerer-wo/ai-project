from flask import Flask, request, jsonify
from sympy import symbols, sympify, lambdify
import numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow CORS from both your GitHub Pages origin and localhost dev
CORS(app, resources={
    r"/*": {
        "origins": [
            "https://conquerer-wo.github.io",
            "http://127.0.0.1:5500"
        ],
        "methods": ["POST", "OPTIONS"]
    }
})

@app.route('/left_sum', methods=['POST'])
def left_sum():
    data = request.get_json()
    x = symbols('x')
    expr = sympify(data['expr'])
    f = lambdify(x, expr, modules='numpy')
    a = float(data['a'])
    b = float(data['b'])
    n = int(data.get('n', 100))
    delta_x = (b - a) / n
    total = sum(delta_x * f(a + i * delta_x) for i in range(n))
    return jsonify({"approx": total})

@app.route('/right_sum', methods=['POST'])
def right_sum():
    data = request.get_json()
    x = symbols('x')
    expr = sympify(data['expr'])
    f = lambdify(x, expr, modules='numpy')
    a = float(data['a'])
    b = float(data['b'])
    n = int(data.get('n', 100))
    delta_x = (b - a) / n
    total = sum(delta_x * f(a + (i + 1) * delta_x) for i in range(n))
    return jsonify({"approx": total})

@app.route('/center_sum', methods=['POST'])
def center_sum():
    data = request.get_json()
    x = symbols('x')
    expr = sympify(data['expr'])
    f = lambdify(x, expr, modules='numpy')
    a = float(data['a'])
    b = float(data['b'])
    n = int(data.get('n', 100))
    delta_x = (b - a) / n
    total = sum(delta_x * f(a + (i + 0.5) * delta_x) for i in range(n))
    return jsonify({"approx": total})

@app.route('/trap_sum', methods=['POST'])
def trap_sum():
    data = request.get_json()
    x = symbols('x')
    expr = sympify(data['expr'])
    f = lambdify(x, expr, modules='numpy')
    a = float(data['a'])
    b = float(data['b'])
    n = int(data.get('n', 100))
    delta_x = (b - a) / n
    total = sum(
        (delta_x / 2) *
        (1 if i == 0 or i == n - 1 else 2) *
        f(a + i * delta_x)
        for i in range(n)
    )
    return jsonify({"approx": total})

if __name__ == "__main__":
    # Use the PORT env var provided by Render, defaulting to 5000
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so Render’s router can reach it, and keep debug on for now
    app.run(host="0.0.0.0", port=port, debug=True)
