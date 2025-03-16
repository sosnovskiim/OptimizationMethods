f = lambda x: 2 * x ** 2 - 6 * x - 3
a, b = -1, 3
eps = 0.00001
h = (b - a) / 4
x0 = a
f0 = f(x0)
while abs(h) >= eps:
    x1 = x0 + h
    f1 = f(x1)
    if f0 <= f1 or x1 <= a or x1 >= b:
        h = -h / 4
    x0, f0 = x1, f1
print(f"Метод поразрядного поиска: {round(x0, 5)}")
