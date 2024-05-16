# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)

        nums.insert(-1, target)
        arr = sorted(nums)
        for i in arr:
            if i == target:
                return arr.index(i)