"""
https://leetcode.com/problems/replace-all-digits-with-characters/
"""


class Solution:
    def shift(self, c: str, x: int) -> str:
        """
        Where c is a character and x is a digit, that returns the xth character after c.
        """
        if len(c) == 1:
            return chr(ord(c)+x)


    def replaceDigits(self, s: str) -> str:
        result_s = ''

        for i in range(len(s)):
            if i%2 == 0:
                result_s += s[i]
                continue

            result_s += self.shift(s[i-1], int(s[i]))
        
        return result_s


if __name__ == '__main__':
    sol = Solution()

    # s = "a1c1e1"
    s = "a1b2c3d4e"

    print(f"Result:   {sol.replaceDigits(s)}")
