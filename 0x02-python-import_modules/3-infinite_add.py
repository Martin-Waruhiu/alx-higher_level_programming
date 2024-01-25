#!/usr/bin/python3
if __name__ == "__main__":
    """infinitite sum"""
import sys
length = len(sys.argv) - 1
sum = 0
for x in range(length):
    sum += int(sys.argv[x + 1])
print("{}".format(sum))
