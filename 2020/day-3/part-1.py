#!/usr/bin/env python

import sys

if __name__ == '__main__':
    maze = []
    for line in sys.stdin:
        maze.append(line.rstrip())

    x = y = 0
    height = len(maze)
    width = len(maze[0])

    total_trees = 0
    while y < height:
       if maze[y][x] == '#':
           total_trees += 1
       x = (x + 3) % width
       y += 1

    print(f"total trees hit is {total_trees}")
