#!/usr/bin/env python3

from copy import deepcopy
import pytest

def parse_mask(line):
    parsed_mask = line.split('=')[1].strip()
    return ('mask', parsed_mask)

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

def replace_x(mask, i):
    if i == len(mask):
        return set([''])
    new_accumulated = set()
    replaced_masks = replace_x(mask, i + 1)
    # print(f'mask={mask}, i={i}')
    # print(f'replaced_masks={replaced_masks}')
    for s in replaced_masks:
        if mask[i] == 'X':
            new_accumulated.add('1' + s)
            new_accumulated.add('0' + s)
        else:
            new_accumulated.add(mask[i] + s)
    # print(f'new_accumulated={new_accumulated}')
    return new_accumulated

def generate_addresses(mask):
    # import pdb; pdb.set_trace()
    replaced_masks = replace_x(mask, 0)
    # print(f'mask={mask}, replaced_masks={replaced_masks}')
    return replaced_masks

@pytest.mark.parametrize('mask, expected_masks', [
    ('1', set(['1'])),
    ('0', set(['0'])),
    ('0X', set(['01', '00'])),
    ('X1', set(['11', '01'])),
    ('0XX', set(['010', '000', '011', '001'])),
    ('X0X', set(['000', '001', '100', '101'])),
])
def test_generate_floating_masks(mask, expected_masks):
    assert generate_addresses(mask) == expected_masks

def step(current_memory, current_mask, instruction):
    memory = deepcopy(current_memory)
    mask = deepcopy(current_mask)
    instr_type = instruction[0]
    if instr_type == 'mask':
        mask = instruction[1]
    elif instr_type == 'memory_access':
        memory_address = '{0:036b}'.format(instruction[1][0])
        memory_value = int(instruction[1][1])
        masked_value = []
        for i in range(36):
            if mask[i] == 'X':
                masked_value.append('X')
            elif mask[i] == '1':
                masked_value.append('1')
            else:
                masked_value.append(memory_address[i])
        for final_address in generate_addresses(masked_value):
            memory[final_address] = memory_value
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
    print(f'instructions={instructions}')

    memory = {}
    mask = None
    for instruction in instructions:
        print(f'instruction={instruction}')
        memory, mask = step(memory, mask, instruction)
        # print(f'memory={memory}')

    total_sum = 0
    for m, v in memory.items():
       total_sum += v

    print(f'total_sum={total_sum}')
