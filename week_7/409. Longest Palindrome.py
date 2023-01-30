"""
https://leetcode.com/problems/longest-palindrome/
"""

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0

        for i in Counter(s).values():
            result += i//2 * 2

            if result%2 == 0 and i%2 == 1:
                result += 1

        return result


if __name__ == '__main__':
    sol = Solution()

    s = "abccccdd"
    # s = "a"

    print(f"Result:   {sol.longestPalindrome(s)}")
