from utils import read_input


def count_increases(xs):
    increases = -1
    previous = 0
    for i in xs:
        if i > previous:
            increases += 1
        previous = i

    return increases

def main():
    xs = read_input()

    print(count_increases(xs))


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
    assert count_increases(xs) == 7
