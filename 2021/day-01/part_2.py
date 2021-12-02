from utils import read_input
from part_1 import count_increases

def count_increases_sliding_window(xs):
    # Generate new xs of sliding window of 3
    xs_p = []
    for i in range(len(xs) - 2):
        xs_p.append(xs[i] + xs[i + 1] + xs[i + 2])

    # count_increases on that new xs
    return count_increases(xs_p)

def main():
    xs = read_input()

    print(count_increases_sliding_window(xs))


if __name__ == '__main__':
    main()


def test_sample_input():
    xs = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    assert count_increases_sliding_window(xs) == 5
