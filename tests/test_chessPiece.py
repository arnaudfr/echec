import unittest
from src.game import Game
from src.chessPiece import ChessPiece

class TestChessPiece(unittest.TestCase):

    def test_CreatePiece(self):
        piece = ChessPiece([3, 1], True)
        self.assertIsNotNone(piece)

    def test_CreateInvalidPiece(self):
        piece = ChessPiece([-1000, -1000000], False)
        self.assertIsNone(piece)