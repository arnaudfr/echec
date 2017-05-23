# -*- coding: utf-8 -*-

import unittest
from src.game import Game

class TestMap(unittest.TestCase):

    # Valid grid initialization test
    def test_initMap(self):
        game = Game()
        map = game.setGrid(10)
        self.assertEqual(10, len(map))
        for row in map:
            self.assertEqual(10, len(row))
            for cel in row:
                self.assertEqual(0, cel)