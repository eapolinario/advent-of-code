import pytest
import sys

def read_input():
    lines = []
    for line in sys.stdin:
        stripped_line = line.rstrip()
        lines.append(stripped_line)
    return lines

def is_opening_char(c):
    return c in ['(', '[', '{', '<']

def is_closing_char(c):
    return c in [')', ']', '}', '>']

def chars_match(a, b):
    if a == '(':
        return b == ')'
    if a == '[':
        return b == ']'
    if a == '{':
        return b == '}'
    if a == '<':
        return b == '>'
    raise Exception('unreachable code!')


def find_first_illegal_character(line):
    s = []
    for c in line:
        print(f'c={c}, s={s}')
        if is_opening_char(c):
            s.append(c)
            continue
        if is_closing_char(c):
            if chars_match(s[-1], c):
                s.pop()
                continue
            else:
                return c
        raise Exception('unreachable code!')


@pytest.mark.parametrize('line, expected_char', [
    # ('[({(<(())[]>[[{[]{<()<>>', '}'),
    ('{([(<{}[<>[]}>{[]{[(<()>', '}'),
    ('[[<[([]))<([[{}[[()]]]', ')'),
    ('[{[{({}]{}}([{[{{{}}([]', ']'),
])
def test_find_first_illegal_character(line, expected_char):
    assert find_first_illegal_character(line) == expected_char

def count_open(line):
    return list(filter(is_opening_char, line))

def count_closed(line):
    return list(filter(is_closing_char, line))

def is_incomplete(line):
    open_chars = count_open(line)
    closed_chars = count_closed(line)
    print(f'open_chars={open_chars}')
    print(f'close_chars={closed_chars}')
    return len(open_chars) != len(closed_chars)

@pytest.mark.parametrize('line, expected_value', [
    ('[({(<(())[]>[[{[]{<()<>>', True),
    ('{([(<{}[<>[]}>{[]{[(<()>', False),
])
def test_is_incomplete(line, expected_value):
    is_incomplete(line) is expected_value


def main():

    lines = read_input()
    score = 0
    for line in lines:
        print(f'\nhandling line={line}')
        try:
            c = find_first_illegal_character(line)
            if c == ')':
                score += 3
            elif c == ']':
                score += 57
            elif c == '}':
                score += 1197
            elif c == '>':
                score += 25137
        except Exception as e:
            print(f'exception is {e}')
            continue

        if is_incomplete(line):
            print(f'{line} is incomplete')


    print(f'Total syntax error score is {score}')

if __name__ == '__main__':
    main()
