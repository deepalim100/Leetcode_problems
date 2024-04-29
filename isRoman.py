# link of the problem : https://leetcode.com/problems/roman-to-integer/description/


class Roman:
    def process(self, s):
        roman = s
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev_val = 0
        res = 0
        for letter in roman:
            value = roman_dict[letter]
            if value > prev_val:
                res += value - 2 * prev_val
            else:
                res += value
            prev_val = value
        return res
    

if __name__ == '__main__':
    s = 'LVIII'
    res = Roman().process(s)
    print('roman conversion :', res)
