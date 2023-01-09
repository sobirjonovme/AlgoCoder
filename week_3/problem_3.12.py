"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
"""


class Solution:
    def checkString(self, s: str) -> bool:
        
        after_b = False

        for i in s:
            if i == 'b':
                after_b = True
                continue
            if i == 'a' and after_b:
                return False
        
        return True


if __name__ == '__main__':
    sol = Solution()

    s = "aaabbb"
    # s = "abab"
    # s = "bbb"

    print(f"Result:   {sol.checkString(s)}")
