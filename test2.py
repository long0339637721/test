#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'buildString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. STRING s
#

def foo(s):
    n = len(s)
    z = [0] * n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

def buildString(a, b, s):
    # Write your code here
    n = len(s)
    # minCharsToSub = b // a + 1
    minCost = [float('inf')] * (n + 1)
    minCost[0] = 0
    for i in range(1, n + 1):
        minCost[i] = minCost[i - 1] + a
        # z = foo(s[:i])
        for j in range(i):
            if s[j:i] in s[:j]:
                minCost[i] = min(minCost[i], minCost[j] + b)
    print(minCost)
    return minCost[n]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        s = input()

        result = buildString(a, b, s)
        
        fptr.write(str(result) + '\n')

    fptr.close()
