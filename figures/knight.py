import basic.board
from figures.figure import Figure


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

    def can_move(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:

        shift_row = 2
        shift_col = 1
        return Knight.__can_move_by_shift(row_from, col_from, row_to, col_to, shift_row, shift_col) or \
            Knight.__can_move_by_shift(row_from, col_from, row_to, col_to, shift_col, shift_row)
