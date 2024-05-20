# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits):
        digits = ''.join(map(str, digits))
        digits = int(digits) + 1
        digits = [int(i) for i in str(digits)]
        return digits
    

if __name__ == "__main__":
    print('Enter the array :')
    digits = list(map(int , input().split()))
    result = Solution().plusOne(digits)
    print(f'resultant array :{result}')