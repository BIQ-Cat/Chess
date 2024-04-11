from abc import ABCMeta, abstractmethod
from typing import Optional


class Figure(metaclass=ABCMeta):
    def __init__(self, color: int):
        self.color = color

    def get_color(self) -> int:
        """Get figure's color"""
        return self.color

    @abstractmethod
    def char(self) -> str:
        """Get figure's char for outputting"""

    @abstractmethod
    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        """Can figure move on this position?"""

    def can_attack(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        return self.can_move(board, row_from, col_from, row_to, col_to)


class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.is_moving = False

    def char(self):
        return 'R'

    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if row_from != row_to and col_from != col_to:
            return False

        step = 1 if row_to >= row_from else -1
        for row in range(row_from + step, row_to, step):
            if not (board.get_piece(row, col_from) is None):
                return False

        step = 1 if col_to >= col_from else -1
        for col in range(col_from + step, col_to, step):
            if not (board.get_piece(row_from, col) is None):
                return False

        self.is_moving = True
        return True


WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class Pawn(Figure):
    def char(self) -> str:
        return 'P'

    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if col_from != col_to:
            return False  # TODO: en passant is not implemented

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row_from + direction == row_to:
            return True

        if (row_from == start_row
                and row_from + 2 * direction == row_to
                and board.get_piece(row_from + direction, col_from) is None):
            return True

        return False

    def can_attack(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        direction = 1 if (self.color == WHITE) else -1
        return (row_from + direction == row_to
                and (col_from + 1 == col_to or col_from - 1 == col_to))


def coords_are_correct(row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8


class Knight(Figure):
    def char(self) -> str:
        return 'N'

    @staticmethod
    def __can_move_by_shift(row_from: int, col_from: int, row_to: int, col_to: int, shift_row: int, shift_col: int):
        return row_to - shift_row == row_from and col_to - shift_col == col_from or \
            row_to + shift_row == row_from and col_to - shift_col == col_from or \
            row_to - shift_row == row_from and col_to + shift_col == col_from or \
            row_to - shift_row == row_from and col_to - shift_col == col_from

    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        shift_row = 2
        shift_col = 1
        return Knight.__can_move_by_shift(row_from, col_from, row_to, col_to, shift_row, shift_col) or \
            Knight.__can_move_by_shift(row_from, col_from, row_to, col_to, shift_col, shift_row)


class King(Figure):

    def __init__(self, color):
        super().__init__(color)
        self.is_moving = False

    def char(self) -> str:
        return 'K'

    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if abs(row_from - row_to) > 1 or abs(row_from - row_to) > 1:
            return False

        self.is_moving = True
        return True  # TODO: King cannot go on attacking field


class Bishop(Figure):
    def char(self) -> str:
        return 'B'

    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if abs(row_from - row_to) != abs(col_from - col_to):
            return False

        if row_to > row_from and col_to > col_from:
            step_row = 1
            step_col = 1
        elif row_to > row_from and col_to < col_from:
            step_row = 1
            step_col = -1
        elif row_to < row_from and col_to > col_from:
            step_row = -1
            step_col = 1
        else:
            step_row = -1
            step_col = -1

        col = col_from + step_col
        for row in range(row_from + step_row, row_to, step_row):
            if not (board.get_piece(row, col) is None):
                return False

            col += step_col

        if col == col_to:
            return True
        return False


class Queen(Figure):
    def char(self) -> str:
        return 'Q'

    @staticmethod
    def __try_move_as_rook(board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if row_from != row_to and col_from != col_to:
            return False

        step = 1 if row_to >= row_from else -1
        for row in range(row_from + step, row_to, step):
            if not (board.get_piece(row, col_from) is None):
                return False

        step = 1 if col_to >= col_from else -1
        for col in range(col_from + step, col_to, step):
            if not (board.get_piece(row_from, col) is None):
                return False

        return True

    @staticmethod
    def __try_move_as_bishop(board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if abs(row_from - row_to) != abs(col_from - col_to):
            return False

        if row_to > row_from and col_to > col_from:
            step_row = 1
            step_col = 1
        elif row_to > row_from and col_to < col_from:
            step_row = 1
            step_col = -1
        elif row_to < row_from and col_to > col_from:
            step_row = -1
            step_col = 1
        else:
            step_row = -1
            step_col = -1

        col = col_from + step_col
        for row in range(row_from + step_row, row_to, step_row):
            if not (board.get_piece(row, col) is None):
                return False

            col += step_col

        if col == col_to:
            return True
        return False

    def can_move(self, board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if row_from == row_to and col_from == col_to:
            return False
        piece = board.get_piece(row_to, col_to)
        if piece is not None:
            if piece.get_color() == self.color:
                return False

        return Queen.__try_move_as_rook(board, row_from, col_from, row_to, col_to) or \
            Queen.__try_move_as_bishop(board, row_from, col_from, row_to, col_to)


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []  # type: list[list[Figure | None]]

        for _ in range(8):
            self.field.append([None] * 8)

        self.field[1] = [Pawn(WHITE) for _ in range(8)]
        self.field[7] = [Pawn(BLACK) for _ in range(8)]

        self.field[0] = [Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
                         King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)]
        self.field[7] = [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
                         King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        current_color = piece.get_color()
        c = 'w' if current_color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row: int, col: int):
        return self.field[row][col]

    def move_piece(self, row_from: int, col_from: int, row_to: int, col_to: int):

        if not coords_are_correct(row_from, col_from) or not coords_are_correct(row_to, col_to):
            return False
        if row_from == row_to and col_from == col_to:
            return False

        piece = self.field[row_from][col_from]

        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False

        if self.field[row_to][col_to] is None:
            if not piece.can_move(self, row_from, col_from, row_to, col_to):
                return False
        elif self.field[row_to][col_to].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row_from, col_from, row_to, col_to):
                return False
        else:
            return False

        self.field[row_from][col_from] = None
        self.field[row_to][col_to] = piece
        self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if self.current_player_color() == WHITE and row1 != 7:
            return False
        if self.current_player_color() == BLACK and row1 != 0:
            return False
        if char in 'PK':
            return False
        if not self.move_piece(row, col, row1, col1):
            return False
        piece = self.get_piece(row1, col1)
        if piece.char() != 'P':
            return False
        if char == 'Q':
            self.field[row1][col1] = Queen(opponent(self.color))
        elif char == 'B':
            self.field[row1][col1] = Bishop(opponent(self.color))
        elif char == 'R':
            self.field[row1][col1] = Rook(opponent(self.color))
        elif char == 'N':
            self.field[row1][col1] = Knight(opponent(self.color))
        return True

    def castling0(self):
        if self.current_player_color() == WHITE:
            king = self.get_piece(0, 4)  # type: Optional[King]
            rook = self.get_piece(0, 0)  # type: Optional[Rook]
            if king is None or rook is None:
                return False
            if king.char() == 'K' and rook.char() == 'R' and \
                    not king.is_moving and not rook.is_moving:
                if self.get_piece(0, 3) is not None or \
                        self.get_piece(0, 2) is not None or self.get_piece(0, 1) is not None:
                    return False
                self.field[0][4] = None
                self.field[0][0] = None
                self.field[0][2] = king
                self.field[0][3] = rook
                self.color = opponent(self.color)
                return True
        if self.current_player_color() == BLACK:
            king = self.get_piece(7, 4)
            rook = self.get_piece(7, 0)
            if king is None or rook is None:
                return False
            if king.char() == 'K' and rook.char() == 'R' and \
                    not king.is_moving and not rook.is_moving:
                if self.get_piece(7, 3) is not None or \
                        self.get_piece(7, 2) is not None or self.get_piece(7, 1) is not None:
                    return False
                self.field[7][4] = None
                self.field[7][0] = None
                self.field[7][2] = king
                self.field[7][3] = rook
                self.color = opponent(self.color)
                return True

        return False

    def castling7(self):
        if self.current_player_color() == WHITE:
            king = self.get_piece(0, 4)  # type: Optional[King]
            rook = self.get_piece(0, 7)  # type: Optional[Rook]
            if king is None or rook is None:
                return False
            if king.char() == 'K' and rook.char() == 'R' and \
                    not king.is_moving and not rook.is_moving:
                if self.get_piece(0, 5) is not None or self.get_piece(0, 6) is not None:
                    return False
                self.field[0][4] = None
                self.field[0][7] = None
                self.field[0][6] = king
                self.field[0][5] = rook
                self.color = opponent(self.color)
                return True
        if self.current_player_color() == BLACK:
            king = self.get_piece(7, 4)
            rook = self.get_piece(7, 7)
            if king is None or rook is None:
                return False
            if king.char() == 'K' and rook.char() == 'R' and \
                    not king.is_moving and not rook.is_moving:
                if self.get_piece(7, 5) is not None or self.get_piece(7, 6) is not None:
                    return False
                self.field[7][4] = None
                self.field[7][7] = None
                self.field[7][6] = king
                self.field[7][5] = rook
                self.color = opponent(self.color)
                return True

        return False


def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    board = Board()
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


if __name__ == "__main__":
    main()
