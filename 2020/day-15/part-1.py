#!/usr/bin/env python3

import pytest

from collections import defaultdict

def calculate_next_number(state, last_number, index):
    # print(f'state={dict(state)}, last_number={last_number}, index={index}')
    if len(state[last_number]) <= 1:
        last_number = 0
    else:
        last_number_list = state[last_number]
        last_number = last_number_list[-1] - last_number_list[-2]
    state[last_number].append(index)
    return state, last_number

def process(puzzle, rounds):
    state = defaultdict(list)
    for index, i in enumerate(puzzle):
        state[i].append(index + 1)
    last_number = puzzle[-1]
    for i in range(len(puzzle) + 1, rounds + 1):
         state, last_number = calculate_next_number(state, last_number, i)
    # print(f'last_number={last_number}')
    return last_number

@pytest.mark.parametrize('puzzle, rounds, expected_last_number', [
    ([0,3,6], 2020, 436),
])
def test_process(puzzle, rounds, expected_last_number):
    assert process(puzzle, rounds) == expected_last_number

if __name__ == '__main__':
    import sys

    puzzle = [2,20,0,4,1,17]
    process(puzzle, 2020)
