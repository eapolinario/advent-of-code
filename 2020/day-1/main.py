#!/usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip())

numbers = list(map(int, lines))

def find_pair(total_sum, numbers):
    """Find pair in `numbers` that add up to `total_sum`"""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == total_sum:
                return (numbers[i], numbers[j])
    raise Exception(f"couldn't find a pair that added up to {total_sum}")

pair = find_pair(2020, numbers)

print(f"Result of multiplication: {pair[0]*pair[1]}")
