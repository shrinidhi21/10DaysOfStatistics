#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def get_median(arr):
    mid = len(arr)//2
    
    if len(arr)%2:
        return arr[mid]
    else:
        return (sum(arr[mid-1:mid+1])/2)
    
def quartiles(arr):
    # Write your code here
    #arr = sorted(arr)
    mid = len(arr)//2
    #q2 = get_median(arr)
    
    if len(arr)%2:
        q1 = get_median(arr[:mid])
        q3 = get_median(arr[mid+1:])
    else:
        q1 = get_median(arr[:mid])
        q3 = get_median(arr[mid:])
        
    return q1,q3

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    
    arr = [i for l in ([v]*f for v, f in zip(values, freq)) for i in l]
    arr = sorted(arr)
    
    q1,q3 = quartiles(arr)
    #print(q1)
    #print(q3)
    res = round(float(q3-q1), 1)
    print(res)
    
            

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
