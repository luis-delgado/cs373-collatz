#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

 # ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
a is an array of int
return true if that succeeds, false otherwise
"""
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert i > 0
    assert j > 0

    if i < j:
        list = [None] * (j - i + 1)
        min = i
        max = j

    elif j < i:
        list = [None] * (i - j + 1)
        min = j
        max = i

    else:
        list = [None]
        min = i
        max = i

    finalMax = -1

    for z in range (min, max + 1):

        cycleLength = 0
        temp = z
        exit = 0

        while temp != 1 and exit == 0:

            if (temp - min) >= 0 and (temp-min) < len(list) and list[temp - min] != None:
                cycleLength += list[temp - min]
                exit = 1

            else:
                if temp % 2 == 0:
                    temp = temp / 2

                else:
                    temp = temp * 3
                    temp = temp + 1

                cycleLength = cycleLength + 1

        if exit == 0:
            cycleLength = cycleLength + 1

        list[z-min] = cycleLength

        if cycleLength > finalMax:
            finalMax = cycleLength

    return finalMax


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
prints the values of i, j, and v
w is a writer
i is the beginning of the range, inclusive
j is the end of the range, inclusive
v is the max cycle length
"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)


collatz_solve(sys.stdin, sys.stdout)
