#!/usr/bin/env python3

import pytest

def decode_seat(seat: str):
    first_part = seat[:7]
    second_part = seat[7:]

    lower = 0
    upper = 127
    print(f'{lower},{upper}')
    for c in first_part:
        print(f'at the beginning of iteration: {c} => {lower},{upper}')
        if c == 'F':
            upper = (lower + upper)//2
        elif c == 'B':
            lower = (lower + upper)//2 + 1
        else:
            raise Exception('unrecognized symbol')
        print(f'{c} => {lower},{upper}')

    assert lower == upper
    row = lower

    lower = 0
    upper = 7
    print(f'second_part={second_part}')
    for c in second_part:
        if c == 'L':
            upper = (lower + upper)//2
        elif c == 'R':
            lower = (lower + upper)//2 + 1
        else:
            raise Exception('unrecognized symbol')
        print(f'{c} => {lower},{upper}')

    assert upper == lower
    column = lower

    return {'row': row, 'column': column, 'seat_id': row*8 + column}

@pytest.mark.parametrize('seat, expected', [
    ('FBFBBFFRLR', {'row': 44, 'column': 5, 'seat_id': 357}),
    ('BFFFBBFRRR', {'row': 70, 'column': 7, 'seat_id': 567}),
    ('FFFBBBFRRR', {'row': 14, 'column': 7, 'seat_id': 119}),
    ('BBFFBBFRLL', {'row': 102, 'column': 4, 'seat_id': 820}),
])
def test_decode_seat(seat, expected):
    assert decode_seat(seat) == expected

if __name__ == '__main__':
    import sys
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    seats = map(decode_seat, lines)

    seat_ids = set([seat['seat_id'] for seat in seats])

    print(seat_ids)

    for s in range(1, 987):
        if s not in seat_ids and s - 1 in seat_ids and s + 1 in seat_ids:
            print(f'found seat={s}')
            break
