# link : https://leetcode.com/problems/can-place-flowers/description/


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check the previous and next plots
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n


if __name__ == "__main__":
    arr = [1,0,0,0,1,0,0]
    n = 2
    result = Solution().canPlaceFlowers(arr, n)
    print(result)