"""
https://leetcode.com/problems/to-lower-case/
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == '__main__':
    sol = Solution()

    s = "Hello"
    s = "here"
    s = "LOVELY"

    print(f"Result:   {sol.toLowerCase(s)}")
