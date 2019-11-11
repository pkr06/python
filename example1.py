#!/bin/python3

import math
import os
import random
import re
import sys


def angryChildren(k, packets):
    packets.sort()

    sum_ = 0
    difference = 0

    for i in range(k - 1, -1, -1):
        difference = difference + abs(packets[i] * (k - 1 - i) - sum_)

        sum_ = sum_ + packets[i]

    min_diff = difference

    for i in range(k, len(packets)):
        sum_ = sum_ - packets[i - k]

        difference = difference - abs(sum_ - packets[i - k] * (k - 1))

        difference = difference + abs(sum_ - (k - 1) * packets[i])

        if (difference < min_diff):
            min_diff = difference

        sum_ = sum_ + packets[i]

    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    packets = []

    for _ in range(n):
        packets_item = int(input())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
