from math import sin

fd = lambda x: 2 * x - 2 + 2 * sin(x)
a, b = -0.5, 1
eps = 0.00001
x = (a + b) / 2
fdx = fd(x)
while abs(fdx) > eps:
    if fdx > 0:
        b = x
    else:
        a = x
    x = (a + b) / 2
    fdx = fd(x)
print(f"Метод средней точки: {round(x, 5)}")
