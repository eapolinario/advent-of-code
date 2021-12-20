import sys
import re
import pytest
from collections import Counter
from typing import List

class Line:
    def __init__(self, x0, y0, x1, y1, dir):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.dir = dir

    def __eq__(self, o) -> bool:
        print(f'self={self}\no={o}')
        return self.x0 == o.x0 and self.y0 == o.y0 and self.x1 == o.x1 and self.y1 == o.y1 and self.dir == o.dir

    def __repr__(self) -> str:
        return f'{self.x0},{self.y0} -> {self.x1},{self.y1}'



def parse_line(line):
    x0, y0, x1, y1 = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups()
    if x0 == x1:
        dir = 'V'
    elif y0 == y1:
        dir = 'H'
    else:
        dir = 'D'
    return Line(int(x0), int(y0), int(x1), int(y1), dir)

def test_parse_line():
    assert parse_line('0,0 -> 0,1') == Line(0, 0, 0, 1, 'V')
    assert parse_line('0,0 -> 1,0') == Line(0, 0, 1, 0, 'H')
    assert parse_line('1,1 -> 2,2') == Line(1, 1, 2, 2, 'D')



def read_input(lines_s: List[str]) -> List[Line]:
    lines = []
    for line_s in lines_s:
        try:
            lines.append(parse_line(line_s))
        except Exception as e:
            print(e)

    return lines

def draw_line(grid: Counter, line: Line):
    if line.dir == 'V':
        min_y = min(line.y0, line.y1)
        max_y = max(line.y0, line.y1)
        assert line.x0 == line.x1
        for y in range(min_y, max_y + 1):
            grid[(line.x0, y)] += 1
    elif line.dir == 'H':
        min_x = min(line.x0, line.x1)
        max_x = max(line.x0, line.x1)
        assert line.y0 == line.y1
        for x in range(min_x, max_x + 1):
            grid[(x, line.y0)] += 1
    elif line.dir == 'D':
        if line.x0 < line.x1:
            most_left = (line.x0, line.y0)
            most_right = (line.x1, line.y1)
        else:
            most_right = (line.x0, line.y0)
            most_left = (line.x1, line.y1)


        # breakpoint()
        xs = range(most_left[0], most_right[0] + 1)
        dir = 'up'
        if most_left[1] < most_right[1]:
            ys = range(most_left[1], most_right[1] + 1)
        else:
            ys = range(most_left[1], most_right[1] - 1, -1)

        assert len(xs) == len(ys)
        for p in zip(xs, ys):
            grid[(p[0], p[1])] += 1
    else:
        raise Exception(f'impossible line={line}')

@pytest.mark.parametrize('lines, expected_grid', [
    (
        [Line(2, 0, 0, 2, 'D')],
        Counter({(2, 0): 1, (1, 1): 1, (0, 2): 1}),
    ),
    (
        [Line(0, 0, 2, 2, 'D')],
        Counter({(0, 0): 1, (1, 1): 1, (2, 2): 1}),
    ),
    (
        [Line(2, 0, 0, 2, 'D'), Line(0, 0, 2, 2, 'D')],
        Counter({(2, 0): 1, (1, 1): 2, (0, 2): 1}),
    ),
])
def test_draw_line(lines, expected_grid):
    grid = Counter()
    for line in lines:
        draw_line(grid, line)
    assert grid == expected_grid

def main():
    lines_s = []
    for line_s in sys.stdin:
        line_s = line_s.rstrip()
        lines_s.append(line_s)

    lines = read_input(lines_s)

    grid = Counter()
    for line in lines:
        draw_line(grid, line)

    print(grid)
    count = 0
    for pos, value in grid.items():
        print(f'pos={pos}, value={value}')
        if value > 1:
            count += 1

    print(f'Total count is {count}')



if __name__ == '__main__':
    main()
