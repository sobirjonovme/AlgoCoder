"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = (high+1) // 2
        extra = low // 2

        return total-extra


if __name__ == '__main__':
    sol = Solution()

    # example 1
    low = 3
    high = 7

    # # example 2
    # low = 8
    # high = 10

    print(f"Result:   {sol.countOdds(low, high)}")
