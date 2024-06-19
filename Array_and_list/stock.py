# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1293687224/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_num = prices[0]
        max_num = 0
        for i in range(len(prices)):
            min_num = min(min_num, prices[i])
            max_num = max(max_num, prices[i]-min_num)

        return max_num
    

if __name__ == '__main__':
    arr = [2,1,2,0,1]
    res = Solution().maxProfit(arr)
    print(f'---res--- : {res}')