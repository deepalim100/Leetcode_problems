# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = list(s.split())
        len_lst = len(lst[-1])
        return len_lst