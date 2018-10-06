#!/bin/python3

import math
import os
import random
import re
import sys
from math import factorial

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    substrings = {}
    number_of_substrings = 0

    for start in range(0, len(s)):
        for substring_size in range(1, len(s)):
            if (start + substring_size < len(s) + 1):
                substring = str(sorted(s[start:start + substring_size]))
                if not substring in substrings:
                    substrings[substring] = 1
                else:
                    substrings[substring] += 1

    for value in substrings.values():
        if value > 1:
            number_of_substrings += factorial(value) / \
                (2 * factorial(value - 2))

    return int(number_of_substrings)

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
