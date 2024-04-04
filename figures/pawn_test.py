import unittest


class TestPawn(unittest.TestCase):
    def __init__(self):
        self.pawn = Pawn()
        super().__init__()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
