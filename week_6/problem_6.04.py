"""
https://leetcode.com/problems/first-bad-version/
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        initial_bad = 1

        # while left <= right:
        #     midpoint = left + (right-left)//2

        #     if isBadVersion(midpoint):
        #         initial_bad = midpoint
        #         right = midpoint-1
        #         continue
            
        #     left = midpoint+1
        
        return initial_bad


if __name__ == '__main__':
    sol = Solution()

    # example 1
    n = 5
    bad = 4

    # example 2
    n = 1
    bad = 1

    # unable to check
    # because we don't have isBadVersion API
