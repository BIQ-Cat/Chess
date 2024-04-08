import figures.figure


class Queen(figures.figure.Figure):
    def char(self) -> str:
        return 'Q'

    def can_move(self, row: int, col: int) -> bool:
        if self.col == col and self.row == row:
            return False
        if not (0 <= row < 8 and 0 <= col < 8):
            return False

        if abs(self.row - row) == abs(self.col - col):
            return True
        if not (self.row != row and self.col != col):
            return True

        return False
