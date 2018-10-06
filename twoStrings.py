#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    substrings = {}
    for letter in s1:
        if not letter in substrings:
            substrings[letter] = True
    for letter in s2:
        if letter in substrings:
            return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
