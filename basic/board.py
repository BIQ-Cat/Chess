import color
from figures.bishop import Bishop
from figures.figure import Figure
from figures.king import King
from figures.knight import Knight
from figures.pawn import Pawn
from figures.queen import Queen
from figures.rook import Rook


def coords_are_correct(row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = color.WHITE
        self.__field = []  # type: list[list[Figure | None]]

        for _ in range(8):
            self.__field.append([None] * 8)

        self.__field[1] = [Pawn(color.WHITE) for _ in range(8)]
        self.__field[7] = [Pawn(color.BLACK) for _ in range(8)]

        self.__field[0] = [Rook(color.WHITE), Knight(color.WHITE), Bishop(color.WHITE), Queen(color.WHITE),
                           King(color.WHITE), Bishop(color.WHITE), Knight(color.WHITE), Rook(color.WHITE)]
        self.__field[7] = [Rook(color.BLACK), Knight(color.BLACK), Bishop(color.BLACK), Queen(color.BLACK),
                           King(color.BLACK), Bishop(color.BLACK), Knight(color.BLACK), Rook(color.BLACK)]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.__field[row][col]
        if piece is None:
            return '  '
        current_color = piece.get_color()
        c = 'w' if current_color == color.WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row: int, col: int):
        return self.__field[row][col]

    def move_piece(self, row_from: int, col_from: int, row_to: int, col_to: int):

        if not coords_are_correct(row_from, col_from) or not coords_are_correct(row_to, col_to):
            return False
        if row_from == row_to and col_from == col_to:
            return False

        piece = self.__field[row_from][col_from]

        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False

        if self.__field[row_to][col_to] is None:
            if not piece.can_move(self, row_from, col_from, row_to, col_to):
                return False
        elif self.__field[row_to][col_to].get_color() == color.opponent(piece.get_color()):
            if not piece.can_attack(self, row_from, col_from, row_to, col_to):
                return False
        else:
            return False

        self.__field[row_from][col_from] = None
        self.__field[row_to][col_to] = piece
        self.color = color.opponent(self.color)
        return True
