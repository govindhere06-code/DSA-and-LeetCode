class Solution:
    def largestElement(self, nums: List[int]) -> int:
        largest = nums[0]

        for num in nums:
            if num > largest:
                largest = num

        return largest