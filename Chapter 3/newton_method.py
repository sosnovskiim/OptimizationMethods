from math import cos, sin

fd = lambda x: 2 * x - 2 + 2 * sin(x)
fdd = lambda x: 2 + 2 * cos(x)
a, b = -0.5, 1
eps = 0.00001
x = (a + b) / 2
fdx = fd(x)
while abs(fdx) > eps:
    x = x - (fdx / fdd(x))
    fdx = fd(x)
print(f"Метод Ньютона: {round(x, 5)}")
