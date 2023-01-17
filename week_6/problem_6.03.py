"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        least_greater = None

        while left <= right:
            midpoint = left + (right-left)//2
            
            if target < letters[midpoint]:
                least_greater = letters[midpoint]
                right = midpoint-1
                continue
            
            left = midpoint+1
        
        if least_greater is not None:
            return least_greater
        
        return letters[0]


if __name__ == '__main__':
    sol = Solution()

    # example 1
    letters = ["c", "f", "j"]
    target = "a"

    # # example 2
    # letters = ["c", "f", "j"]
    # target = "c"

    # # example 3
    # letters = ["x", "x", "y", "y"]
    # target = "z"

    print(f"Result:   {sol.nextGreatestLetter(letters, target)}")
