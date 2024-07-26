"""
Python Merge Sort using Github Copilot
"""

# Write a function that takes a list and sorts it using merge sort algorithm
# Merge sort is a divide and conquer algorithm.
# It works as follows:
# 1. Divide the unsorted list into n sublists, each containing one element
# 2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining


def merge_sort(arr):
    """
    Merge Sort algorithm
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


UNSORTED_LIST: list[int] = [12, 7, 18, 9, 16, 22, 13, 15, 98, 76, 28]

SORTED_LIST = merge_sort(UNSORTED_LIST)

print(f"Sorted list: {SORTED_LIST}")
