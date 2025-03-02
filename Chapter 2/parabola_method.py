f = lambda x: x ** 3 + 4 * x ** 2 - 3 * x + 1
a, b = -1, 2
eps = 0.00001
x1, x2, x3 = a, (a + b) / 2, b
x_prev, x_min = None, None
delta = 1
while delta > eps:
    a1 = (f(x2) - f(x1)) / (x2 - x1)
    a2 = 1 / (x3 - x2) * ((f(x3) - f(x1)) / (x3 - x1) -
                          (f(x2) - f(x1)) / (x2 - x1))
    x_min = 0.5 * (x1 + x2 - a1 / a2)
    if f(x_min) >= f(x2):
        x1 = x_min
    else:
        x1 = x2
        x2 = x_min
    if x_prev is not None:
        delta = abs(x_prev - x_min)
    x_prev = x_min
print(f"Метод парабол: {round(x_min, 5)}")
