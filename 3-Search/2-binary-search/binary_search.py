"""
Binary Search Algorithm python implementation
"""

from typing import Optional


def binary_search(items: list[int], target: int) -> Optional[int]:
    """
    Performs a binary search on a sorted list of integers to find the index
    of a given target value.

    Parameters:
        arr (List[int]): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        Optional[int]: The index of the target value in the list, or None
        if the target value is not in the list.
    """
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


items = [i for i in range(10)]

search = int(input("Search an item: "))

SEARCH_RESULT = binary_search(items, search)

if SEARCH_RESULT:
    print(SEARCH_RESULT)
else:
    print("No results found!")
