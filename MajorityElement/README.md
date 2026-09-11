# Majority Element

Given an array `nums` of size `n`, return the majority element — the element that appears more than `⌊n / 2⌋` times. It is guaranteed that a majority element always exists.

## Examples

**Example 1**
```
Input:  nums = [3,2,3]
Output: 3
```

**Example 2**
```
Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

## Approach: Boyer-Moore Voting Algorithm

This solution runs in **O(n) time** and **O(1) space**, which beats the more obvious approaches (hash map counting: O(n) time / O(n) space, or sorting: O(n log n) time).

### Intuition

Think of it as a tug-of-war. The majority element appears more times than *all other elements combined*. If every occurrence of the majority element "cancels out" one occurrence of some other element, the majority element is guaranteed to have leftover, uncancelled instances by the end.

We track a `candidate` and a `count` (a net score: candidate's appearances minus everyone else's, since the last reset).

- If `count` hits `0`, we have no confidence in the current candidate, so we pick a new one.
- If the current number matches the candidate, we gain confidence (`+1`).
- If it doesn't match, we lose confidence (`-1`).

### Code

```python
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
```

### Walkthrough: `[2,2,1,1,1,2,2]`

| num | count before | action                     | candidate | count after |
|-----|---------------|----------------------------|-----------|-------------|
| 2   | 0             | count=0 → candidate=2      | 2         | 1           |
| 2   | 1             | match → +1                 | 2         | 2           |
| 1   | 2             | no match → -1              | 2         | 1           |
| 1   | 1             | no match → -1              | 2         | 0           |
| 1   | 0             | count=0 → candidate=1      | 1         | 1           |
| 2   | 1             | no match → -1              | 1         | 0           |
| 2   | 0             | count=0 → candidate=2      | 2         | 1           |

**Result: `2`** ✓

### Why it works (correctness guarantee)

Every "reset" pairs one non-majority element against one majority element, cancelling both out. Since the majority element appears more times than all other elements *combined*, there aren't enough non-majority elements to cancel out every single occurrence of it. No matter how many times the candidate gets reset along the way, the majority element is guaranteed to be the one still standing at the end.

## Complexity

| Approach            | Time         | Space |
|----------------------|--------------|-------|
| Boyer-Moore Voting    | O(n)         | O(1)  |
| Hash map counting     | O(n)         | O(n)  |
| Sorting               | O(n log n)   | O(1) / O(log n)* |

\* depends on the sort implementation