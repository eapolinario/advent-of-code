#!/usr/bin/env python3

import sys

def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    return lines

def find_candidates(matrix, initial_candidates, ith, value):
    """
    Returns a trimmed list of candidates where line[i] == value
    """
    candidates = []
    for i in initial_candidates:
        if matrix[i][ith] == value:
            candidates.append(i)

    return candidates

def find_oxygen_generator_rating(matrix):
    candidates = list(range(len(matrix)))
    ith = 0
    while len(candidates) != 1:
        zero_candidates = find_candidates(matrix, candidates, ith, '0')
        one_candidates = find_candidates(matrix, candidates, ith, '1')

        if len(zero_candidates) > len(one_candidates):
            candidates = zero_candidates
        else:
            candidates = one_candidates

        ith += 1

    print(f'candidates={candidates}')
    return int('0b' + matrix[candidates[0]], 2)


def find_co2_scrubber_rating(matrix):
    candidates = list(range(len(matrix)))
    ith = 0
    while len(candidates) != 1:
        zero_candidates = find_candidates(matrix, candidates, ith, '0')
        one_candidates = find_candidates(matrix, candidates, ith, '1')

        if len(zero_candidates) <= len(one_candidates):
            candidates = zero_candidates
        else:
            candidates = one_candidates

        ith += 1

    print(f'candidates={candidates}')
    return int('0b' + matrix[candidates[0]], 2)

def main():
    lines = read_input()

    oxygen = find_oxygen_generator_rating(lines)
    co2 = find_co2_scrubber_rating(lines)
    print(f'oxygen={oxygen}, co2={co2}. The multiplication is {oxygen * co2}')


if __name__ == '__main__':
    main()
