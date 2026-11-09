class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            maximum = max(maximum, current_sum)

        return maximum