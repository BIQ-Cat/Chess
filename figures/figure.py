from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    @abstractmethod
    def get_color(self) -> int:
        """Get figure's color"""

    @abstractmethod
    def char(self) -> str:
        """Get figure's char for outputting"""

    @abstractmethod
    def can_move(self, row: int, col: int) -> bool:
        """Can figure move on this position?"""

    @abstractmethod
    def set_position(self, row: int, col: int):
        """Set figure's position"""
