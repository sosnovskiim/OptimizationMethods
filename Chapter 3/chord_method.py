from math import sin

fd = lambda x: 2 * x - 2 + 2 * sin(x)
a, b = -0.5, 1
eps = 0.00001
fda, fdb = fd(a), fd(b)
x = a - fda / (fda - fdb) * (a - b)
fdx = fd(x)
while abs(fdx) > eps:
    if fdx > 0:
        b = x
        fdb = fdx
    else:
        a = x
        fda = fdx
    x = a - fda / (fda - fdb) * (a - b)
    fdx = fd(x)
print(f"Метод хорд: {round(x, 5)}")
