# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            current = nums[i]
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1
        while non_zero < len(nums):
            nums[non_zero] = 0
            non_zero += 1
        return nums