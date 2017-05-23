# -*- coding: utf-8 -*-

from src.constant import *
import unittest
from src.game import Game

class TestPlayers(unittest.TestCase):

    # Init a player
    def test_initPlayer(self):
        game = Game()
        player = game.createPlayer()
        self.assertEqual(player.id, 0)

    # Get a valid player
    def test_getPlayer(self):
        game = Game()
        player0 = game.createPlayer()
        player1 = game.createPlayer()
        self.assertEqual(player0.id, 0)
        self.assertEqual(player1.id, 1)
        playerN = game.getPlayer(0)
        self.assertEqual(playerN.id, 0)
        playerN = game.getPlayer(1)
        self.assertEqual(playerN.id, 1)

    # Get an invalid player
    def test_unvalidPlayer(self):
        game = Game()
        player = game.getPlayer(0)
        self.assertIsNone(player)
