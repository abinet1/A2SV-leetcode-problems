#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def display(ar):
    for j in ar:
        print(j,end=" ")
    print("")
    
def insertionSort1(n, arr):
    ar = arr
    s = ar[-1]
    for i in range(n-2,-1,-1):
        if(ar[i]>s):
            ar[i+1]=ar[i]
            display(ar)
        elif(ar[i]<s):
            ar[i+1]=s
            display(ar)
            return
    ar[0]=s
    display(ar)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
