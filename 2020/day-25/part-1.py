#!/usr/bin/env python3

import pytest

MAGIC_NUMBER = 20201227

def find_loop_size(pk, subject_number):
    loop_size = 1
    while pk != pow(subject_number, loop_size, MAGIC_NUMBER):
        loop_size += 1
    return loop_size

@pytest.mark.parametrize('pk, subject_number, expected', [
    (5764801, 7, 8),
    (17807724, 7, 11),
])
def test_find_loop_size(pk, subject_number, expected):
    assert find_loop_size(pk, subject_number) == expected

def find_encryption_key(card_pk, door_pk):
    card_loop_size = find_loop_size(card_pk, 7)
    door_loop_size = find_loop_size(door_pk, 7)
    encryption_key = pow(card_pk, door_loop_size, MAGIC_NUMBER)
    assert encryption_key == pow(door_pk, card_loop_size, MAGIC_NUMBER)
    return encryption_key

@pytest.mark.parametrize('card_pk, door_pk, expected', [
    (5764801, 17807724, 14897079),
])
def test_find_encryption_key(card_pk, door_pk, expected):
    assert find_encryption_key(card_pk, door_pk) == expected

if __name__ == '__main__':
    card_pk = 6929599
    door_pk = 2448427

    encryption_key = find_encryption_key(card_pk, door_pk)

    print(f'encryption_key = {encryption_key}')
