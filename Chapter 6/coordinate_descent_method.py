import numpy as np

f = lambda x: (
        (x[0] ** 2 + x[1] ** 2 - 1) ** 2 + (x[0] + x[1] - 1) ** 2)
eps = 0.00001
x = np.array((0, 0))
fx = f(x)
n = x.shape[0]
k = 0
while True:
    x_, fx_ = x, fx
    for j in range(n):
        e = np.array((0, 0))
        e[j] = 1
        phi = lambda alpha: f(x + alpha * e)
        h = 1
        a0 = 1
        while abs(h) >= eps:
            f0 = phi(a0)
            a1 = a0 + h
            f1 = phi(a1)
            if f0 <= f1:
                h = -h / 4
            a0, f0 = a1, f1
        x_ = x + a0 * e
        fx_ = f(x_)
        if j < n - 1:
            x, fx = x_, fx_
    k += 1
    if np.linalg.norm(x_ - x) < eps or abs(fx_ - fx) < eps:
        break
    x, fx = x_, fx_
print(f"Метод циклического покоординатного спуска: "
      f"({x[0]:.5f}, {x[1]:.5f})")
print(f"Количество итераций: {k}")
