#!/usr/bin/env python3

import itertools

def parse_cubes(lines):
    cubes = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            cubes[(x, y, 0, 0)] = c
    return cubes

def generate_neighbor_positions(cubes, cube):
    neighbors = []
    dim = len(cube)
    for coords in itertools.product([-1, 0, 1], repeat=dim):
        if coords == (0,) * dim:
            continue
        pos = tuple(a + b for a, b in zip(cube, coords))
        neighbors.append(pos)
    return neighbors

def active_neighbors(cubes, cube) -> int:
    return len(list(filter(lambda pos: cubes.get(pos) == '#', generate_neighbor_positions(cubes, cube))))

def step(cubes):
    new_cubes = {}
    candidates = set(cubes)
    [candidates.add(neighbor) for cube in cubes for neighbor in generate_neighbor_positions(cubes, cube)]
    for cube in candidates:
        n_active_neighbors = active_neighbors(cubes, cube)
        cube_v = cubes.get(cube, '.')
        if cube_v == '#' and n_active_neighbors in [2, 3]:
            new_cubes[cube] = '#'
        elif cube_v == '.' and n_active_neighbors == 3:
            new_cubes[cube] = '#'
    return new_cubes

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    cubes = parse_cubes(lines)
    for _ in range(6):
        cubes = step(cubes)

    print(f"total active = {sum(1 for cube_v in cubes.values() if cube_v == '#')}")
