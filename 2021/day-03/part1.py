#!/usr/bin/env python3

import sys

def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    return lines

def main():
    lines = read_input()

    n = len(lines)
    cols = len(lines[0])
    zeroes = [0] * cols

    for line in lines:
        for i in range(cols):
            if line[i] == '0':
                zeroes[i] += 1

    print(f'zeroes={zeroes}')

    gamma = ['0'] * cols
    for i in range(cols):
        if zeroes[i] * 2 < len(lines):
            gamma[i] = '1'

    epsilon = ['0'] * cols
    for i in range(cols):
        if gamma[i] == '0':
            epsilon[i] = '1'

    gamma = int('0b' + ''.join(gamma), 2)
    epsilon = int('0b' + ''.join(epsilon), 2)

    print(f'{gamma}, {epsilon}. Multiplication is {gamma * epsilon}')

if __name__ == '__main__':
    main()
