#!/usr/bin/env python3

from typing import List, Set
import pytest
from collections import defaultdict

def parse_line(line):
    # search for 'bags contain'
    src, rest = line.split('bags contain')
    # clean up dst from spaces
    src = src.strip()
    i = line.find('bags contain ') + len('bags contain')
    dst = set()
    while i < len(line):
        j = line.find('bag', i)
        if j == -1:
            break
        print(f'i={i}, j={j}')
        parts = line[i:j].split(' ')
        print(f'parts={parts}')
        if parts[1] == 'no':
            q = 0
            adv = len('other bags')
        else:
            q = int(parts[1])
            adv = len('bags')
            bag = " ".join(parts[2:-1])
            print(f'q={q}, bag={bag}')
            dst.add((bag, q))
        i = j + adv

    return {'dst': dst, 'src': src}

@pytest.mark.parametrize('line, expected', [
    (
        'posh teal bags contain 2 faded coral bags, 3 striped crimson bags, 1 faded red bag.',
        {
            'src': 'posh teal',
            'dst': set([
                ('striped crimson', 3),
                ('faded coral', 2),
                ('faded red', 1),
            ]),
        }
    ),
    (
        'drab black bags contain 1 drab plum bag.',
        {
            'src': 'drab black',
            'dst': set([
                ('drab plum', 1),
            ]),
        }
    ),
    (
        'mirrored cyan bags contain 2 vibrant tomato bags, 4 clear black bags, 4 striped gold bags.',
        {
            'src': 'mirrored cyan',
            'dst': set([
                ('vibrant tomato', 2),
                ('clear black', 4),
                ('striped gold', 4),
            ]),
        }
    ),
    (
        'clear black bags contain no other bags.',
        {
            'src': 'clear black',
            'dst': set([]),
        }
    ),
])
def test_parse_line(line, expected):
    assert parse_line(line) == expected

def build_graph(vertices: List[dict]):
    g = {}
    for vertex_description in vertices:
        print(f'vertex_description={vertex_description}')
        for v in vertex_description['dst']:
            print(f'v={v}')
            g[vertex_description['src']] = vertex_description['dst']
    print(f'g={g}')
    return dict(g)

@pytest.mark.parametrize('vertices_description, expected', [
    ([{'src': 'a', 'dst': set([('b', 2), ('c', 1)])}], {'a': set([('b', 2), ('c', 1)])}),
    (
        [
            {'src': 'a', 'dst': set([('b', 42), ('c', 2)])},
            {'src': 'b', 'dst': set([('c', 3)])},
        ],
        {'a': set([('b', 42), ('c', 2)]), 'b': set([('c', 3)])},
    ),
])
def test_build_graph(vertices_description, expected):
    assert dict(build_graph(vertices_description)) == expected

def dfs(graph, node, visited: Set[bool]):
    count = 0
    print(f'node={node}, visited={visited}')
    for v in graph.get(node, []):
        print(f'v={v}')
        if v[0] in visited:
            continue
        visited.add(v[0])
        count += v[1]*dfs(graph, v[0], visited)
        visited.remove(v[0])
    return count + 1

@pytest.mark.parametrize('graph, initial_node, expected_count', [
    (
        {'b': set([('a', 1)]), 'c': set([('a', 2), ('b', 3)])},
        'c',
        8 + 1,
    ),
    (
        {
            'sg': set([('dr', 2)]),
            'dr': set([('do', 2)]),
            'do': set([('dy', 2)]),
            'dy': set([('dg', 2)]),
            'dg': set([('db', 2)]),
            'db': set([('dv', 2)]),
            'dv': set([]),
        },
        'sg',
        126 + 1,
    )
])
def test_dfs(graph, initial_node, expected_count):
    assert dfs(graph, initial_node, set()) == expected_count

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    g = build_graph(map(parse_line, lines))
    print(dfs(g, 'shiny gold', set()))
