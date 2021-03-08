#!/usr/bin/env python3

from collections import deque

class Cups:
    def __init__(self, cups):
        self.current = cups[0]
        self.next_cup = {}
        for i, c in enumerate(cups, 1):
            try:
                self.next_cup[c] = cups[i]
            except IndexError:
                self.next_cup[c] = cups[0]

    def __iter__(self):
        return self

    def step(self):
        remove = []
        to_move = self.current
        for i in range(3):
            remove.append(self.next_cup[to_move])
            to_move = self.next_cup[to_move]
        self.next_cup[self.current] = self.next_cup[remove[2]]
        destination = self.current - 1
        while destination <= 0 or destination in remove:
            if destination == 0:
                destination = len(self.next_cup)
            if destination in remove:
                destination -= 1
        self.next_cup[destination], self.next_cup[remove[2]] = (
            remove[0],
            self.next_cup[destination],
        )
        self.current = self.next_cup[self.current]


if __name__ == '__main__':
    cups_data = [int(c) for c in '496138527']
    cups_data.extend(range(10, 1000001))
    cups = Cups(cups_data)
    for i in range(10000000):
        cups.step()
    a = cups.next_cup[1]
    b = cups.next_cup[a]
    print(f'multiplication of labels is {a*b}')
