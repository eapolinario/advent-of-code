import sys
import pytest

def read():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    return lines

def process(lines: list[str]) -> int:
    ans = 0
    for line in lines:
        filtered = [c for c in line if c.isdigit()]
        ans += (ord(filtered[0]) - ord('0')) * 10 + (ord(filtered[-1]) - ord('0'))
    return ans

@pytest.mark.parametrize("lines, expected_sum", [
    (["1abc2"], 12),
    (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], 142)
])
def test_single_line(lines, expected_sum):
    assert process(lines) == expected_sum

def main():
    lines = read()
    ans = process(lines)
    print(f"sum is {ans}")



if __name__ == "__main__":
    main()
