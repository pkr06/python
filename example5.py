#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

def nonDivisibleSubset(k, s):
    result = 0
    s = Counter(map(lambda x: x % k, s))
    for i in range(1, k // 2 + 1):
        j = k - i
        if i == j and s[i] > 0:
            result += 1
        elif s[i] > s[j]:
            result += s[i]
        else:
            result += s[j]
    if s[0] > 0:
        result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
