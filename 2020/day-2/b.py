#!/usr/bin/env python

import pytest
import sys
from operator import xor

def parse_line(line):
    policy, password = line.split(':')
    times, char = policy.split(' ')
    min_times, max_times = list(map(int, times.split('-')))

    return min_times, max_times, char, password.lstrip()

def is_valid(p1, p2, char, password):
    found_p1 = password[p1 - 1] == char
    found_p2 = password[p2 - 1] == char
    return xor(found_p1, found_p2)

@pytest.mark.parametrize('p1, p2, char, password, expected', [
    (1, 3, 'a', 'abcde', True),
    (1, 3, 'c', 'abcde', True),
    (1, 3, 'b', 'cdefg', False),
    (2, 3, 'b', 'bhngbb', False),
    (2, 9, 'c', 'ccccccccc', False),
])
def test_is_valid(p1, p2, char, password, expected):
    assert is_valid(p1, p2, char, password) == expected

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    c = 0
    for line in lines:
        min_times, max_times, char, password = parse_line(line)
        if is_valid(min_times, max_times, char, password):
            print(min_times, max_times, char, password)
            c += 1
    print(f'final tally of valid passwords is {c}')
