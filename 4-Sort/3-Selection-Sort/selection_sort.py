"""
Selection Sort algorithm
"""


def selection_sort(items: list[int]):
    """
    Sorts the list using selection sort algorithm

    Parameter and return type:
    - takes a list of integers as a parameters
    - sorts the list and returns it
    """
    for i in range(len(items) - 1):
        min_num = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_num]:
                min_num = j
        items[i], items[min_num] = items[min_num], items[i]

    return items


items = [6, 2, 11, 9, 27, 16, 23]

print(f"Unsorted list: {items}")

sorted_items = selection_sort(items)

print(f"Sorted list: {sorted_items}")
