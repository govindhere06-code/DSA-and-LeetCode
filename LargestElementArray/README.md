# Largest Element in an Array

## Problem Statement

Given an array of integers `nums`, return the largest element present in the array.

### Example

**Input:**

```text
nums = [5, 8, 2, 12, 7]
```

**Output:**

```text
12
```

---

## Approach

1. Assume the first element of the array is the largest.
2. Traverse the array from left to right.
3. Compare each element with the current largest element.
4. If the current element is greater, update the largest element.
5. After traversing the entire array, return the largest element.

---

## Python Solution

```python
from typing import List

class Solution:
    def largestElement(self, nums: List[int]) -> int:
        largest = nums[0]

        for num in nums:
            if num > largest:
                largest = num

        return largest
```

---

## Dry Run

### Input

```text
nums = [5, 8, 2, 12, 7]
```

| Current Element | Largest Before | Largest After |
|----------------:|---------------:|--------------:|
| 5 | 5 | 5 |
| 8 | 5 | 8 |
| 2 | 8 | 8 |
| 12 | 8 | 12 |
| 7 | 12 | 12 |

### Final Output

```text
12
```

---

## Time Complexity

- **O(n)**

The array is traversed exactly once.

---

## Space Complexity

- **O(1)**

Only one extra variable (`largest`) is used regardless of the input size.

---

## Edge Cases

- Array with one element

```text
[42] → 42
```

- Array containing all negative numbers

```text
[-5, -9, -1, -7] → -1
```

- Array with duplicate largest elements

```text
[3, 7, 7, 2] → 7
```

---

## Key Learning

- Array Traversal
- Linear Search
- Maintaining a Running Maximum
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Notes

- Initializing `largest` with `nums[0]` ensures the solution works correctly even when all elements are negative.
- Every element must be checked because the largest value could appear anywhere in the array.