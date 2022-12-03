import sys

def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    numbers = list(map(int, lines))
    return numbers
