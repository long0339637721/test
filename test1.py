#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    arr = [*s[0], *s[1], *s[2]]
    minCost = 8 * 9
    for p in itertools.permutations(range(1, 10)):
        if sum(p[0:3]) == 15 and sum(p[3:6]) == 15 and sum(p[0::3]) == 15 and sum(p[1::3]) == 15 and sum(p[0::4]) == 15 and sum(p[2:7:2]) == 15:
            minCost = min(minCost, sum(abs(p[i] - arr[i]) for i in range(9)))
    return minCost
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
