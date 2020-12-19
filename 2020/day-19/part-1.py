#!/usr/bin/env python3

import pytest
import re

def parse_rule(line):
    parts = line.strip().split(': ')
    rule_number = parts[0]
    rules = []
    for sub_rule in parts[1].split(' '):
        rules.append(sub_rule)
    return (rule_number, rules)

def parse_rules(lines):
    rules = {}
    for line in lines:
        print(f'line={line}')
        rule_number, sub_rules = parse_rule(line)
        rules[rule_number] = sub_rules
    return rules

def build_pattern(rules, i) -> str:
    regex = []
    for sub_rule in rules[i]:
        if sub_rule[0] == '"':
            regex.append(sub_rule[1])
        elif sub_rule == '|':
            regex.append(sub_rule)
        else:
            regex.append(build_pattern(rules, sub_rule))
    return f"({''.join(regex)})"

@pytest.mark.parametrize('rules, i, expected_regex', [
    ({'0': ['1', '2'], '1': [ '"b"' ], '2': [ '"a"' ]}, '0', '((b)(a))'),
    ({'0': ['1', '2', '|', '3'], '1': [ '"b"' ], '2': [ '3' ], '3': [ '"a"' ]}, '0', '((b)(a)|(a))'),
])
def test_build_pattern(rules, i, expected_regex):
    assert build_pattern(rules, i) == expected_regex

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        if line.strip() == '':
            break
        lines.append(line.strip())

    search_strings = []
    for line in sys.stdin:
        search_strings.append(line.strip())

    rules = parse_rules(lines)
    print(f'rules={rules}')

    pattern_0 = f"^{build_pattern(rules, '0')}$"
    print(f'pattern={pattern_0}')

    count = 0
    for s in search_strings:
        if re.match(pattern_0, s):
            count += 1

    print(f'total matches = {count}')
