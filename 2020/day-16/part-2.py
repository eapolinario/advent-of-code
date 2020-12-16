#!/usr/bin/env python3

import pytest
from itertools import permutations
from tqdm import tqdm
from collections import defaultdict

def parse_input(lines):
    fields = []
    your_ticket = []
    nearby_tickets = []

    state = 'reading constraints'
    for line in lines:
        if len(line.strip()) == 0:
            continue

        print(line)
        if line.startswith('your ticket'):
            state = 'your ticket'
            continue
        elif line.startswith('nearby tickets'):
            state = 'nearby tickets'
            continue

        if state == 'reading constraints':
            description, contraints_str = line.split(':')
            contraints_pair = contraints_str.split(' or ')
            constraints = []
            for p in contraints_pair:
                low, high = p.split('-')
                low = int(low)
                high = int(high)
                constraints.append((low, high))
            fields.append((description, constraints))
        elif state == 'your ticket':
            your_ticket = [int(i) for i in line.split(',')]
        elif state == 'nearby tickets':
            nearby_tickets.append([int(i) for i in line.split(',')])

    return (fields, your_ticket, nearby_tickets)

def is_valid(value, field):
    constraints = field[1]
    return (constraints[0][0] <= value <= constraints[0][1]) or (constraints[1][0] <= value <= constraints[1][1])

def calculate_invalid_values(fields, ticket):
    invalid_values = []
    for n in ticket:
        valid = False
        checks = list(map(lambda f: is_valid(n, f), fields))
        if not any(checks):
            invalid_values.append(n)
    return invalid_values

@pytest.mark.parametrize('fields, ticket, expected', [
    ([('a', [(1, 3), (5, 7)])], [1, 4, 6], [4]),
])
def test_calculate_invalid_values(fields, ticket, expected):
    assert calculate_invalid_values(fields, ticket) == expected

def determine_field_order(nearby_tickets, fields):
    valid_tickets = list(filter(lambda t: len(calculate_invalid_values(fields, t)) == 0, nearby_tickets))

    candidates = defaultdict(list)
    for field_index, field in enumerate(fields):
        for mapping_index in range(len(fields)):
            valid_mapping = True
            for ticket in valid_tickets:
                if not is_valid(ticket[mapping_index], field):
                    valid_mapping = False
                    break
            if valid_mapping:
                candidates[field_index].append(mapping_index)

    # Candidates can have
    for k, v in candidates.items():
        print(f'k={k}, len(v)={len(v)}')

    final_mapping = {}
    while len(candidates):
        # Find the key that has a mapping to 1
        single_mapping = None
        to_delete = None
        for k, v in candidates.items():
            if len(v) == 1:
                single_mapping = v[0]
                final_mapping[k] = single_mapping
                to_delete = k
                break
        del candidates[to_delete]
        for k, v in candidates.items():
            if single_mapping in v:
                v.remove(single_mapping)

    return final_mapping

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    fields, your_ticket, nearby_tickets = parse_input(lines)

    field_order = determine_field_order(nearby_tickets, fields)

    result = 1
    for index, field in enumerate(fields):
        if field[0].startswith('departure'):
           result *= your_ticket[field_order[index]]

    print(result)
