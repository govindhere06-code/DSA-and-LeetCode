class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count0 = count1 = count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1

            elif num == 1:
                count1 += 1

            else:
                count2 += 1

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
        