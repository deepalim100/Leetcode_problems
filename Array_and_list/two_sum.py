# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        # If no solution is found, return an empty list
        return []

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,4]
    target = 6
    result = sol.twoSum(nums, target)
    print(f"The indices of the two numbers that add up to {target} are: {result}")
