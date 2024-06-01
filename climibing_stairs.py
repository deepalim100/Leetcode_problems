# leetcode : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        if n == 0:
            return n 

        a , b =1, 1
        for i in range(2, n+1):
            a , b = b , a+b

        return b