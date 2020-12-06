#!/usr/bin/env python3

import pytest
from collections import Counter

def count_votes(answers_lines):
    votes = Counter()
    for line in answers_lines:
        for c in line:
            votes[c] += 1

    voters = len(answers_lines)
    result = 0
    for v, count in votes.most_common():
        if count == voters:
            result += 1
    return result

@pytest.mark.parametrize('answers_lines, expected_count', [
    (['abc'], 3),
    (['a', 'b', 'c'], 0),
    (['ab', 'bc'], 1),
    (['a', 'a', 'a', 'a'], 1),
    (['b'], 1),
])
def test_count_votes(answers_lines, expected_count):
    assert count_votes(answers_lines) == expected_count

if __name__ == '__main__':
    import sys
    lines = []
    unparsed_answers_lines = []
    for line in sys.stdin:
        print(lines)
        if len(line.rstrip()) == 0:
            unparsed_answers_lines.append(lines)
            lines = []
        else:
            lines.append(line.rstrip())
    unparsed_answers_lines.append(lines)

    print(sum(map(count_votes, unparsed_answers_lines)))
