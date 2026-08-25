# Second Largest Element in an Array

## Problem Statement

Given an array of integers `nums`, find the **second largest distinct element** in the array.

### Example

**Input:**

```text
nums = [12, 35, 1, 10, 34, 1]
```

**Output:**

```text
34
```

---

## Approach

We use two variables:

- `largest` → stores the largest element found so far.
- `second_largest` → stores the second largest element found so far.

### Steps

1. Initialize `largest` and `second_largest` to negative infinity.
2. Traverse the array once.
3. If the current element is greater than `largest`:
   - Move the current `largest` to `second_largest`.
   - Update `largest`.
4. Otherwise, if the current element is smaller than `largest` but greater than `second_largest`, update `second_largest`.
5. Return `second_largest`.

---

## Python Solution

```python
from typing import List

class Solution:
    def secondLargestElement(self, nums: List[int]) -> int:
        largest = float('-inf')
        second_largest = float('-inf')

        for num in nums:

            if num > largest:
                second_largest = largest
                largest = num

            elif largest > num > second_largest:
                second_largest = num

        return second_largest
```

---

## Dry Run

### Input

```text
nums = [12, 35, 1, 10, 34]
```

| Current Element | Largest | Second Largest |
|----------------:|--------:|---------------:|
| 12 | 12 | -∞ |
| 35 | 35 | 12 |
| 1 | 35 | 12 |
| 10 | 35 | 12 |
| 34 | 35 | 34 |

### Final Output

```text
34
```

---

## Why `float('-inf')`?

We initialize both variables with negative infinity so that the solution also works when the array contains only negative numbers.

For example:

```text
[-10, -5, -20]
```

The answer is:

```text
-10
```

Using `0` as the initial value would give an incorrect result for such arrays.

---

## Time Complexity

- **O(n)**

The array is traversed only once.

---

## Space Complexity

- **O(1)**

Only two extra variables are used.

---

## Key Learning

- Array Traversal
- Maintaining multiple variables
- Finding the largest and second largest values
- Handling duplicate values
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Notes

- The second largest element must be **distinct** from the largest element.
- The algorithm does not require sorting.
- Using a single traversal makes this more efficient than the sorting approach.

