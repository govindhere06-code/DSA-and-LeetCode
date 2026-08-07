# Check if Array Is Sorted

## Problem Statement

Given an array of integers `nums`, determine whether the array is sorted in **non-decreasing order**.

An array is considered sorted if every element is greater than or equal to the element before it.

### Example 1

**Input:**

```text
nums = [1, 2, 3, 4, 5]
```

**Output:**

```text
True
```

### Example 2

**Input:**

```text
nums = [1, 3, 2, 4]
```

**Output:**

```text
False
```

---

## Approach

We compare each element with the element immediately before it.

### Steps

1. Start from index `1`.
2. Compare `nums[i]` with `nums[i - 1]`.
3. If the current element is smaller than the previous element, the array is not sorted.
4. Return `False` immediately.
5. If the entire array is traversed without finding an invalid pair, return `True`.

---

## Python Solution

```python
from typing import List

class Solution:
    def isSorted(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False

        return True
```

---

## Dry Run

### Input

```text
nums = [1, 2, 2, 4, 5]
```

| Index | Current Element | Previous Element | Current < Previous? |
|------:|----------------:|-----------------:|:--------------------:|
| 1 | 2 | 1 | No |
| 2 | 2 | 2 | No |
| 3 | 4 | 2 | No |
| 4 | 5 | 4 | No |

No invalid pair is found.

### Output

```text
True
```

---

## Example of an Unsorted Array

```text
nums = [1, 4, 3, 5]
```

At index `2`:

```text
nums[2] = 3
nums[1] = 4
```

Since:

```text
3 < 4
```

the array is not sorted.

Therefore:

```text
False
```

---

## Time Complexity

- **O(n)**

The array is traversed at most once.

---

## Space Complexity

- **O(1)**

No extra data structure is used.

---

## Key Learning

- Array traversal
- Comparing adjacent elements
- Early return
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Important Note

This solution checks whether an array is **already sorted**.

It does **not** check whether an array is **sorted and rotated**.

For example:

```text
[3, 4, 5, 1, 2]
```

is not sorted in its current form, so this function returns `False`.