from figures.figure import Figure


def coords_are_correct(row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8


class Knight(Figure):
    def char(self) -> str:
        return 'N'

    def can_move_by_shift(self, row, col, shift_row, shift_col):
        return row - shift_row == self.row and col - shift_col == self.col or \
                row + shift_row == self.row and col - shift_col == self.col or \
                row - shift_row == self.row and col + shift_col == self.col or \
                row - shift_row == self.row and col - shift_col == self.col

    def can_move(self, row: int, col: int) -> bool:
        if not coords_are_correct(row, col):
            return False
        shift_row = 2
        shift_col = 1
        return self.can_move_by_shift(row, col, shift_row, shift_col) or \
            self.can_move_by_shift(row, col, shift_col, shift_row)
