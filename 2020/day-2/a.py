#!/usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip())

def parse_line(line):
    policy, password = line.split(':')
    times, char = policy.split(' ')
    min_times, max_times = list(map(int, times.split('-')))

    return min_times, max_times, char, password

def is_valid(min_times, max_times, char, password):
    times = 0
    for c in password:
        if c == char:
            times += 1

    return min_times <= times <= max_times

if __name__ == '__main__':
    c = 0
    for line in lines:
        min_times, max_times, char, password = parse_line(line)
        if is_valid(min_times, max_times, char, password):
            print(password)
            c += 1
    print(f'final tally of valid passwords is {c}')
