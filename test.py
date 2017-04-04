#!/usr/bin/env python
# -*- coding: utf-8; -*- # PEP 263
# vim: set fileencoding=utf-8 tabstop=8 expandtab shiftwidth=4 softtabstop=4: # PEP 8

import unittest

class TestHello(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(1, 2)

    def test_random(self):
        import random
        random.seed(0)
        r = random.randint(0, 9)
        self.assertEqual(r, 8)

if __name__ == '__main__':
    unittest.main()
