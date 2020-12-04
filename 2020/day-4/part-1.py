#!/usr/bin/env python3

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
    return True

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
