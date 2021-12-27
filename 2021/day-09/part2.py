import operator
import sys
from functools import reduce

def read_input():
    grid = {}
    y = 0
    for line in sys.stdin:
        stripped_line = line.rstrip()
        for x in range(len(stripped_line)):
            grid[(x, y)] = stripped_line[x]
        y += 1

    return grid

def is_valid(grid, x, y):
    return grid.get((x, y), 'X') != 'X'


def neighbors(grid, x, y):
    xs = []
    for pos in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        if is_valid(grid, x + pos[0], y + pos[1]):
            xs.append((x + pos[0], y + pos[1]))
    print(f'xs={xs}')
    return xs


def dfs(grid, x, y):
    if grid.get((x, y)) in ['9', 'X']:
        return 0

    grid[(x, y)] = 'X'

    acc = 1
    for candidate in neighbors(grid, x, y):
        print(f'candidate={candidate}')
        acc += dfs(grid, candidate[0], candidate[1])

    return acc


def main():
    grid = read_input()

    # print(f'dfs(0, 0)={dfs(grid, 0, 0)}')
    basins = []
    for p, v in grid.items():
        x, y = p
        print(f'({x},{y})')
        basin_size = dfs(grid, x, y)
        if basin_size > 0:
            basins.append(basin_size)

    print(f'basins={basins}')
    top_basins = sorted(basins, reverse=True)[:3]
    print(f'Multiplication of top three basins = {reduce(operator.mul, top_basins, 1)}')


if __name__ == '__main__':
    main()
