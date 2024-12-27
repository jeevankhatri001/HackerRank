#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time_p = s[-2:]
    time = s[:-2]
    hours,minutes,seconds = map(int,time.split(":"))
    if(time_p == "AM"):
        if hours == 12:
            hour = 0
        elif(time_p=="PM"):
            if time!=12:
                time+=12
    return f"{hours:02}:{minutes:02}:{seconds:02}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
