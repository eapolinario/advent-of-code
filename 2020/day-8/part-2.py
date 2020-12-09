#!/usr/bin/env python3

import pytest

def parse_instruction(line):
    operation, argument_str = line.split(' ')
    return (operation, int(argument_str))

@pytest.mark.parametrize('line, expected', [
    ('nop +0', ('nop', 0)),
    ('acc +3', ('acc', 3)),
    ('acc -3', ('acc', -3)),
])
def test_parse_instruction(line, expected):
    assert parse_instruction(line) == expected

def step(program, pc, acc):
    operation, argument = program[pc]
    if operation == 'nop':
        return program, pc + 1, acc
    elif operation == 'acc':
        return program, pc + 1, acc + argument
    elif operation == 'jmp':
        return program, pc + argument, acc

def simulate(program):
    acc = 0
    pc = 0
    executed_instructions = set()
    while pc not in executed_instructions and pc < len(program):
        executed_instructions.add(pc)
        program, pc, acc = step(program, pc, acc)
    return (pc == len(program), acc)

@pytest.mark.parametrize('program, expected', [
    (
        [
            ('nop', 0),
            ('acc', 1),
            ('jmp', 4),
            ('acc', 3),
            ('jmp', -3),
            ('acc', -99),
            ('acc', 1),
            ('jmp', -4),
            ('acc', 6),
        ],
        (False, 5)
    ),
])
def test_simulate(program, expected):
    assert simulate(program) == expected

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    program = list(map(parse_instruction, lines))

    for i in range(len(program)):
        op, argument = program[i]
        if op in ['nop', 'jmp']:
            if op == 'nop':
                program[i] = ('jmp', argument)
            elif op == 'jmp':
                program[i] = ('nop', argument)
            terminate, acc = simulate(program)
            if terminate:
                print(f'After program terminates acc = {acc}')
            program[i] = (op, argument)
