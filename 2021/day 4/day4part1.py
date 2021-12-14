class Board:

    def __init__(self, board):
        self.board = board
        self.won_at = None
        self.winning_board = None

    def mark(self, number):
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board)):
                cell = self.board[row_index][col_index]
                if cell == number:
                    if cell == 0:
                        self.board[row_index][col_index] = None
                    else:
                        self.board[row_index][col_index] = -cell
                    break
        won = self.has_won()
        if won and self.winning_board is None:
            self.winning_board = [row[:] for row in self.board]
        return won

    def sum_of_won_board(self):
        sum = 0
        for row in self.winning_board:
            for col in row:
                if col is not None and col >= 0:
                    sum += col
        return sum

    def sum_of_unmarked(self):
        sum = 0
        for row in self.board:
            for col in row:
                if col is not None and col >= 0:
                    sum += col
        return sum

    def has_won(self):
        for row_index in range(len(self.board)):
            won = True
            for col_index in range(len(self.board)):
                cell = self.board[row_index][col_index]
                if cell is not None and cell >= 0:
                    won = False
            if won:
                return True
        for row_index in range(len(self.board)):
            won = True
            for col_index in range(len(self.board)):
                cell = self.board[col_index][row_index]
                if cell is not None and cell >= 0:
                    won = False
            if won:
                return True
        return False

    def print(self):
        for row in self.board:
            print("")
            for col in row:
                print(col, end=" ")
        print()

def giant_squid_pt1():
    with open("2021/day4/nums.txt", 'r') as f:
        lines = f.readlines()
        numbers = [int(line.strip()) for line in lines[0].split(",")]

        boards = []
        board = []
        for line in lines[1:]:

            if line.strip() == "":
                boards.append(Board(board))
                board = []
            else:
                line = list(filter(lambda c: c != "", [l.strip() for l in line.split(" ")]))
                parsed_lines = [int(c) for c in line]
                board.append(parsed_lines)

        boards.append(Board(board))

        for number in numbers:
            for board in boards:
                if board.mark(number):
                    return number * board.sum_of_unmarked()


print(f'Part one: {giant_squid_pt1()}')