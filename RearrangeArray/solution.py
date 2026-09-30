class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        result = [0] * len(nums)

        positive,negative = 0,1

        for x in nums:
            if x > 0:
                result[positive] = x
                positive += 2

            else:
                result[negative] = x
                negative += 2

        return result
        