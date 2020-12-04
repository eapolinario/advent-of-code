#!/usr/bin/env python3

import pytest
import sys

def parse_passport(unparsed_passport_lines):
    passport = {}
    for line in unparsed_passport_lines:
        for p in line.split(' '):
            print(p)
            k, v = p.split(':')
            passport[k] = v
    return passport

def is_passport_valid(passport: dict) -> bool:
    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    passport_fields = set(passport.keys())
    for f in required_fields:
        if f not in passport_fields:
            return False

    for f,v in passport.items():
        print(f'f={f}, v={v}')
        if f == 'byr':
            if len(v) != 4:
                return False
            v = int(v)
            if v < 1920 or v > 2002:
                return False
        elif f == 'iyr':
            if len(v) != 4:
                return False
            v = int(v)
            if v < 2010 or v > 2020:
                return False
        elif f == 'eyr':
            if len(v) != 4:
                return False
            v = int(v)
            if v < 2020 or v > 2030:
                return False
        elif f == 'hgt':
            unit = v[-2:]
            try:
                v = int(v[:-2])
            except:
                return False
            if unit == 'cm':
                if v < 150 or v > 193:
                    return False
            elif unit == 'in':
                if v < 59 or v > 76:
                    return False
            else:
                return False
        elif f == 'hcl':
            if len(v) != 7:
                return False
            if v[0] != '#':
                return False
            for c in v[1:]:
                if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    return False
        elif f == 'ecl':
            if v not in ['amb','blu','brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif f == 'pid':
            if len(v) != 9:
                return False
            for c in v:
                if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return False
    return True

@pytest.mark.parametrize('passport, valid', [
    (
        {'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu', 'byr': '1944', 'eyr': '2021', 'pid': '093154719'},
        True,
    ),
])
def test_is_passport_valid(passport, valid):
    assert is_passport_valid(passport) == valid

def main():
    lines = []
    unparsed_passport_lines = []
    for line in sys.stdin:
        print(lines)
        if len(line.rstrip()) == 0:
            unparsed_passport_lines.append(lines)
            lines = []
        else:
            lines.append(line.rstrip())
    unparsed_passport_lines.append(lines)

    passports = []
    for unparsed_passport in unparsed_passport_lines:
       passports.append(parse_passport(unparsed_passport))

    print(passports)
    print()

    valid_passports = 0
    for p in passports:
        print(p)
        if is_passport_valid(p):
            valid_passports += 1

    print(valid_passports)

if __name__ == '__main__':
    main()
