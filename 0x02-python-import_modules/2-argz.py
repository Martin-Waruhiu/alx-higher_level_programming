#!/usr/bin/python3
if __name__ == "__main__":
    """dynamic script"""
import sys
length = len(sys.argv) - 1
if length == 1:
    print("0 arguments.")
elif length == 2:
    print("1 argument:")
    print("1:{}".format(sys.argv[1]))
else:
    print("{} arguments".format(length))
    for x in range(length):
        print("{}:{}".format(x + 1, sys.argv[x + 1]))
