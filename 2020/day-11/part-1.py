#!/usr/bin/env python3

from copy import deepcopy

def number_adjacent_occupied(grid, x, y):
    occupied = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if grid.get((x + i, y + j)) and grid[(x + i, y + j)] == '#':
                occupied += 1
    return occupied

def step(grid):
    new_grid = deepcopy(grid)
    for p, v in grid.items():
        x, y = p
        number_adjacent = number_adjacent_occupied(grid, x, y)
        # print(f'x={x}, y={y}, v={v}, number_adjacent={number_adjacent}')
        if v == 'L' and number_adjacent == 0:
            new_grid[(x, y)] = '#'
        elif v == '#' and number_adjacent >= 4:
            new_grid[(x, y)] = 'L'
    return new_grid

def print_grid(grid, width, height):
   for y in range(height):
       r = ''
       for x in range(width):
          r += grid[(x, y)]
       print(r)

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    print(lines)
    grid = {}
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            grid[(c, r)] = lines[r][c]

    height = len(lines)
    width = len(lines[0])

    print_grid(grid, width, height)

    new_grid = None
    iteration = 1
    while True:
        # print(f'iteration={iteration}')
        new_grid = step(grid)
        # print_grid(new_grid, width, height)
        if new_grid == grid:
            break
        grid = new_grid

    # print(new_grid)

    occupied = 0
    for p, v in new_grid.items():
        if v == '#':
            occupied += 1

    print(f'final tally = {occupied}')
