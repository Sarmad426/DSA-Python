# Linear Search Algorithm

## Overview

Linear search, also known as sequential search, is a simple method for finding a target value within a list. It sequentially checks each element of the list until a match is found or the entire list has been searched. It is generally less efficient than other search algorithms, such as binary search, for large datasets, but it is straightforward to implement and works well for small lists or unordered data.

## Algorithm

The algorithm works by iterating through the elements of the list one by one, comparing each element with the target value until a match is found or the end of the list is reached.

## Pseudo code

```algo
function linear_search(list, target):
    for each item in the list:
        if item equals target:
            return index of item
    return -1
```

## Time Complexity

The time complexity of linear search is O(n), where n is the number of elements in the list. This is because, in the worst-case scenario, the algorithm may have to iterate through all elements of the list to find the target element.

## Implementation in Python

```python
from typing import List, Any, Optional

def linear_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform linear search to find the index of the target element in the array.

    Args:
        arr (List[Any]): The list to search through.
        target (Any): The target element to search for.

    Returns:
        Optional[int]: The index of the target element if found, None otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None
```

## Example Usage

```python
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70
result = linear_search(arr, target)
if result is not None:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
```

In this example, the target element `70` is found at index `6`.
