import sys

class Board:
    def __init__(self, board):
        self.board = board
        self.marked = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]

    def mark(self, v):
        print(f'v={v}')
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == v:
                    print(f'i={i}, j={j}')
                    self.marked[i][j] = True

    def is_winner(self):
        for i in range(5):
            all_row_marked = True
            for j in range(5):
               if self.marked[i][j] == False:
                   all_row_marked = False
                   break
            if all_row_marked:
                return True
        for i in range(5):
            all_col_marked = True
            for j in range(5):
               if self.marked[j][i] == False:
                   all_col_marked = False
                   break
            if all_col_marked:
                return True
        return False

    def unmarked(self):
        numbers = []
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    numbers.append(int(self.board[i][j]))

        return numbers

def print_boards(boards):
    for board in boards:
        print(f'board={board.board}')
        print(f'marked={board.marked}')


def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    random_numbers = lines[0].split(',')
    boards = []
    lines = lines[2:]
    for i in range(0, len(lines), 6):
        board = []
        for j in range(5):
            print(lines[i + j])
            board.append(list(filter(None, lines[i + j].split(' '))))
        boards.append(Board(board))

    return random_numbers, boards

def main():
    random_numbers, boards = read_input()
    print(f'random_numbers={random_numbers}, boards={boards}')

    for n in random_numbers:
        print(f'playing {n}')
        for board in boards:
            board.mark(n)

        print_boards(boards)

        found_winner = False
        for i in range(len(boards)):
            if boards[i].is_winner():
                print(f'winner is {i}')
                found_winner = True
                break

        if found_winner:
            sum_unmarked = sum(boards[i].unmarked())
            print(f'sum_unmarked={sum_unmarked}, n={n}. Multiplication is {sum_unmarked * int(n)}')
            break


if __name__ == '__main__':
    main()
