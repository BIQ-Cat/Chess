import basic.board
from figures.figure import Figure
from basic import color


class Pawn(Figure):
    def char(self) -> str:
        return 'P'

    def can_move(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if col_from != col_to:
            return False  # TODO: en passant is not implemented

        if self.color == color.WHITE:
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

    def can_attack(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        direction = 1 if (self.color == color.WHITE) else -1
        return (row_from + direction == row_to
                and (col_from + 1 == col_to or col_from - 1 == col_to))
