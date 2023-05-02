#!/bin/bash
# a function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):

     left = 0
    right = len(list_of_integers) - 1

    # Continue searching until the range is empty
    while left < right:
        # Calculate the midpoint of the range
        mid = (left + right) // 2

        # If the midpoint is greater than both its neighbors, it's a peak
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]

        # If the left neighbor is greater than the midpoint, search the left half
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
