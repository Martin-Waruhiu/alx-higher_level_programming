#!/usr/bin/python3

""" Module to find a peak in a list of unsorted integers.
Going to utilise a binary search approach.
"""


def find_peak(list_of_integers):
    """Function to find peak in list of integers.
    """
    if not list_of_integers:
        return None

    # initialize low and high indices
    low, high = 0, len(list_of_integers) - 1

    # Binary search loop
    while low < high:
        # calculate the middle index
        mid = (low + high) // 2
        # check if current element is greater than the next element
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # update high to mid, if true
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
