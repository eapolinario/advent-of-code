#!/usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip())

numbers = list(map(int, lines))

def three_sum(total_sum, numbers):
    s = set(numbers)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (total_sum - (numbers[i] + numbers[j])) in s:
                return (numbers[i], numbers[j], total_sum - (numbers[i] + numbers[j]))
    raise Exception(f"couldn't find a triple that added up to {total_sum}")

triple = three_sum(2020, numbers)

print(f"Result of multiplication: {triple[0]*triple[1]*triple[2]}")
