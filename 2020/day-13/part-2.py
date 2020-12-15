#!/usr/bin/env python3

from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

if __name__ == '__main__':
    import sys

    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    buses = [(i, int(bus)) for i, bus in enumerate(lines[1].split(',')) if bus != 'x']
    n = [bus for _, bus in buses]
    a = [bus - i for i, bus in buses]
    print(f'n={n}')
    print(f'a={a}')
    print(chinese_remainder(n, a))
