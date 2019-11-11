#!/bin/python3

import math
import os
import random
import re
import sys


def stockmax(p):
    c=p[len(p)-1]
    a=0
    for i in range(len(p)-1,-1,-1):
        if c<p[i]:
            c=p[i]
        a+=(c-p[i])
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
