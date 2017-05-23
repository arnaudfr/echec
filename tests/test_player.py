# -*- coding: utf-8 -*-

from src.constant import *
import unittest
from src.game import Game
from src.player import Player

class TestPlayer(unittest.TestCase):

    # Init player
    def test_initPlayer(self):
        player = Player(0)
        self.assertEqual(player._id, 0)

    # Init invalid player
    def test_initInvalidPlayer(self):
        player = Player(-12)
        self.assertIsNone(player)
