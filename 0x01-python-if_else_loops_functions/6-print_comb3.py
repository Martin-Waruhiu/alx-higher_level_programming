#!/usr/bin/python3
for x in range(9):
    for y in range(x + 1, 10):
        if x * 10 + y < 89:
            print("{}{}".format(x, y), end=', ')
        else:
            print("{}".format(89))
