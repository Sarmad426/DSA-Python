# Binary Search Algorithm

Binary search is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half until the target is found or the subarray is empty. Binary search is an efficient algorithm with a time complexity of O(log n), where n is the number of elements in the array. However, it requires the array to be sorted beforehand.

## Algorithm

Binary search works by repeatedly dividing the search interval in half. It compares the target value with the middle element of the array. If the target value matches the middle element, its position is returned. If the target value is less than the middle element, the search continues in the lower half of the array. If the target value is greater than the middle element, the search continues in the upper half of the array. This process continues until the target value is found or the search interval is empty.

## Pseudocode

```pseudo
function binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Implementation in Python

```python
from typing import List, Any, Optional

def binary_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform binary search to find the index of the target element in the sorted array.

    Args:
        arr (List[Any]): The sorted list to search through.
        target (Any): The target element to search for.

    Returns:
        Optional[int]: The index of the target element if found, None otherwise.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
```

## Example Usage

```python
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70
result = binary_search(arr, target)
if result is not None:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
```

In this example, the target element `70` is found at index `6`.
