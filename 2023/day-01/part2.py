import sys
import pytest

def read():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    return lines

def spelled_out(i, line) -> str:
    if line[i:i+3] == "one":
        return "1"
    elif line[i:i+3] == "two":
        return "2"
    elif line[i:i+5] == "three":
        return "3"
    elif line[i:i+4] == "four":
        return "4"
    elif line[i:i+4] == "five":
        return "5"
    elif line[i:i+3] == "six":
        return "6"
    elif line[i:i+5] == "seven":
        return "7"
    elif line[i:i+5] == "eight":
        return "8"
    elif line[i:i+4] == "nine":
        return "9"
    else:
        return ""

@pytest.mark.parametrize("i, line, expected", [
    (0, "two1nine", "2"),
])
def test_spelled_out(i, line, expected):
    assert spelled_out(i, line) == expected


def transform_line(line) -> str:
    transformed_line = ""
    i = 0
    while i < len(line):
        digit = spelled_out(i, line)
        if digit == "":
            transformed_line += line[i]
        else:
            transformed_line += digit
        i += 1
    return transformed_line

@pytest.mark.parametrize("line, expected_line", [
    ("two1nine", "219"),
])
def test_transform_line(line, expected_line):
    assert transform_line(line) == expected_line

def process_transformed_line(line) -> int:
    filtered = [c for c in line if c.isdigit()]
    return (ord(filtered[0]) - ord('0')) * 10 + (ord(filtered[-1]) - ord('0'))

def process(lines: list[str]) -> int:
    ans = 0
    for line in lines:
        transformed_line = transform_line(line)
        ans += process_transformed_line(transformed_line)
    return ans

@pytest.mark.parametrize("lines, expected_sum", [
    (["two1nine"], 29),
    ([
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ], 281),
    # (["1abc2"], 12),
    # (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], 142)
])
def test_single_line(lines, expected_sum):
    assert process(lines) == expected_sum

def main():
    lines = read()
    ans = process(lines)
    print(f"sum is {ans}")



if __name__ == "__main__":
    main()
