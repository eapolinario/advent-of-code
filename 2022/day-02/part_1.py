import sys
from typing import List, Tuple

def parse_line(line: str) -> Tuple:
    play = line.split(' ')
    return (play[0], play[1])

def analyze_play(play: Tuple) -> int:
    # rock
    if play[0] == 'A':
        # rock
        if play[1] == 'X':
            return 1 + 3
        # paper
        elif play[1] == 'Y':
            return 2 + 6
        # scissors
        elif play[1] == 'Z':
            return 3 + 0
    # paper
    if play[0] == 'B':
        # rock
        if play[1] == 'X':
            return 1 + 0
        # paper
        elif play[1] == 'Y':
            return 2 + 3
        # scissors
        elif play[1] == 'Z':
            return 3 + 6
    # scissors
    if play[0] == 'C':
        # rock
        if play[1] == 'X':
            return 1 + 6
        # paper
        elif play[1] == 'Y':
            return 2 + 0
        # scissors
        elif play[1] == 'Z':
            return 3 + 3
    else:
        raise Exception("unreachable")


def main():
    plays = []
    for line in sys.stdin:
        line = line.rstrip()
        plays.append(parse_line(line))

    print(plays)

    answer = 0
    for i, play in enumerate(plays):
        answer += analyze_play(play)
        print(answer)

    print(answer)



if __name__ == '__main__':
    raise SystemExit(main())
