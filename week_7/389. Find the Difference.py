"""
https://leetcode.com/problems/find-the-difference/
"""

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for key, value in t_counter.items():
            
            temp = s_counter.get(key)
            if temp is None:
                return key
            
            if value != temp:
                return key


if __name__ == '__main__':
    sol = Solution()

    # example 1
    s = "abcd"
    t = "abcde"

    # # example 2
    # s = ""
    # t = "y"

    print(f"Result:   {sol.findTheDifference(s, t)}")
