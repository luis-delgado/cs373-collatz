#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read2 (self) :
        r = StringIO.StringIO("4 8\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  4)
        self.assert_(a[1] == 8)

    def test_read3 (self) :
        r = StringIO.StringIO("24 91\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  24)
        self.assert_(a[1] == 91)

    def test_read4 (self) :
        r = StringIO.StringIO("30 90\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  30)
        self.assert_(a[1] == 90)

    def test_read5 (self) :
        r = StringIO.StringIO("68 72\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  68)
        self.assert_(a[1] == 72)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 5, 6, 9)
        self.assert_(w.getvalue() == "5 6 9\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 4, 5, 6)
        self.assert_(w.getvalue() == "4 5 6\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 3, 8)
        self.assert_(w.getvalue() == "1 3 8\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("10 24\n30 40\n23 65\n90 115\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 24 21\n30 40 107\n23 65 113\n90 115 119\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("50 150\n150 200\n200 250\n250 300\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "50 150 122\n150 200 125\n200 250 128\n250 300 123\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
