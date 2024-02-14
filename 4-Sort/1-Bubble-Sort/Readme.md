# Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## Algorithm Steps

1. Start from the first element (index 0) and compare it with the next element.
2. If the current element is greater than the next element, swap them.
3. Move to the next pair of adjacent elements and repeat step 2.
4. Continue this process until the end of the list is reached.
5. Repeat steps 1-4 until no swaps are performed in a full iteration.

## Time Complexity

- **Worst-case time complexity:** O(n<sup>2</sup>)
- **Best-case time complexity:** O(n) (when the list is already sorted)
- **Average-case time complexity:** O(n<sup>2</sup>)

## Space Complexity

Bubble Sort has a space complexity of O(1) because it only requires a constant amount of additional space for storing temporary variables.

## Python Implementation

```python
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
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", unsorted_list)
sorted_list = bubble_sort(unsorted_list)
print("Sorted List:", sorted_list)
```

### Example

Consider the following list: `[64, 34, 25, 12, 22, 11, 90]`
After applying Bubble Sort, the sorted list would be: `[11, 12, 22, 25, 34, 64, 90]`
