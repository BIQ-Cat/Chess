import color
from figures.figure import Figure


def coords_are_correct(row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = color.WHITE
        self.field = []  # type: list[list[Figure | None]]
        for row in range(8):
            self.field.append([None] * 8)
        self.field[1][4] = Pawn(1, 4, color.WHITE)

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
