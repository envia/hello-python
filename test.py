#!/usr/bin/env python
# -*- coding: utf-8; -*- # PEP 263
# vim: set fileencoding=utf-8 tabstop=8 expandtab shiftwidth=4 softtabstop=4: # PEP 8

import unittest

class TestHello(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(1+1, 2)

    def test_random(self):
        import random
        import sys
        random.seed(0)
        r = random.randint(0, 9)
        if sys.version_info[0] == 2:
            self.assertEqual(r, 8)
        if sys.version_info[0] == 3:
            self.assertEqual(r, 6)

    def test_tempfile(self):
        import filecmp
        import shutil
        import tempfile
        s = tempfile.mkdtemp()
        t = tempfile.mkdtemp()
        with open(s + "/hello", "w") as f:
            f.write("hello\n")
        shutil.copy(s + "/hello", t + "/hello")
        self.assertTrue(filecmp.cmp(s + "/hello", t + "/hello"))
        shutil.rmtree(s)
        shutil.rmtree(t)

if __name__ == '__main__':
    unittest.main()
