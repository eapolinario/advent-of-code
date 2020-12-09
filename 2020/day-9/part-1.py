#!/usr/bin/env python3

def find_first_not_sum(numbers, preamble):
    for i in range(preamble, len(numbers)):
        print(f'i={i}, N[i]={numbers[i]}')
        is_sum = False
        for j in range(i - preamble, i):
            if is_sum:
                break
            for k in range(j + 1, i):
                if numbers[i] == numbers[j] + numbers[k]:
                    print(f'i={i}, N[i]={numbers[i]}, j={j}, k={k}, N[j]={numbers[j]}, N[k]={numbers[k]}')
                    print('found sum!')
                    is_sum = True
                    break

        if is_sum == False:
            return numbers[i]

    raise Exception('unreachable code')

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    numbers = list(map(int, lines))
    print(numbers)

    print(find_first_not_sum(numbers, 25))
