# Rearrange Array Elements by Sign

A Python solution to **LeetCode 2149: Rearrange Array Elements by Sign**.

## Problem Statement

You are given a 0-indexed integer array `nums` of **even length** containing an **equal number of positive and negative integers**.

Rearrange the array so that:

1. Every consecutive pair of integers has **opposite signs**.
2. For all integers with the same sign, the **original relative order is preserved**.
3. The rearranged array **begins with a positive integer**.

Return the modified array.

## Example

```
Input:  nums = [3, 1, -2, -5, 2, -4]
Output: [3, -2, 1, -5, 2, -4]
```

**Explanation:**
- Positives in order: `3, 1, 2`
- Negatives in order: `-2, -5, -4`
- Interleaved starting with a positive: `[3, -2, 1, -5, 2, -4]`

## Approach

Since the result must start with a positive number and alternate signs:

- **Positive numbers** go at **even indices** (`0, 2, 4, ...`)
- **Negative numbers** go at **odd indices** (`1, 3, 5, ...`)

We keep two pointers into a result array of the same size:

| Pointer    | Starts at | Moves by | Fills        |
|------------|-----------|----------|--------------|
| `positive` | `0`       | `+2`     | Even indices |
| `negative` | `1`       | `+2`     | Odd indices  |

We iterate through `nums` once. Each element is placed at the next available slot for its sign, which automatically preserves the relative order within each group.

## Code

```python
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        result = [0] * len(nums)

        positive, negative = 0, 1

        for x in nums:
            if x > 0:
                result[positive] = x
                positive += 2
            else:
                result[negative] = x
                negative += 2

        return result
```

## Dry Run

For `nums = [3, 1, -2, -5, 2, -4]`:

| Step | `x`  | Placed at | `result`                  |
|------|------|-----------|---------------------------|
| 1    | 3    | index 0   | `[3, 0, 0, 0, 0, 0]`      |
| 2    | 1    | index 2   | `[3, 0, 1, 0, 0, 0]`      |
| 3    | -2   | index 1   | `[3, -2, 1, 0, 0, 0]`     |
| 4    | -5   | index 3   | `[3, -2, 1, -5, 0, 0]`    |
| 5    | 2    | index 4   | `[3, -2, 1, -5, 2, 0]`    |
| 6    | -4   | index 5   | `[3, -2, 1, -5, 2, -4]`   |

## Complexity Analysis

| Metric | Complexity | Reason                                      |
|--------|------------|---------------------------------------------|
| Time   | **O(n)**   | Single pass through the input array         |
| Space  | **O(n)**   | Extra result array of the same size as input |

## Constraints

- `2 <= nums.length <= 2 * 10^5`
- `nums.length` is even
- `1 <= |nums[i]| <= 10^5`
- `nums` has an equal number of positive and negative integers

> **Note:** The `else` branch treats any non-positive value as negative. This is safe here because the constraints guarantee `nums` contains no zeros.

## How to Run

```python
sol = Solution()
print(sol.rearrangeArray([3, 1, -2, -5, 2, -4]))  # [3, -2, 1, -5, 2, -4]
print(sol.rearrangeArray([-1, 1]))                # [1, -1]
```

## Tags

`Array` `Two Pointers` `Simulation`