import sys
from typing import List, Mapping

DIGIT_MAPPING: Mapping[int, str] = {
    1: 'cf',
    7: 'acf',
    4: 'bcdf',
    2: 'acdeg',
    3: 'acdfg',
    5: 'abdfg',
    0: 'abcefg',
    6: 'abdefg',
    9: 'abcdfg',
    8: 'abcdefg',
}

def find_segments(digits, size):
    return [v for v in digits if len(v) == size]

def share_segment(digit0, digit1):
    print(f'digit0={digit0}, digit1={digit1}')
    return set(digit0).intersection(digit1) == set(digit0)

def find_zero_and_six(digits, one, nine):
    for candidate in find_segments(digits, 6):
        if candidate == nine:
            continue

        if share_segment(one, candidate):
            zero = candidate
        else:
            six = candidate
    return zero, six

def find_two_and_five(digits, three, six):
    print(f'two_and_five candidates={list(find_segments(digits, 5))}')
    for candidate in find_segments(digits, 5):
        print(f'candidate={candidate}')
        if candidate == three:
            continue

        if share_segment(candidate, six):
            five = candidate
        else:
            two = candidate
    return two, five


def find_six(digits, one, nine):
    for candidate in find_segments(digits, 6):
        if candidate == nine:
            continue

        if share_segment(one, candidate):
            return candidate
    raise Exception('unreachable')

def find_one(digits):
    return find_segments(digits, 2)[0]

def find_three(digits, one):
    for candidate in find_segments(digits, 5):
        if share_segment(one, candidate):
            return candidate
    raise Exception('unreachable')

def find_four(digits):
    return find_segments(digits, 4)[0]

def find_seven(digits):
    return find_segments(digits, 3)[0]

def find_eight(digits):
    return find_segments(digits, 7)[0]

def find_nine(digits, four):
    for candidate in find_segments(digits, 6):
        if share_segment(four, candidate):
            return candidate
    raise Exception('unreachable')



def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    total_sum = 0
    for line in lines:
        line_split = line.split(' | ')
        unique_signal_patters_s = line_split[0]
        four_digit_output_value_s = line_split[1]

        digits = [''.join(sorted(v)) for v in unique_signal_patters_s.split(' ')]
        output_values = [''.join(sorted(v)) for v in four_digit_output_value_s.split(' ')]

        print(f'digits={digits}, output_values={output_values}')

        one = find_one(digits)
        print(f'one={one}')
        four = find_four(digits)
        seven = find_seven(digits)
        eight = find_eight(digits)

        three = find_three(digits, one)
        nine = find_nine(digits, four)
        zero, six = find_zero_and_six(digits, one, nine)
        two, five = find_two_and_five(digits, three, six)

        mapping = {
            zero: '0',
            one: '1',
            two: '2',
            three: '3',
            four: '4',
            five: '5',
            six: '6',
            seven: '7',
            eight: '8',
            nine: '9',
        }
        print(f'mapping={mapping}')

        number_s = ''
        for output_value in output_values:
           number_s += mapping[output_value]

        total_sum += int(number_s)

    print(f'Total sum of decoded output value is {total_sum}')

if __name__ == '__main__':
    main()
