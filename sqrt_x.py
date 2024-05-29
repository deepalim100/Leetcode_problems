# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low, high = 0, x
        while low <= high :
            mid = (low + high) // 2
            mid_square = mid * mid
            if mid_square == x:
                return mid
            elif mid_square < x:
                low = mid + 1
            else:
                high = mid -1

        return high