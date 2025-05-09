import numpy as np

f = lambda x: (
        (x[0] ** 2 + x[1] ** 2 - 1) ** 2 + (x[0] + x[1] - 1) ** 2)
eps = 0.00001
x = np.array((0, 0))
fx = f(x)
n = x.shape[0]
delta = np.array((0.5, 0.5))
k = 0
while True:
    x_, fx_ = x, fx
    for j in range(n):
        e = np.array((0, 0))
        e[j] = 1
        y = x_ - delta[j] * e
        fy = f(y)
        if fx_ <= fy:
            y = x_ + delta[j] * e
            fy = f(y)
            if fx_ > fy:
                x_, fx_ = y, fy
        else:
            x_, fx_ = y, fy
    k += 1
    if not np.allclose(x, x_):
        x = x + 0.5 * (x_ - x)
        fx = f(x)
    elif np.linalg.norm(delta) < eps:
        break
    else:
        delta /= 2
print(f"Метод Хука-Дживса: ({x[0]:.5f}, {x[1]:.5f})")
print(f"Количество итераций: {k}")
