#!/usr/bin/env python3

def find_contiguous_sum(numbers, n):
    for i in range(0, len(numbers)):
        c = n - numbers[i]
        print(f'c={c}')
        for j in range(i + 1, len(numbers)):
            print(f'j={j}, numbers[j]={numbers[j]}')
            if c - numbers[j] == 0:
                return numbers[i:j + 1]
            elif c - numbers[j] < 0:
                break
            else:
                c -= numbers[j]
    raise Exception('unreachable code')

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    numbers = list(map(int, lines))

    answer = find_contiguous_sum(numbers, 57195069)
    print(answer)
    print(f'sum of smallest and largest = {max(answer) + min(answer)}')
