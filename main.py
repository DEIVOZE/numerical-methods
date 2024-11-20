from flask import Flask, render_template, request, jsonify
import re

from task_solver import func_rect

app = Flask(__name__)

def process_formula(formula):
    # Убираем пробелы вокруг `**`
    formula = re.sub(r'\s*\*\*\s*', '**', formula)
    # Преобразуем Unicode-суперскрипты (например, x³ -> x ** 3)
    formula = formula.replace('²', '**2').replace('³', '**3')
    formula = re.sub(r'⁴', '**4', formula)
    formula = re.sub(r'⁵', '**5', formula)
    formula = re.sub(r'⁶', '**6', formula)
    formula = re.sub(r'⁷', '**7', formula)
    formula = re.sub(r'⁸', '**8', formula)
    formula = re.sub(r'⁹', '**9', formula)
    # Преобразуем x^3 в x ** 3
    formula = re.sub(r'\^(\d+)', r'**\1', formula)
    # Добавляем `*` между числом и переменной (например, 4x -> 4 * x)
    formula = re.sub(r'(\d)([a-zA-Z])', r'\1 * \2', formula)
    # Заменяем запятые на точки
    formula = formula.replace(',', '.')

    return formula

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    formula = data.get('formula', '')
    a = data.get('a', 0)
    b = data.get('b', 0)
    n = data.get('n', 0)
    processed_formula = process_formula(formula)
    g = func_rect(a, b, n, processed_formula)
    return render_template('result.html', ans=g)

if __name__ == '__main__':
    app.run(debug=True)
