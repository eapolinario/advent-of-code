import copy
import pytest
from collections import Counter
from typing import List

def step(fish: Counter) -> Counter:
    new_fish = Counter()
    for i, v in fish.items():
        if i == 0:
            new_fish[8] += v
            new_fish[6] += v
        else:
            new_fish[i - 1] += v

    return new_fish

@pytest.mark.parametrize('fish, expected_fish', [
    (
        Counter([3, 4, 3, 1, 2]),
        Counter([2, 3, 2, 0, 1]),
    ),
    (
        Counter([2, 3, 2, 0, 1]),
        Counter([1, 2, 1, 6, 0, 8]),
    ),
])
def test_step(fish, expected_fish):
    assert step(fish) == expected_fish


def test_sample_input():
    fish = Counter([3, 4, 3, 1, 2])
    for _ in range(18):
        fish = step(fish)

    assert fish == Counter([6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8])
    assert sum(fish.values()) == 26

    for _ in range(80 - 18):
        fish = step(fish)

    assert sum(fish.values()) == 5934


if __name__ == '__main__':
    fish = Counter([1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3])
    for _ in range(256):
        fish = step(fish)

    print(f'total fish is {sum(fish.values())}')
