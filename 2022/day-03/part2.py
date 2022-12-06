import sys
import numpy as np

def parse_line(line):
    return line[:len(line) // 2], line[len(line) // 2:]

def test_parse_line():
    assert parse_line("abcd") == ("ab", "cd")
    assert parse_line("abcdef") == ("abc", "def")

def chunks(xs, n):
    n = max(1, n)
    return (xs[i:i+n] for i in range(0, len(xs), n))

def duplicate_letter(s1, s2, s3):
    for a in s1:
        for b in s2:
            if a == b and a in s3:
                return a
    raise ValueError("no duplicate letter could be found in the 3 strings")


def main():
    rucksacks = []
    for line in sys.stdin:
        line = line.rstrip()
        rucksacks.append(line)

    groups = chunks(rucksacks, 3)

    answer = 0
    for group in groups:
        x = duplicate_letter(group[0], group[1], group[2])
        if 'a' <= x <= 'z':
            answer += ord(x) - ord('a') + 1
        elif 'A' <= x <= 'Z':
            answer += ord(x) - ord('A') + 27

    print(answer)

if __name__ == '__main__':
    SystemExit(main())
