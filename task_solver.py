def func_rect(a, b, n, func, way):
    h = round((b - a) / n, 5)
    half_h = h / 2
    xi = {}
    func_x = {}
    other = {}
    if way == 0:
        other['h'] = h
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
        return xi, ci, func_c, other

    if way == 1:
        other['h'] = h
        for i in range(n + 1):
            x = round(a + i * h, 5)
            xi[f'x{i}'] = x
            func_x[f'f({i})'] = round(eval(func), 5)
        g = list(func_x.values())
        ans = round(h * ((g[0] + g[-1]) / 2 + sum(g[1:-1])), 5)
    else:
        other['h'] = half_h
        for i in range(2 * n + 1):
            x = round(a + i * half_h, 5)
            xi[f'x{i}'] = x
            func_x[f'f({i})'] = round(eval(func), 5)
        g = list(func_x.values())
        ans = round((b - a) / (6 * n) * ((g[0] + g[-1]) + 4 * (sum(g[1:-1:2])) + 2 * (sum(g[2:-2:2]))), 5)
    other['ans'] = ans
    return xi, func_x, other


if __name__ == '__main__':
    print(func_rect(1.2, 2.1, 10, '0.1 * x ** 4 + 2.1 * x ** 3 - 1.3 * x ** 2 + 3.1 * x + 2.5', 0))
