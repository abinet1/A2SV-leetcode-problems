#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:  
        if grade>=38:
            if grade%5>=3:
                g=grade+(5-(grade%5))
                result.append(g)
            else:
                result.append(grade)
        else: 
            result.append(grade)
    return result

if __name__ == '__main__':
    grades = [73,67,38,33]

    result = gradingStudents(grades)

    print(result)
