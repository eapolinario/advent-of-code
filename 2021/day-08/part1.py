import sys
from typing import List

class Entry:
    def __init__(self, unique_signal_pattern, four_digit_output_value):
        self.unique_signal_pattern = unique_signal_pattern
        self.four_digit_output_value = four_digit_output_value

    def __repr__(self):
        return f'usp={self.unique_signal_pattern} | dov={self.four_digit_output_value}'

def read_input() -> List[Entry]:
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    entries = []
    for line in lines:
        line_split = line.split('|')
        unique_signal_patters_s = line_split[0]
        four_digit_output_value_s = line_split[1]
        entries.append(Entry([v for v in unique_signal_patters_s.split(' ') if len(v) > 0], [v for v in four_digit_output_value_s.split(' ') if len(v) > 0]))

    return entries

def main():
    entries = read_input()

    print(f'entries={entries}')

    easy_digits = 0
    for entry in entries:
        for digit in entry.four_digit_output_value:
            fdov_len = len(digit)
            if fdov_len in [7, 4, 2, 3]:
                easy_digits += 1

    print(f'Total easy digits is {easy_digits}')


if __name__ == '__main__':
    main()
