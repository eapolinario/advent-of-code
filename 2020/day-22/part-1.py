#!/usr/bin/env python3

def parse_cards(lines):
    return [int(n) for n in lines[1:]]

if __name__ == '__main__':
    import sys
    lines = []
    players_cards = []
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
           players_cards.append(parse_cards(lines))
           lines = []
        else:
            lines.append(line)
    players_cards.append(parse_cards(lines))

    while len(players_cards[0]) != 0 and len(players_cards[1]) != 0:
        print(f'players_cards={players_cards}')
        top_0 = players_cards[0][0]
        top_1 = players_cards[1][0]
        del players_cards[0][0]
        del players_cards[1][0]

        if top_0 > top_1:
            players_cards[0].append(top_0)
            players_cards[0].append(top_1)
        elif top_1 > top_0:
            players_cards[1].append(top_1)
            players_cards[1].append(top_0)

    print(f'players_cards={players_cards}')

    winner = None
    if len(players_cards[0]) > 0:
        winner = players_cards[0]
    else:
        winner = players_cards[1]

    answer = 0
    for i, v in enumerate(reversed(winner)):
        answer += (i + 1)*v

    print(f'final answer is {answer}')
