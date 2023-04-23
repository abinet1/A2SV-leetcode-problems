#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    
    re = a
    counter = 0
    
    for i in range(1,len(re),1):
        
        for j in range(0, len(re)-1):
            if (re[j] > re[j + 1]):
                counter += 1
                
                c = re[j] 
                re[j] = re[j+1]
                re[j+1] = c
    
    print("Array is sorted in",counter,"swaps.")
    print("First Element:",re[0])
    print("Last Element:",re[len(re)-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
