from math import *

m = float(input('Введите m (m > 0): '))
n = float(input('Введите n (n >= 0): '))

# Проверка области допустимых значений
if m <= 0 or n < 0:
    print("Ошибка: m > 0, n >= 0")
else:
    # Подкоренное выражение знаменателя z1
    d = m**3 * n + n * m + m**2 - m
    if d <= 0:
        print("Ошибка: знаменатель z1 не определён (d <= 0)")
    else:
        z1 = ((m - 1) * sqrt(m) - (n - 1) * sqrt(n)) / sqrt(d)
        z2 = (sqrt(m) - sqrt(n)) / m
        print("{0:.4f} {1:.4f}".format(z1, z2))
