import figure


class Rook(figure.Figure):
    def char(self):
        return 'R'

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False

        return True
    