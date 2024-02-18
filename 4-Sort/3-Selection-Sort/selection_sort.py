"""
Selection Sort algorithm
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the Selection Sort algorithm.

    Parameters:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", unsorted_list)
sorted_list = selection_sort(unsorted_list)
print("Sorted List:", sorted_list)
