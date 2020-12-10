#!/usr/bin/env python3

from collections import Counter
import pytest

def calculate_differences(numbers):
    numbers = [0] + sorted(numbers)
    differences = Counter({
        1: 0,
        2: 0,
        3: 1, # we know that the last device is 3 jolts higher than the last connector
    })
    for i in range(0, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff > 3:
            raise Exception('consecutive differences larger than 3')
        differences[diff] += 1
    return differences

@pytest.mark.parametrize('numbers, expected', [
    ([1, 2, 3], Counter({ 1: 3, 2: 0, 3: 1 })),
    ([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], { 1: 7, 2: 0, 3: 5 }),
])
def test_calculate_differences(numbers, expected):
    assert calculate_differences(numbers) == expected

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    numbers = list(map(int, lines))
    print(calculate_differences(numbers))
