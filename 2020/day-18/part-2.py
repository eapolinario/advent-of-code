#!/usr/bin/env python3

import pytest
import re

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_name(str):
    return re.match(r"\w+", str)

def peek(stack):
    return stack[-1] if stack else None

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))

def compare_precedence(op1, op2):
    precedences = {'+' : 1, '*' : 0}
    return precedences[op1] > precedences[op2]

def shunting_yard_parse(expression):
    tokens = re.findall(r"[+*()]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop() # Discard the '('
        else:
            top = peek(operators)
            while top is not None and top not in "()" and compare_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    return operators, values

def compute_postfix_notation(operators, values):
    while peek(operators) is not None:
        apply_operator(operators, values)
    return values[0]

@pytest.mark.parametrize('expr, expected', [
    ('1 + 2', 3),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 46),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
    ('1 + 2 * 3 + 4 * 5 + 6', 231),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
])
def test_compute(expr, expected):
    operators, values = shunting_yard_parse(expr)
    assert compute_postfix_notation(operators, values) == expected

def parse_and_compute(expr):
    operators, values = shunting_yard_parse(expr)
    return compute_postfix_notation(operators, values)

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    print(f'total sum or results = {sum(map(parse_and_compute, lines))}')
