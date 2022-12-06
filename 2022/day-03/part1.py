import sys

def parse_line(line):
    return line[:len(line) // 2], line[len(line) // 2:]

def test_parse_line():
    assert parse_line("abcd") == ("ab", "cd")
    assert parse_line("abcdef") == ("abc", "def")

def duplicate_letter(s1, s2):
    for c in s1:
        if c in s2:
            return c

def main():
    rucksacks = []
    for line in sys.stdin:
        line = line.rstrip()
        rucksacks.append(parse_line(line))

    answer_part1 = 0
    for rucksack in rucksacks:
        # Find duplicate letter
        letter = duplicate_letter(rucksack[0], rucksack[1])
        # Find priority value
        if 'a' <= letter <= 'z':
            answer_part1 += ord(letter) - ord('a') + 1
        elif 'A' <= letter <= 'Z':
            answer_part1 += ord(letter) - ord('A') + 27

    print(answer_part1)

if __name__ == '__main__':
    SystemExit(main())
