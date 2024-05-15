# finding the first occurence of substring
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def substring(self, needle, haystack):
        index = haystack.find(needle)
        if index != -1:
            return index
        else:
            return -1
        

if __name__ == "__main__":
    needle = str(input('Enter substring:'))
    haystack = str(input('Enter main string:'))
    i = Solution().substring(needle, haystack)
    print(f'{i} of found substring')