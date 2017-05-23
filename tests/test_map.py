# -*- coding: utf-8 -*-

from src.constant import *
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

    # Too small grid
    def test_tooSmallMap(self):
        game = Game()
        map = game.setGrid(MINGRID - 1)
        self.assertEqual(0, map)

    # Too big grid
    def test_tooBigMap(self):
        game = Game()
        map = game.setGrid(MAXGRID + 1)
        self.assertEqual(0, map)

    # Negative grid
    def test_negativeMap(self):
        game = Game()
        map = setGrid(-12)
        self.assertEqual(0, map)
