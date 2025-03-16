def Lip(a, b):
    mx = fd(a)
    i = float(a)
    while i < b:
        var = fd(i)
        if mx < var:
            mx = var
        i += 0.01
    return mx


# f = lambda x: (x + 3) * (x + 1) * x * (x - 3) - 1
f = lambda x: x ** 4 + x ** 3 - 9 * x ** 2 - 9 * x - 1
fd = lambda x: 4 * x ** 3 + 3 * x ** 2 - 18 * x - 9
a, b = -3, 3
eps = 0.00001
L = round(Lip(a, b))
x0 = 1 / (2 * L) * (f(a) - f(b) + L * (a + b))
p = 1 / 2 * (f(a) + f(b) + L * (a - b))
delta = 1 / (2 * L) * (f(x0) - p)
while 2 * L * delta > eps:
    x1 = x0 - delta
    x2 = x0 + delta
    if f(x1) < f(x2):
        x0 = x1
    else:
        x0 = x2
    p = 0.5 * (f(x0) + p)
    delta = 1 / (2 * L) * (f(x0) - p)
print(f"Метод ломаных: {round(x0, 5)}")
