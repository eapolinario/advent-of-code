import sys
from typing import Tuple

def parse_assignment(assignment_str: str) -> Tuple:
    assignment = assignment_str.split('-')
    return int(assignment[0]), int(assignment[1])

def parse_line(line: str) -> Tuple[Tuple[int], Tuple[int]]:
    assignments = line.split(',')
    return parse_assignment(assignments[0]), parse_assignment(assignments[1])

def overlap(a: Tuple[int, int], b: Tuple[int, int]):
    return (a[0] <= b[0] and a[1] >= b[0]) or (b[0] <= a[0] and b[1] >= a[0])


def main():
    assignments = []
    for line in sys.stdin:
        line = line.rstrip()
        assignments.append(parse_line(line))

    ans = 0
    for assignment in assignments:
        if overlap(assignment[0], assignment[1]):
            ans += 1

    print(ans)


if __name__ == '__main__':
    SystemExit(main())
