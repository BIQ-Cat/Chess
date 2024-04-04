import color
from figures.figure import Figure
from figures.knight import Knight
from figures.pawn import Pawn
from figures.rook import Rook


def coords_are_correct(row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = color.WHITE
        self.field = []  # type: list[list[Figure | None]]

        for _ in range(8):
            self.field.append([None] * 8)

        self.field[1] = [Pawn(1, i, color.WHITE) for i in range(8)]
        self.field[7] = [Pawn(7, i, color.BLACK) for i in range(8)]

        self.field[0][0] = Rook(0, 0, color.WHITE)
        self.field[0][1] = Knight(0, 1, color.WHITE)
        self.field[0][6] = Knight(0, 6, color.WHITE)
        self.field[0][7] = Rook(0, 7, color.WHITE)

        self.field[7][0] = Rook(7, 0, color.BLACK)
        self.field[0][1] = Knight(0, 1, color.BLACK)
        self.field[0][6] = Knight(0, 6, color.BLACK)
        self.field[7][7] = Rook(7, 7, color.BLACK)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        current_color = piece.get_color()
        c = 'w' if current_color == color.WHITE else 'b'
        return c + piece.char()

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
        if not piece.can_move(row_to, col_to):
            return False
        self.field[row_from][col_from] = None
        self.field[row_to][col_to] = piece
        piece.set_position(row_to, col_to)
        self.color = color.opponent(self.color)
        return True
