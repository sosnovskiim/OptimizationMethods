f = lambda x: 2 * x ** 2 - 6 * x - 3
a, b = -1, 3
eps = 0.00001
h = (b - a) / 4
x0 = a
while abs(h) >= eps:
    x1 = x0 + h
    if f(x0) <= f(x1):
        h = -h / 4
    x0 = x1
print(f"Метод поразрядного поиска: {round(x0, 5)}")
