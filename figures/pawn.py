from figures.figure import Figure
from basic import color


class Pawn(Figure):
    def char(self) -> str:
        return 'P'

    def can_move(self, row: int, col: int) -> bool:
        if self.col != col:
            return False  # TODO: en passant is not implemented

        if self.color == color.WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if self.row + direction == row:
            return True

        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False
