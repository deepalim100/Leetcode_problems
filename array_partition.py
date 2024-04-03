
# leet code link : https://leetcode.com/problems/array-partition/description/

class Array_partition:
    def __init__(self, nums):
        self.nums = nums
    
    def run(self):
        max_num = 0
        self.nums = sorted(self.nums)
        for i in range(0, len(self.nums), 2):
            max_num += min(self.nums[i], self.nums[i+1])

        return max_num


if __name__ == '__main__':
    arr = list(map(int , input('Enter the array:').split()))
    res = Array_partition(arr).run()
    print('---result----',res)