import math
import os
import random
import re
import sys
from collections import Counter


def most_common(string_):
    counter = Counter()
    for i in string_:
        counter[i] += 1
    result = []
    for i in counter:
        result.append((counter[i], i))
    result.sort(key=lambda x: (-x[0], x[1]))
    for i in range(3):
        print result[i][1], result[i][0]


if __name__ == '__main__':
    s = raw_input()
    most_common(s)

