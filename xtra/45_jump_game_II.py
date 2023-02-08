"""
https://leetcode.com/problems/jump-game-ii/
"""


class Solution:

    @staticmethod
    def find_best_jump(nums, curr_pos):
        best_pos = curr_pos+1

        for i in range(curr_pos+2, curr_pos + nums[curr_pos] + 1):

            if nums[i] != 0 and ((i-curr_pos) + nums[i]) > ((best_pos-curr_pos) + nums[best_pos]):
                best_pos = i
        
        return best_pos

    def jump(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0
        
        curr_pos = 0
        counter = 0

        while curr_pos < len(nums):
            counter += 1

            if (len(nums)-1) <= (nums[curr_pos] + curr_pos):
                return counter
            
            curr_pos = self.find_best_jump(nums, curr_pos)
        

if __name__ == '__main__':
    sol = Solution()

    nums = [2, 3, 1, 1, 4]
    # nums = [2, 3, 0, 1, 4]

    print(f"Result:   {sol.jump(nums)}")
