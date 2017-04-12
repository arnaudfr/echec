# -*- coding: utf-8 -*-

import unittest
from src.main import Main

class TestMain(unittest.TestCase):

    def test_sayHello(self):
        main = Main()
        self.assertEqual(main.sayHello(), "hello world")