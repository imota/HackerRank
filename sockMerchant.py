#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    pairs = {}
    for element in ar:
        if element in pairs:
            pairs[element] += 1
        else:
            pairs[element] = 1

    number_of_pairs = 0

    for values in pairs.values():
        number_of_pairs = number_of_pairs + (values // 2)

    return number_of_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
