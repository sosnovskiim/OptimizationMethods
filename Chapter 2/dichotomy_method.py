f = lambda x: 2 * x ** 2 - 6 * x - 3
a, b = -1, 3
eps = 0.00001
delta = eps
while (b - a) / 2 > eps:
    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2
    if f(x1) <= f(x2):
        b = x2
    else:
        a = x1
print(f"Метод дихотомии: {round((a + b) / 2, 5)}")
