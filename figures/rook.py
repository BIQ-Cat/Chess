import basic.board
import figure


class Rook(figure.Figure):
    def char(self):
        return 'R'

    def can_move(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        if row_from != row_to and col_from != col_to:
            return False

        step = 1 if row_to >= row_from else -1
        for row in range(row_from + step, row_to, step):
            if not (board.get_piece(row, col_from) is None):
                return False

        step = 1 if col_to >= col_from else -1
        for col in range(col_from + step, col_to, step):
            if not (board.get_piece(row_from, col) is None):
                return False
