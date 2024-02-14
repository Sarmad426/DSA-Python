"""
Bubble Sort algorithm
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the Bubble Sort algorithm.

    Parameters:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize the sorting process by breaking the loop if no swaps occur
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break
    return arr


unsorted_list = [11, 15, 13, 7, 9, 16, 19, 25, 17, 46, 99, 105]
print("Unsorted List:", unsorted_list)
sorted_list = bubble_sort(unsorted_list)
print("Sorted List:", sorted_list)
