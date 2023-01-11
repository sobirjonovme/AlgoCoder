"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""
# a ->	97	lowercase a

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        result = ''

        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                ascii_num = int(s[i]) * 10 + int(s[i+1]) + 96
                result += chr(ascii_num)
                i += 3
                continue
            result += chr(int(s[i])+96)
            i += 1
        
        return result
                


if __name__ == '__main__':
    sol = Solution()

    # s = "10#11#12"
    s = "1326#"

    print(f"Result:   {sol.freqAlphabets(s)}")
