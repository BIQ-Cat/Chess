import basic.board
from figures.figure import Figure


class Bishop(Figure):
    def char(self) -> str:
        return 'B'

    def can_move(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if abs(row_from - row_to) != abs(col_from - col_to):
            return False

        if row_to > row_from and col_to > col_from:
            step_row = 1
            step_col = 1
        elif row_from > row_from and col_to < col_from:
            step_row = 1
            step_col = -1
        elif row_from < row_from and col_to > col_from:
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
