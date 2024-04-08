import figures.figure


class King(figures.figure.Figure):
    def char(self) -> str:
        return 'K'

    def can_move(self, row: int, col: int) -> bool:
        if abs(self.row - row) == 1 or abs(self.col - col) == 1:
            return True

        return False
