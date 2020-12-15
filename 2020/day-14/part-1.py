#!/usr/bin/env python3

from copy import deepcopy
import pytest

def parse_mask(line):
    parsed_mask = line.split('=')[1].strip()
    return ('mask', (int(parsed_mask.replace("X", "0"), 2), int(parsed_mask.replace("X", "1"), 2)))

@pytest.mark.parametrize('line, expected_mask', [
    ('mask = X1011100000X111X01001000001110X00000', ('mask', (int('010111000000111001001000001110000000', 2), int('110111000001111101001000001110100000', 2)))),
])
def test_parse_mask(line, expected_mask):
    assert parse_mask(line) == expected_mask

def parse_memory_access(line):
    parts = line.split('=')
    memory_address = int(parts[0].strip()[4:-1])
    value = int(parts[1].strip())
    return 'memory_access', (memory_address, value)

@pytest.mark.parametrize('line, expected_memory_access', [
    ('mem[4616] = 8311689', ('memory_access', (4616, 8311689))),
])
def test_parse_memory_access(line, expected_memory_access):
    assert parse_memory_access(line) == expected_memory_access

def parse_instructions(lines):
    instructions = []
    for line in lines:
        if line[0:4] == 'mask':
           instructions.append(parse_mask(line))
        else:
            instructions.append(parse_memory_access(line))
    return instructions

def step(current_memory, current_mask, instruction):
    memory = deepcopy(current_memory)
    mask = deepcopy(current_mask)
    instr_type = instruction[0]
    if instr_type == 'mask':
        mask = instruction[1]
    elif instr_type == 'memory_access':
        memory_address = instruction[1][0]
        memory_value = instruction[1][1]
        memory[memory_address] = (memory_value & mask[1]) | mask[0]
    return memory, mask

@pytest.mark.parametrize('current_memory, current_mask, instruction, expected_result', [
    ({}, parse_mask('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')[1], parse_memory_access('mem[8] = 11'), ({8: 73}, parse_mask('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')[1])),
])
def test_step(current_memory, current_mask, instruction, expected_result):
    assert step(current_memory, current_mask, instruction) == expected_result


if __name__ == '__main__':
    import sys

    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    instructions = parse_instructions(lines)

    memory = {}
    mask = None
    for instruction in instructions:
        memory, mask = step(memory, mask, instruction)

    total_sum = 0
    for m, v in memory.items():
       total_sum += v

    print(f'total_sum={total_sum}')
