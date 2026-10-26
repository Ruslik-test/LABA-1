from math import *
def formula1(alpha):
    z1 = ((m - 1) * sqrt(m) - (n - 1) * sqrt(n)) / sqrt(m**3 * n) + n * m + m**2 - m
    print("{0:.4f}".format(z1))

def formula2(alpha):
    z2 = (sqrt(m) - sqrt(n)) / m
    print("{0:.4f}".format(z2))

m = float(input("Введите параметр m: "))
n = float(input("Введите параметр n: "))

formula1(m)
formula2(m)