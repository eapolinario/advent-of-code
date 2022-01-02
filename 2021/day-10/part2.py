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
    return False


def find_first_illegal_character(line):
    s = []
    for c in line:
        # print(f'c={c}, s={s}')
        if is_opening_char(c):
            s.append(c)
            continue
        if is_closing_char(c):
            if chars_match(s[-1], c):
                s.pop()
                continue
            else:
                return True, s
    return False, s


def main():

    lines = read_input()
    scores = []
    for line in lines:
        print(f'\nhandling line={line}')

        print(f'{find_first_illegal_character(line)}')
        is_corrupted, stack = find_first_illegal_character(line)
        if is_corrupted:
            print(f'{line} is corrupted')
            continue

        print(f'stack={stack}')
        line_score = 0
        point_map = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }
        for c in stack[::-1]:
            line_score = line_score*5 + point_map[c]

        scores.append(line_score)

    scores = sorted(scores)
    print(f'Total score={scores[int(len(scores)/2)]}')


if __name__ == '__main__':
    main()
