#!/bin/env python3

import sys

tosum = []
sum = 0

if __name__ == '__main__':
    data_file = sys.argv[1]
    contents = open(data_file)
    lines = contents.readlines()
    for line in lines:
        line = line.replace("\n", "")
        tosum.append(line)
    
for num in tosum:
    try:
        num = float(num)
        sum += num
    except ValueError:
        pass
print(sum)
