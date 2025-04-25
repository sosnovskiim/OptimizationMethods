import numpy as np

pd1 = lambda x: 198 * x[0] + 196 * x[1] - 95
pd2 = lambda x: 196 * x[0] + 198 * x[1] - 9
eps = 0.00001
x = np.array((0, 0))
grad = np.array((pd1(x), pd2(x)))
H_inv = 1 / 788 * np.array(((198, -196), (-196, 198)))
k = 0
while (grad[0] ** 2 + grad[1] ** 2) ** 0.5 > eps:
    x = x - np.dot(H_inv, grad)
    grad[0], grad[1] = pd1(x), pd2(x)
    k += 1
print(f"Метод Ньютона: ({x[0]:.5f}, {x[1]:.5f})")
print(f"Количество итераций: {k}")
