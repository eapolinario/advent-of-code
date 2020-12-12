#!/usr/bin/env python3

import cmath
import pytest
from functools import reduce

class Ship:
    def __init__(self, pos: complex, dir: complex):
        self.pos = pos
        self.waypoint = dir

    def final_distance(self) -> int:
        return int(abs(ship.pos.real) + abs(ship.pos.imag))

    def __str__(self):
        return f'pos={self.pos}, waypoinit={self.waypoint}'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ship):
            return NotImplemented
        return self.pos == other.pos and self.waypoint == other.waypoint

class Instruction:
    def __init__(self, action: str, value: int):
        self.action = action
        self.value = value

    def __str__(self):
        return f'action={self.action}, value={self.value}'

def parse_instruction(line) -> Instruction:
    action = line[0]
    value = int(line[1:])
    return Instruction(action, value)

def next_position(ship: Ship, instruction: Instruction) -> Ship:
    print(f'ship={ship}, instruction={instruction}')
    action = instruction.action
    if action == 'F':
        return Ship(ship.pos + instruction.value * ship.waypoint, ship.waypoint)
    elif action == 'N':
        return Ship(ship.pos, ship.waypoint + instruction.value * complex(0, 1))
    elif action == 'S':
        return Ship(ship.pos, ship.waypoint + instruction.value * complex(0, -1))
    elif action == 'E':
        return Ship(ship.pos, ship.waypoint + instruction.value * complex(1, 0))
    elif action == 'W':
        return Ship(ship.pos, ship.waypoint + instruction.value * complex(-1, 0))
    elif action == 'L':
        rotations = (instruction.value//90)%4
        return Ship(ship.pos, ship.waypoint * reduce(lambda c1, c2: c1 * c2, rotations * [complex(0, 1)]))
    elif action == 'R':
        rotations = ( instruction.value//90 )%4
        return Ship(ship.pos, ship.waypoint * reduce(lambda c1, c2: c1 * c2, rotations * [complex(0, -1)]))
    else:
        raise Exception('unreachable code')

@pytest.mark.parametrize('ship, instruction, expected_ship', [
    (Ship(complex(10, 0), complex(1, 0)), parse_instruction('R270'), Ship(complex(10, 0), complex(0, 1))),
    (Ship(complex(10, 0), complex(1, 0)), parse_instruction('R180'), Ship(complex(10, 0), complex(-1, 0))),
    (Ship(complex(10, 0), complex(1, 0)), parse_instruction('R90'), Ship(complex(10, 0), complex(0, -1))),
])
def test_next_position(ship, instruction, expected_ship):
    assert next_position(ship, instruction) == expected_ship


if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    instructions = map(parse_instruction, lines)
    ship = Ship(complex(0, 0), complex(10, 1))
    for instruction in instructions:
        ship = next_position(ship, instruction)

    print(f'final ship position = {ship.pos}')
    print(f'{ship.final_distance()}')
