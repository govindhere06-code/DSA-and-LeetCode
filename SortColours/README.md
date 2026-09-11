# Sort Colors (Dutch National Flag Problem)

## Problem
Given an array `nums` with `n` objects colored red, white, or blue (represented as `0`, `1`, and `2`), sort them in-place so that objects of the same color are adjacent, in the order red, white, blue — **without using a built-in sort function**.

## Approach: Counting Sort (Two-Pass)

Since there are only three distinct values (`0`, `1`, `2`), we can count how many of each value exist, then overwrite the array based on those counts.

### Steps
1. **First pass:** Traverse the array once and count occurrences of `0`, `1`, and `2` using three counters (`count0`, `count1`, `count2`).
2. **Second pass:** Overwrite the array from left to right — write `count0` zeros, then `count1` ones, then `count2` twos.

### Code
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0

        # First pass: count occurrences
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Second pass: overwrite array using counts
        index = 0
        for _ in range(count0):
            nums[index] = 0
            index += 1
        for _ in range(count1):
            nums[index] = 1
            index += 1
        for _ in range(count2):
            nums[index] = 2
            index += 1
```

### Complexity
- **Time:** O(n) — two passes through the array
- **Space:** O(1) — only three counter variables used

## Example

**Input:** `[2,0,2,1,1,0]`
**Output:** `[0,0,1,1,2,2]`

**Input:** `[2,0,1]`
**Output:** `[0,1,2]`

## Possible Follow-Up
A **one-pass** solution exists using three pointers (`low`, `mid`, `high`), known as the **Dutch National Flag algorithm**, which sorts the array while only traversing it once.