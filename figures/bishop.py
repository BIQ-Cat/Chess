from figures.figure import Figure


class Bishop(Figure):
    def char(self) -> str:
        return 'B'

    def can_move(self, row, col):
        if self.col == col and self.row == row:
            return False

        if not (0 <= row < 8 and 0 <= col < 8):
            return False

        if abs(self.row - row) == abs(self.col - col):
            return True

        return False
