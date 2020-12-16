#!/usr/bin/env python3

import pytest

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
        print(f'n={n}')
        print(f'fields={fields}')
        valid = False
        checks = list(map(lambda f: is_valid(n, f), fields))
        print(f'checks={checks}')
        print(f'any={any(checks)}')
        if not any(checks):
            invalid_values.append(n)
        print(f'invalid_values={invalid_values}')
    return invalid_values

@pytest.mark.parametrize('fields, ticket, expected', [
    ([('a', [(1, 3), (5, 7)])], [1, 4, 6], [4]),
])
def test_calculate_invalid_values(fields, ticket, expected):
    assert calculate_invalid_values(fields, ticket) == expected

def process_nearby_tickets(nearby_tickets, fields):
    all_invalid = []
    for ticket in nearby_tickets:
        all_invalid.extend(calculate_invalid_values(fields, ticket))

    return sum(all_invalid)

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    fields, your_ticket, nearby_tickets = parse_input(lines)
    print(f'sum of all invalid values={process_nearby_tickets(nearby_tickets, fields)}')
