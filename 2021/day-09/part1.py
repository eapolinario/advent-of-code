import sys

def read_input():
    grid = []
    for line in sys.stdin:
        grid.append(line.rstrip())

    return grid

def get_v(grid, x, y):
    if x < 0 or x == len(grid[0]) or y < 0 or y == len(grid):
        return -1
    return grid[y][x]


def is_lowest(grid, x, y):
    p = grid[y][x]

    candidates = [v for v in [get_v(grid, x - 1, y), get_v(grid, x + 1, y), get_v(grid, x, y - 1), get_v(grid, x, y + 1)] if v != -1]
    return min(candidates) > p

def main():
    grid = read_input()
    print(f'grid={grid}')

    lowest_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_lowest(grid, x, y):
                print(f'lowest point coordinates = {(x, y)}')
                lowest_points.append(grid[y][x])

    print(f'lowest_points={lowest_points}')
    print(f'Sum or risk levels is {sum([(1 + int(v)) for v in lowest_points])}')


if __name__ == '__main__':
    main()
