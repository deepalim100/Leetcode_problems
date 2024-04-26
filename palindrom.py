
## link of prgram : https://leetcode.com/problems/palindrome-number/submissions/1242645452/
class Solution:
    def isPalindrome(self, x: int):
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    x = 12321
    res = Solution().isPalindrome(x)
    print(f'palindrom is : {res}')