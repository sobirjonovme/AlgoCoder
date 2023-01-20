"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/
"""


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        lt_counter = 0  # Counter of numbers that are Less Than Target 
        et_counter = 0  # Counter of numbers that are Equal To Target 

        for number in nums:
            if number < target:
                lt_counter += 1
                continue
            if number == target:
                et_counter += 1
        
        return list(range(lt_counter, lt_counter+et_counter))


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums = [1, 2, 5, 2, 3]
    target = 2

    # # example 2
    # nums = [1, 2, 5, 2, 3]
    # target = 3

    print(f"Result:   {sol.targetIndices(nums, target)}")
