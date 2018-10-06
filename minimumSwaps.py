#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    swaps = 0
    sorted_arr = sorted(arr)
    index_dict = {v: i for i, v in enumerate(arr)}
    for i, value in enumerate(arr):
        found_index = index_dict[sorted_arr[i]]
        if sorted_arr[i] != value:
            arr[i], arr[found_index] = arr[found_index], arr[i]
            index_dict[value], index_dict[sorted_arr[i]] = found_index, i
            swaps += 1

    return swaps

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    # fptr.write(str(res) + '\n')

    # fptr.close()

    print(res)
