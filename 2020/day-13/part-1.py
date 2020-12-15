#!/usr/bin/env python3

from math import ceil

import sys
lines = []
for line in sys.stdin:
    lines.append(line.strip())

N = int(lines[0])
input = lines[1].split(',')
print(input)

numbers = []
for n in input:
    if n == 'x':
        continue
    numbers.append(int(n))

print(f'numbers={numbers}')


min_bus_id = -1
min_bus_time = -1
for i in numbers:
    c = ceil(N / i) * i
    if min_bus_id == -1 or c < min_bus_time:
        min_bus_id = i
        min_bus_time = c

print(f'min_bus_id={min_bus_id}, min_bus_time={min_bus_time}')

print(min_bus_id * (min_bus_time - N))
