f = lambda x: x ** 4 + x ** 3 - 9 * x ** 2 - 9 * x - 1
fd = lambda x: 4 * x ** 3 + 3 * x ** 2 - 18 * x - 9
a, b = -3, 3
eps = 0.00001
L = 72
fa, fb = f(a), f(b)
pair_min = (
    0.5 / L * (fa - fb + L * (a + b)),
    0.5 * (fa + fb + L * (a - b))
)
pairs = [pair_min]
x, p = pair_min[0], pair_min[1]
fx = f(x)
delta = 0.5 / L * (fx - p)
while 2 * L * delta > eps:
    x1 = x - delta
    x2 = x + delta
    p = 0.5 * (fx + p)
    pairs.remove(pair_min)
    pairs.append((x1, p))
    pairs.append((x2, p))
    pair_min = None
    for pair in pairs:
        if pair_min is None or pair_min[1] > pair[1]:
            pair_min = pair
    x, p = pair_min[0], pair_min[1]
    fx = f(x)
    delta = 0.5 / L * (fx - p)
print(f"Метод ломаных: {round(x, 5)}")
