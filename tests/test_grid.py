# -*- coding: utf-8 -*-

import unittest
from src.game import Game

class TestGrid(unittest.TestCase):

    # Valid grid initialization test
    def test_initGrid(self):
        game = Game()
        grid = game.setGrid(10)
        self.assertEqual(10, len(grid))
        for row in grid:
            self.assertEqual(10, len(row))
            for cel in row:
                self.assertEqual(0, cel)