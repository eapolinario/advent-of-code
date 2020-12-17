#!/usr/bin/env python3

def parse_cubes(lines):
    cubes = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            cubes[(x, y, 0)] = c
    return cubes

def active_neighbors(cubes, cube) -> int:
    # print('inside active_neighbors')
    # print(f'cubes={cubes}, cube={cube}')
    active_count = 0
    for xs in [-1, 0, 1]:
        for ys in [-1, 0, 1]:
            for zs in [-1, 0, 1]:
                if xs == 0 and ys == 0 and zs == 0:
                    continue
                p = (cube[0] + xs, cube[1] + ys, cube[2] + zs)
                # print(f'p={p}')
                if cubes.get(p) == '#':
                    # print(f'found active neighbor = {p}')
                    active_count += 1
    return active_count

def step(cubes):
    new_cubes = {}
    candidates = set()
    for cube in cubes:
        for xs in [-1, 0, 1]:
            for ys in [-1, 0, 1]:
                for zs in [-1, 0, 1]:
                    if xs == 0 and ys == 0 and zs == 0:
                        continue
                    candidates.add((cube[0] + xs, cube[1] + ys, cube[2] + zs))
                    candidates.add(cube)

    # print(f'candidates={candidates}')
    for cube in candidates:
        n_active_neighbors = active_neighbors(cubes, cube)
        # print(f'cube={cube}, cube_v={cubes.get(cube)}, active={n_active_neighbors}, ')
        cube_v = cubes.get(cube, '.')
        if cube_v == '#' and n_active_neighbors in [2, 3]:
            new_cubes[cube] = '#'
        elif cube_v == '.' and n_active_neighbors == 3:
            new_cubes[cube] = '#'
        # TODO: not sure if we need this
        # else:
        #     new_cubes[cube] = '.'
    return new_cubes

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    cubes = parse_cubes(lines)
    # print(f'cubes={cubes}')
    for _ in range(6):
        # print(f'previous cubes = {cubes}')
        cubes = step(cubes)
        # print(f'next cubes = {cubes}')
    # print(f'cubes={cubes}')

    active = 0
    for cube in cubes:
       if cubes[cube] == '#':
           active += 1

    print(f'total active = {active}')
