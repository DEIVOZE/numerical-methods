from flask import Flask, render_template, request, redirect, url_for
import re

from task_solver import func_rect

app = Flask(__name__)


# Обработка формулы
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


# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')


# Обработка формы и перенаправление
@app.route('/process', methods=['POST'])
def process():
    # Получение данных из формы
    formula = request.form.get('formula', '')
    a = request.form.get('a', 0, type=float)
    b = request.form.get('b', 0, type=float)
    n = request.form.get('n', 0, type=int)
    way = request.form.get('way', 0, type=int)

    # Обработка формулы
    processed_formula = process_formula(formula)

    # Перенаправление на страницу результатов с передачей данных
    return redirect(url_for('results', formula=processed_formula, a=a, b=b, n=n, way=way))


# Страница результатов
@app.route('/results')
def results():
    formula = request.args.get('formula', '')
    formula = formula.lower()
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    n = request.args.get('n', 0, type=int)
    way = request.args.get('way', 0, type=int)

    # Вычисление интеграла с использованием средней прямоугольной формулы
    ans = func_rect(a, b, n, formula, way)

    # Отображение результата на странице результатове
    return render_template('result.html', ans=ans)


if __name__ == '__main__':
    app.run(debug=True)
