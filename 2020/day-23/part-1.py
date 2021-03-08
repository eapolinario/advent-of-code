#!/usr/bin/env python3

from collections import deque

def step(cups):
    current = cups[0]
    cups.rotate(-1)

    pickup = deque([cups.popleft() for _ in range(3)])
    dest = current - 1

    while dest not in cups:
        dest -= 1
        if dest <= 0:
            dest = max(cups)
            break

    while cups[0] != dest:
        cups.rotate(-1)
    cups.rotate(-1)

    for x in range(3):
        cups.appendleft(pickup.pop())

    while cups[0] != current:
        cups.rotate(-1)
    cups.rotate(-1)

    return cups

if __name__ == '__main__':
    cups = deque([int(c) for c in '496138527'])
    for _ in range(100):
        print(f'before: cups={cups}')
        cups = step(cups)
        print(f'after: cups={cups}')

    index_1 = cups.index(1)
    ans = []
    for i in range(1, 9):
       ans.append(cups[(index_1 + i)%len(cups)])

    print(''.join(map(str, ans)))
