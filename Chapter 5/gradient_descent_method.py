import numpy as np

f = lambda x: (99 * x[0] ** 2 + 196 * x[0] * x[1] +
               99 * x[1] ** 2 - 95 * x[0] - 9 * x[1] + 91)
pd1 = lambda x: 198 * x[0] + 196 * x[1] - 95
pd2 = lambda x: 196 * x[0] + 198 * x[1] - 9
norm = lambda grad: (grad[0] ** 2 + grad[1] ** 2) ** 0.5
eps = 0.00001
alpha = 3.31
x = np.array((-11, -11))
fx = f(x)
grad = np.array((pd1(x), pd2(x)))
norm_grad = norm(grad)
k = 0
while norm_grad > eps:
    y = x - alpha * (grad / norm_grad)
    fy = f(y)
    if fy < fx:
        x, fx = y, fy
        grad[0], grad[1] = pd1(x), pd2(x)
        norm_grad = norm(grad)
    else:
        alpha /= 2
    k += 1
print(f"Метод градиентного спуска: ({x[0]:.5f}, {x[1]:.5f})")
print(f"Количество итераций: {k}")
