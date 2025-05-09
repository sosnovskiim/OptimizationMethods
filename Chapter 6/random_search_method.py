import numpy as np

f = lambda x: (
        (x[0] ** 2 + x[1] ** 2 - 1) ** 2 + (x[0] + x[1] - 1) ** 2)
eps = 0.00001
alpha = 0.5
x = np.array((0, 0))
fx = f(x)
k = 0
while True:
    j = 1
    while j <= 6:
        xi = np.random.rand(2) * 2 - 1
        while True:
            y = x + alpha * (xi / np.linalg.norm(xi))
            fy = f(y)
            if fy < fx:
                x, fx = y, fy
            else:
                j += 1
                break
    k += 1
    if alpha < eps:
        break
    alpha /= 2
print(f"Метод случайного поиска: ({x[0]:.5f}, {x[1]:.5f})")
print(f"Количество итераций: {k}")
