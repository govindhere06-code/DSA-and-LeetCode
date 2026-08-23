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

    