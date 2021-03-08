#!/usr/bin/env python3

from copy import copy

def parse_cards(lines):
    return [int(n) for n in lines[1:]]

def play_game(player_1, player_2, rounds: set):
    while len(player_1) and len(player_2):
        if (1, tuple(player_1), 2, tuple(player_2)) in rounds:
            return 1
        rounds.add((1, tuple(player_1), 2, tuple(player_2)))

        top_1 = player_1[0]
        top_2 = player_2[0]
        del player_1[0]
        del player_2[0]

        if len(player_1) >= top_1 and len(player_2) >= top_2:
            winner = play_game(copy(player_1[:top_1]), copy(player_2[:top_2]), set())
        else:
            if top_1 > top_2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            player_1.append(top_1)
            player_1.append(top_2)
        else:
            player_2.append(top_2)
            player_2.append(top_1)

    if len(player_1) > 0:
        return 1
    else:
        return 2

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

    winner = play_game(players_cards[0], players_cards[1], set())

    print(f'player_cards={players_cards}')

    answer = 0
    for i, v in enumerate(reversed(players_cards[winner - 1])):
        answer += (i + 1)*v

    print(f'final answer is {answer}')
