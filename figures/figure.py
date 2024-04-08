from abc import ABCMeta, abstractmethod

import basic.board


class Figure(metaclass=ABCMeta):
    def __init__(self, color: int):
        self.color = color

    def get_color(self) -> int:
        """Get figure's color"""
        return self.color

    @abstractmethod
    def char(self) -> str:
        """Get figure's char for outputting"""

    @abstractmethod
    def can_move(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        """Can figure move on this position?"""

    def can_attack(self, board: basic.board.Board, row_from: int, col_from: int, row_to: int, col_to: int) -> bool:
        return self.can_move(board, row_from, col_from, row_to, col_to)
