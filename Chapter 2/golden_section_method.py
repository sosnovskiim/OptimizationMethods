f = lambda x: 2 * x ** 2 - 6 * x - 3
a, b = -1, 3
eps = 0.00001
tau = (5 ** 0.5 - 1) / 2
eps_n = (b - a) / 2
while eps_n > eps:
    x1 = b - (b - a) * tau
    x2 = a + (b - a) * tau
    if f(x1) <= f(x2):
        b = x2
    else:
        a = x1
    eps_n *= tau
print(f"Метод золотого сечения: {round((a + b) / 2, 5)}")
