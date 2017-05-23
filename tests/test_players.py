# -*- coding: utf-8 -*-

from src.constant import *
import unittest
from src.game import Game

class TestPlayers(unittest.TestCase):

    # Init a player
    def test_initPlayer(self):
        game = Game()
        player = game.createPlayer()
        self.assertEqual(player._id, 0)

    # Get a valid player
    def test_getPlayer(self):
        game = Game()
        player0 = game.createPlayer()
        player1 = game.createPlayer()
        self.assertEqual(player0._id, 0)
        self.assertEqual(player1._id, 1)
        playerN = game.getPlayer(0)
        self.assertEqual(playerN._id, 0)
        playerN = game.getPlayer(1)
        self.assertEqual(playerN._id, 1)

    # Get an invalid player
    def test_getUnvalidPlayer(self):
        game = Game()
        player = game.getPlayer(0)
        self.assertIsNone(player)

    # Set to many players
    def test_tooManyPlayers(self):
        game = Game()
        for i in range(1,5):
            game.createPlayer()
        player = getPlayer(2)
        self.assertEqual(player._id, 2)
        player = getPlayer(5)
        # self.assertIsNone(player)
        self.assertRaises(ValueError)
