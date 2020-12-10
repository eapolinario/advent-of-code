#!/usr/bin/env python3

import functools
import pytest

def calculate_arrangements(numbers):
    numbers = [0] + sorted(numbers)

    return calculate(numbers, 0, {})

def calculate(numbers, i, table):
    print(f'begin - i={i}')
    if i == len(numbers) - 1:
        return 1

    answers = 0
    for j in range(i + 1, len(numbers)):
        if numbers[j] - numbers[i] > 3:
            break
        if not table.get(j):
            table[j] = calculate(numbers, j, table)
        answers += table[j]
    return answers

@pytest.mark.parametrize('numbers, expected', [
    ([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], 8),
    ([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49], 19208),
])
def test_calculate_arrangements(numbers, expected):
    assert calculate_arrangements(numbers) == expected

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    numbers = list(map(int, lines))
    print(calculate_arrangements(numbers))
