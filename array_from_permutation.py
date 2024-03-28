class Solution:
    def buildArray(self, nums):
        """
        Builds a new array from the given permutation.
        
        Args:
            nums (List[int]): The input permutation.
            
        Returns:
            List[int]: The new array built from the permutation.
        """
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            print(nums[i], '=====', nums[nums[i]])
            arr[i] = nums[nums[i]]
            
        print('===arr===', arr)
        return arr


if __name__ == '__main__':
    nums = [5, 0, 1, 2, 3, 4]#list(map(int, input().split()))
    res = Solution().buildArray(nums)
    print(f'==final res===:{res}')