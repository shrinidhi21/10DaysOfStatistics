#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def get_median(arr):
    mid = len(arr)//2
    
    if len(arr)%2:
        return arr[mid]
    else:
        return round(sum(arr[mid-1:mid+1])/2)
    
def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    mid = len(arr)//2
    q2 = get_median(arr)
    
    if len(arr)%2:
        q1 = get_median(arr[:mid])
        q3 = get_median(arr[mid+1:])
    else:
        q1 = get_median(arr[:mid])
        q3 = get_median(arr[mid:])
        
    return q1,q2,q3
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
