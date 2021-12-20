import copy
import pytest
from typing import List

def step(fish: List[int]) -> List[int]:
    new_fish = []
    added_fish = 0
    for n in fish:
        if n == 0:
            added_fish += 1
            new_fish.append(6)
        else:
            new_fish.append(n - 1)
    for _ in range(added_fish):
        new_fish.append(8)

    return new_fish

@pytest.mark.parametrize('fish, expected_fish', [
    (
        [3, 4, 3, 1, 2],
        [2, 3, 2, 0, 1],
    ),
    (
        [2, 3, 2, 0, 1],
        [1, 2, 1, 6, 0, 8],
    ),
])
def test_step(fish, expected_fish):
    assert step(fish) == expected_fish


def test_sample_input():
    fish = [3, 4, 3, 1, 2]
    for _ in range(18):
        fish = step(fish)

    assert fish == [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    assert len(fish) == 26

    for _ in range(80 - 18):
        fish = step(fish)

    assert len(fish) == 5934


if __name__ == '__main__':
    # fish = [3, 4, 3, 1, 2]
    fish = [1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3]
    for _ in range(80):
        fish = step(fish)

    print(f'total fish is {len(fish)}')
