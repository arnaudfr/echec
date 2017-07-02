# -*- coding: utf-8 -*-

import unittest
from src.game import Game
from src.chessPiece import ChessPiece

class TestChessPiece(unittest.TestCase):

    def test_CreatePiece(self):
        piece = ChessPiece([3, 1], True)
        self.assertIsNotNone(piece)

    def test_CreateNegativePattern(self):
        piece = ChessPiece([-1000, -1000000], False)
        self.assertRaises(excClass=ValueError)
        self.assertEqual(ValueError.message, 'negativePattern')
