#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    count_in_word = 0
    count_in_word = s.count('a')

    word_size = len(s)

    number_of_word_repetitions = n // word_size
    repetitions = number_of_word_repetitions * count_in_word

    number_of_missing_letters = n - (number_of_word_repetitions * word_size)

    repetitions += s[:number_of_missing_letters].count('a')

    return repetitions

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
