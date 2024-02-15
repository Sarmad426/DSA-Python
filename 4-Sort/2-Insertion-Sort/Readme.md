# Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted list one item at a time. It works by iteratively taking an element from the unsorted part of the list and inserting it into its correct position in the sorted part of the list.

## Algorithm Steps

1. Start with the second element (index 1) and consider it as the first element in the sorted part.
2. Compare the current element with the elements in the sorted part of the list.
3. Shift the larger elements to the right to make space for the current element.
4. Insert the current element into its correct position in the sorted part of the list.
5. Repeat steps 1-4 until all elements are in the sorted order.

## Time Complexity

- **Worst-case time complexity:** O(n<sup>2</sup>)
- **Best-case time complexity:** O(n) (when the list is already sorted)
- **Average-case time complexity:** O(n<sup>2</sup>)

## Space Complexity

Insertion Sort has a space complexity of O(1) because it only requires a constant amount of additional space for storing temporary variables.

## Python Implementation

```python
from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the Insertion Sort algorithm.

    Parameters:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", unsorted_list)
sorted_list = insertion_sort(unsorted_list)
print("Sorted List:", sorted_list)
```
