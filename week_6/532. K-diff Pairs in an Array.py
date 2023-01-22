"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums_dict = {}
        counter = 0

        for i in nums:
            # num1-x=k -> x=num1-k
            x1 = i-k
            # x-num1=k -> x=num1+k
            x2 = i+k
            if x1 in nums_dict and nums_dict[x1] > 0:
                nums_dict[x1] -= 1
                counter += 1
            elif x2 in nums_dict and nums_dict[x2] > 0:
                nums_dict[x2] -= 1
                counter += 1

            nums_dict[i] = nums_dict[i]+1 if i in nums_dict else 1

        return counter        


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums = [3, 1, 4, 1, 5]
    k = 2

    #example 2
    nums = [1, 2, 3, 4, 5]
    k = 1

    # # example 3
    # nums = [1, 3, 1, 5, 4]
    # k = 0

    print(f"Result:   {sol.findPairs(nums, k)}")
    