"""
Linear Search Algorithm python implementation
"""

from typing import Optional


def linear_search(items: list[int], target: int) -> Optional[int]:
    """
    Linear Search Algorithm

    Parameters:
    - items (list[int]): list of items to search
    - target (int) : target value to search

    Returns:
    int: if target exist in items, returns its index, otherwise returns -1
    """
    for item in items:
        if item == target:
            return item
    return None


items = [11, 35, 23, 45, 16, 29]

search = int(input("Search for an item: "))

SEARCH_RESULT = linear_search(items, search)
if SEARCH_RESULT:
    print(SEARCH_RESULT)
else:
    print("Item not found:")
