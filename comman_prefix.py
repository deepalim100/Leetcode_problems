# link for code : https://leetcode.com/problems/longest-common-prefix/description/

class comman_prefix:
    def process(self, strings):
        if not strings:
            return ""
        min_len = min(len(s) for s in strings)
        prefix = ""

        for i in range(min_len):
            char = strings[0][i]
            if all(string[i] == char for string in strings):
                prefix += char
            else:
                break

        return prefix
    


if __name__ == "__main__":
    strings = ["flower", "flow", "flight", "flo"]
    res = comman_prefix().process(strings)
    print(f'comman prefix:{res}')