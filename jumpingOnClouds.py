#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jumps = 0
    last_cloud = len(c) - 1

    cloud = 0
    while cloud < last_cloud:
        jumps += 1
        if cloud + 2 <= last_cloud and c[cloud + 2] == 1:
            cloud = cloud + 1
        else:
            cloud = cloud + 2
    return jumps


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
