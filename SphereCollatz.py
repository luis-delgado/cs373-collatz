#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
import sys

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
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
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    table = [1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 10, 18, 18, 5, 13, 21, 21, 8]

    if i <= j :
        temp = j / 2
        if  temp > i:
            i = temp
        myMin = i
        myMax = j

    else :
        temp = i / 2
        if  temp > j:
            j = temp
        myMin = j
        myMax = i

    trueMax = 1

    for z in range(myMin, myMax+1):
    
        currentCycleLength = 0
    
        while z != 1:

            if z < 20:
                
                #value is already in cache
                currentCycleLength = currentCycleLength + table[z - 1]
                z = 1
            
            else:
            
                #compute
                if (z % 2) != 1:
            
                    currentCycleLength = currentCycleLength + 1
                    z = (z / 2)
            
                else:
            
                    currentCycleLength = currentCycleLength + 2
                    z = ((3 * z) + 1) / 2
        
        if currentCycleLength > trueMax :
            trueMax = currentCycleLength;

    assert trueMax > 0
    return trueMax

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
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

