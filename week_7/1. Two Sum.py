"""
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}

        for i in range(len(nums)):
            num2 = target - nums[i]

            if nums_dict.get(num2) is not None:
                return [nums_dict.get(num2), i]
            
            nums_dict[nums[i]] = i


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums = [2, 7, 11, 15]
    target = 9

    # # example 2
    # nums = [3, 2, 4]
    # target = 6    

    print(f"Result:   {sol.twoSum(nums, target)}")
