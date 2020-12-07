#!/usr/bin/env python3

from typing import List
import pytest
from collections import defaultdict

def parse_line(line):
    # search for 'bags contain'
    dst, rest = line.split('bags contain')
    # clean up dst from spaces
    dst = dst.strip()
    i = line.find('bags contain ') + len('bags contain')
    src = set()
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
            src.add((bag, q))
        i = j + adv

    return {'dst': dst, 'src': src}

@pytest.mark.parametrize('line, expected', [
    (
        'posh teal bags contain 2 faded coral bags, 3 striped crimson bags, 1 faded red bag.',
        {
            'dst': 'posh teal',
            'src': set([
                ('striped crimson', 3),
                ('faded coral', 2),
                ('faded red', 1),
            ]),
        }
    ),
    (
        'drab black bags contain 1 drab plum bag.',
        {
            'dst': 'drab black',
            'src': set([
                ('drab plum', 1),
            ]),
        }
    ),
    (
        'mirrored cyan bags contain 2 vibrant tomato bags, 4 clear black bags, 4 striped gold bags.',
        {
            'dst': 'mirrored cyan',
            'src': set([
                ('vibrant tomato', 2),
                ('clear black', 4),
                ('striped gold', 4),
            ]),
        }
    ),
    (
        'clear black bags contain no other bags.',
        {
            'dst': 'clear black',
            'src': set([]),
        }
    ),
])
def test_parse_line(line, expected):
    assert parse_line(line) == expected

def build_graph(vertices: List[dict]):
    g = defaultdict(set)
    for vertex_description in vertices:
        print(f'vertex_description={vertex_description}')
        for v in vertex_description['src']:
            print(f'v={v}')
            g[v[0]].add(vertex_description['dst'])
    print(f'g={g}')
    return dict(g)

@pytest.mark.parametrize('vertices_description, expected', [
    ([{'dst': 'a', 'src': set([('b', 2), ('c', 1)])}], {'b': set(['a']), 'c': set(['a'])}),
    (
        [
            {'dst': 'a', 'src': set([('b', 42), ('c', 2)])},
            {'dst': 'b', 'src': set([('c', 2)])},
        ],
        {'b': set(['a']), 'c': set(['a', 'b'])},
    ),
])
def test_build_graph(vertices_description, expected):
    assert dict(build_graph(vertices_description)) == expected

def bfs(graph, initial_node):
    visited = set()
    q = [initial_node]
    count = 0
    while len(q) > 0:
        print(f' q={q}')
        node = q.pop(0)
        print(f'node={node}, count={count}, visited={visited}')
        if node in visited:
            continue
        else:
            visited.add(node)
        if node != initial_node:
            count += 1
        children = graph.get(node, [])
        print(f'children={children}')
        for c in children:
            q.append(c)
    return count

@pytest.mark.parametrize('graph, initial_node, expected_count', [
    (
        {'b': set(['a']), 'c': set(['a', 'b'])},
        'c',
        2,
    ),
    (
        {'sg': set(['bw', 'my']), 'bw': set(['do', 'lr']), 'my': set(['do', 'lr'])},
        'sg',
        4,
    )
])
def test_bfs(graph, initial_node, expected_count):
    assert bfs(graph, initial_node) == expected_count

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    g = build_graph(map(parse_line, lines))
    print(bfs(g, 'shiny gold'))
