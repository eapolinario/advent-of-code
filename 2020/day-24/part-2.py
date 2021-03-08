#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict, Tuple

def parse_path(line):
    i = 0
    path = []
    while i < len(line):
        if line[i] in ['e', 'w']:
            path.append(line[i])
            i += 1
        elif line[i] in ['n', 's']:
            path.append(line[i:i+2])
            i += 2
        else:
            raise Exception('invalid direction in line')
    return path

def count_black_neighbors(tiles, p):
    n_black = 0
    for dir in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
        if tiles.get((p[0] + dir[0], p[1] + dir[1], p[2] + dir[2])) == 1:
            n_black += 1
    return n_black

def generate_neighbors(pos):
    neighbors = []
    for dir in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
        neighbors.append((pos[0] + dir[0], pos[1] + dir[1], pos[2] + dir[2]))
    return neighbors

def simulate(tiles: Dict[Tuple[int, int, int], int]):
    new_tiles = {}
    candidates = set()
    for pos, color in tiles.items():
        candidates.add(pos)
        if color == 1:
            for neighbor in generate_neighbors(pos):
                candidates.add(neighbor)
    for pos in candidates:
        color = tiles.get(pos, 0)
        assert color in [0, 1]
        n_black = count_black_neighbors(tiles, pos)
        if color%2 == 1 and (n_black == 0 or n_black > 2):
            new_tiles[pos] = 0
        elif color%2 == 0 and n_black == 2:
            new_tiles[pos] = 1
        else:
            if color == 1:
                new_tiles[pos] = color
    return new_tiles

if __name__ == '__main__':
    import sys
    lines= []
    for line in sys.stdin:
        lines.append(line)

    paths = []
    for line in lines:
        paths.append(parse_path(line.strip()))

    tiles = defaultdict(int)
    for path in paths:
        p = (0, 0, 0)
        for dir in path:
            if dir == 'e':
                p = (p[0] + 1, p[1] - 1, p[2])
            elif dir == 'se':
                p = (p[0], p[1] - 1, p[2] + 1)
            elif dir == 'sw':
                p = (p[0] - 1, p[1], p[2] + 1)
            elif dir == 'w':
                p = (p[0] - 1, p[1] + 1, p[2])
            elif dir == 'nw':
                p = (p[0], p[1] + 1, p[2] - 1)
            elif dir == 'ne':
                p = (p[0] + 1, p[1], p[2] - 1)
            else:
                raise Exception('invalid direction')
        tiles[p] = (tiles[p] + 1)%2

    for i in range(100):
        tiles = simulate(tiles)
        blacks = 0
        for pos, side in tiles.items():
            if side%2 == 1:
                blacks += 1
    print(f'total blacks up after day {i + 1} is {blacks}')
