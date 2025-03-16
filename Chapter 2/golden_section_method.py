f = lambda x: 2 * x ** 2 - 6 * x - 3
a, b = -1, 3
eps = 0.00001
eps_n = (b - a) / 2
tau = (5 ** 0.5 - 1) / 2
x1 = b - tau * (b - a)
x2 = a + tau * (b - a)
f1, f2 = f(x1), f(x2)
while eps_n > eps:
    if f1 <= f2:
        b, x2, f2 = x2, x1, f1
        x1 = a + b - x2
        f1 = f(x1)
    else:
        a, x1, f1 = x1, x2, f2
        x2 = a + b - x1
        f2 = f(x2)
    eps_n *= tau
print(f"Метод золотого сечения: {round((a + b) / 2, 5)}")
