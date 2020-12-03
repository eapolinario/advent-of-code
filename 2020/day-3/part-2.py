#!/usr/bin/env python3

import sys

def count_trees_hit(x, y, step_x, step_y, maze):
    height = len(maze)
    width = len(maze[0])

    total_trees = 0
    while y < height:
       if maze[y][x] == '#':
           total_trees += 1
       x = (x + step_x) % width
       y += step_y

    return total_trees


if __name__ == '__main__':
    maze = []
    for line in sys.stdin:
        maze.append(line.rstrip())

    total_trees_hit = 1
    for step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        total_trees_hit *= count_trees_hit(0, 0, step[0], step[1], maze)

    print(f"total trees hit is {total_trees_hit}")
