#!/usr/bin/env python3

import pytest

def parse(expr):
    stack = [[]]
    for i in expr:
        current_node = stack[-1]
        if i == '(':
            new_node = []
            current_node.append(new_node)
            stack.append(new_node)
        elif i == ')':
            stack.pop()
        elif not i.isspace():
            current_node.append(i)

    return stack[0]

@pytest.mark.parametrize('expr, expected', [
    ('1 + 2', ['1', '+', '2']),
    ('1 + 2 + 3', ['1', '+', '2', '+', '3']),
    ('1 * 2 + 3 + (4 + 5)', ['1', '*', '2', '+', '3', '+', ['4', '+', '5']]),
])
def test_parse(expr, expected):
    assert parse(expr) == expected

def compute(tokens) -> int:
    acc = 0
    op = '+'
    state = 'expr'
    i = 0
    while i < len(tokens):
        print(f'acc={acc}, op={op}, state={state}, i={i}, tokens[i]={tokens[i]}')
        if state == 'expr':
            if isinstance(tokens[i], list):
                v = compute(tokens[i])
            else:
                v = int(tokens[i])
            if op == '+':
                acc += v
            elif op == '*':
                acc *= v
            else:
                raise Exception('unreachable code')
            state = 'op'
        elif state == 'op':
            op = tokens[i]
            state = 'expr'
        i += 1
    return acc

@pytest.mark.parametrize('tokens, expected', [
    (['1', '+', '3'], 4),
    (['1', '+', ['3', '*', '2']], 7),
    (['1', '+', '2', '*', '3', '+', '4', '*', '5', '+', '6'], 71),
])
def test_compute(tokens, expected):
    assert compute(tokens) == expected

def parse_and_compute(expr):
    return compute(parse(expr))

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())


    results = map(parse_and_compute, lines)

    print(f'total sum or results = {sum(results)}')
