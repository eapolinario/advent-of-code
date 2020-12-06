#!/usr/bin/env python3

import pytest

def count_votes(answers_lines):
    votes = set()
    for line in answers_lines:
        for c in line:
            votes.add(c)
    return len(votes)

@pytest.mark.parametrize('answers_lines, expected_count', [
    (['abcx', 'abcy', 'abcz'], 6),
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
