"""
https://leetcode.com/problems/distribute-candies/
"""

from collections import Counter


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        types_number = len(Counter(candyType))
        candy_number = len(candyType)

        if types_number <= candy_number/2:
            return types_number
        
        return candy_number//2
        

if __name__ == '__main__':
    sol = Solution()

    candyType = [1, 1, 2, 2, 3, 3]
    # candyType = [1, 1, 2, 3]
    # candyType = [6, 6, 6, 6]

    print(f"Result:   {sol.distributeCandies(candyType)}")
