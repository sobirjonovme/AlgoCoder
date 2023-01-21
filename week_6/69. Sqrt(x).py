"""
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = left + (right-left)//2
            
            if mid*mid == x:
                return mid
            
            if mid*mid < x:
                left = mid+1
                ans = mid
                continue

            right = mid-1
        
        return ans


if __name__ == '__main__':
    sol = Solution()

    x = 4
    # x = 8

    print(f"Result:   {sol.mySqrt(x)}")
