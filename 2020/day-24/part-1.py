#!/usr/bin/env python3

from collections import defaultdict

def parse_path(line):
    print(line)
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

if __name__ == '__main__':
    import sys
    lines= []
    for line in sys.stdin:
        lines.append(line)

    print(lines)

    paths = []
    for line in lines:
        paths.append(parse_path(line.strip()))

    print(paths)

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

    print(f'tiles={dict(tiles)}')

    blacks = 0
    for pos, side in tiles.items():
        if side%2 == 1:
            blacks += 1

    print(f'total blacks up is {blacks}')
