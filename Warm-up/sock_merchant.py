#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    nmbr_of_pair = 0
    prv=False
    ar.sort()
    for i in ar:
        if(prv==i):
            nmbr_of_pair+=1
            prv = False
        else:
            prv = i
    return nmbr_of_pair

if (__name__ == '__main__'):

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
