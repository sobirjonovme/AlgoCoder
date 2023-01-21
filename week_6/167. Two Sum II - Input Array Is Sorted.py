"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            total = numbers[left] + numbers[right]
            
            if total == target:
                return [left+1, right+1]
            
            if total > target:
                right -= 1
                continue
            left += 1


if __name__ == '__main__':
    sol = Solution()

    # example 1
    numbers = [2, 7, 11, 15]
    target = 9

    # # example 2
    # numbers = [2, 3, 4]
    # target = 6

    # # example 3
    # numbers = [-1, 0]
    # target = -1

    print(f"Result:   {sol.twoSum(numbers, target)}")
