# Selection Sort

Selection Sort is a simple sorting algorithm that divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly finds the minimum element from the unsorted sublist and moves it to the beginning of the sorted sublist.

## Algorithm Steps

1. Divide the input list into two sublists: a sorted sublist and an unsorted sublist.
2. Initially, the sorted sublist is empty, and the unsorted sublist contains all elements of the list.
3. Find the minimum element from the unsorted sublist.
4. Swap the minimum element with the first element of the unsorted sublist, thus extending the sorted sublist by one.
5. Repeat steps 3-4 until all elements are in the sorted order.

## Time Complexity

- **Worst-case time complexity:** O(n<sup>2</sup>)
- **Best-case time complexity:** O(n<sup>2</sup>)
- **Average-case time complexity:** O(n<sup>2</sup>)

## Space Complexity

Selection Sort has a space complexity of O(1) because it only requires a constant amount of additional space for storing temporary variables.

## Python Implementation

```python
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
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", unsorted_list)
sorted_list = selection_sort(unsorted_list)
print("Sorted List:", sorted_list)
```

## Example

Consider the following list: `[64, 34, 25, 12, 22, 11, 90]`
After applying Selection Sort, the sorted list would be: `[11, 12, 22, 25, 34, 64, 90]`
