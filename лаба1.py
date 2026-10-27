# -*- coding: cp1251 -*-
from math import *

m = float(input('Введите значение m: '))
n = float(input('Введите значение n: '))

# Вычисление z1
numerator1 = (m - 1) * sqrt(m) - (n - 1) * sqrt(n)
denominator1 = sqrt(m**3 * n + n * m + m**2 - m)
z1 = numerator1 / denominator1

# Вычисление z2
numerator2 = sqrt(m) - sqrt(n)
z2 = numerator2 / m

print("m={0:.2f} n={1:.2f}".format(m, n))
print("z1={0:.4f} z2={1:.4f}".format(z1,z2))