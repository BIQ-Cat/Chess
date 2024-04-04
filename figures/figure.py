from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    def __init__(self, row: int, col: int, color: int):
        self.row = row
        self.col = col
        self.color = color

    def get_color(self) -> int:
        """Get figure's color"""
        return self.color

    @abstractmethod
    def char(self) -> str:
        """Get figure's char for outputting"""

    @abstractmethod
    def can_move(self, row: int, col: int) -> bool:
        """Can figure move on this position?"""

    def set_position(self, row: int, col: int):
        """Set figure's position"""
        self.row = row
        self.col = col