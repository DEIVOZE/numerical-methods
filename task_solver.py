def func_rect(a, b, n, func):
    h = round((b - a) / n, 5)
    half_h = h / 2
    xi = {}
    ci = {}
    func_x = {}
    func_c = {}
    for i in range(n * 2 + 1):
        x = round(a + half_h * i, 5)
        if i % 2 == 0:
            xi[f'x{i // 2}'] = x
            func_x[f'f(x{i // 2})'] = round(eval(func), 5)
        else:
            ci[f'c{i // 2 + 1}'] = x
            func_c[f'f(c{i // 2 + 1})'] = round(eval(func), 5)
    return xi, ci, func_x, func_c
