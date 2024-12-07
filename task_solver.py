def func_rect(a, b, n, func, way):
    h = round((b - a) / n, 5)
    half_h = h / 2
    xi = {}
    func_x = {}
    other = {}
    if way == 0:
        other['h'] = f'({b} - {a})/{n} = {h}'
        ci = {}
        func_c = {}
        for i in range(n * 2 + 1):
            x = round(a + half_h * i, 5)
            if i % 2 == 0:
                xi[f'x{i // 2}'] = x
                func_x[f'f(x{i // 2})'] = round(eval(func), 5)
            else:
                ci[f'c{i // 2 + 1}'] = x
                func_c[f'f(c{i // 2 + 1})'] = round(eval(func), 5)

        ans = round(h * sum(func_c.values()), 5)
        other['ans'] = ans
        other['text_ans'] = f'{h} * ({" + ".join(map(str, func_c.values()))}) = {h} * {sum(func_c.values())} = {ans}'
        return xi, ci, func_c, other

    if way == 1:
        other['h'] = f'({b} - {a})/{n} = {h}'
        for i in range(n + 1):
            x = round(a + i * h, 5)
            xi[f'x{i}'] = x
            func_x[f'f({i})'] = round(eval(func), 5)
        y = list(func_x.values())
        ans = round(h * ((y[0] + y[-1]) / 2 + sum(y[1:-1])), 5)
        text_ans = f'{h} * (({y[0]} + {y[-1]})/2 + ({" + ".join(map(str, y[1:-1]))}) = {h} * ({(y[0] + y[-1]) / 2} + {sum(y[1:-1])}) = {ans}'
    else:
        other['h'] = f'({b} - {a})/{2 * n} = {h}'
        for i in range(2 * n + 1):
            x = round(a + i * half_h, 5)
            xi[f'x{i}'] = x
            func_x[f'f({i})'] = round(eval(func), 5)
        y = list(func_x.values())
        ans = round((b - a) / (6 * n) * ((y[0] + y[-1]) + 4 * (sum(y[1:-1:2])) + 2 * (sum(y[2:-2:2]))), 5)
        text_ans = f'({b} - {a})/{6 * n} * (({y[0]} + {y[-1]}) + 4({sum(y[1:-1:2])}) + 2({sum(y[2:-2:2])})) = {round((b - a) / (6 * n), 5)} * {(y[0] + y[-1]) + 4 * (sum(y[1:-1:2])) + 2 * (sum(y[2:-2:2]))} = {ans}'
    other['ans'] = ans
    other['text_ans'] = text_ans
    return xi, func_x, other


if __name__ == '__main__':
    g = func_rect(1.2, 2.1, 10, '0.1 * x ** 4 + 2.1 * x ** 3 - 1.3 * x ** 2 + 3.1 * x + 2.5', 2)
    for el in g:
        for key, value in el.items():
            print(f'{key} = {value}')
