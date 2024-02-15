"""
Insertion sort Python code
"""


def insertion_sort(items: list[int]) -> list[int] | None:
    """
    Insertion Sort algorithm

    Parameters:
    - items (list[int]): list to be sorted

    Return:
    - list[int]: Sorted list
    """
    size = len(items)

    for i in range(1, size):
        temp = items[i]
        j = i - 1
        while j >= 0 and items[j] > temp:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = temp
    return items


if __name__ == "__main__":
    items = [11, 15, 13, 7, 9, 16, 19, 25, 17, 46, 99, 105]
    print(f"Unsorted List: {items}")
    print("Sorted List", insertion_sort(items))
