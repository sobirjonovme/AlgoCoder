"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 1
        right = len(arr)-2

        while left <= right:
            midpoint = left + (right-left)//2
            if arr[midpoint-1] < arr[midpoint] and arr[midpoint] > arr[midpoint+1]:
                return midpoint
            
            if arr[midpoint-1] < arr[midpoint]:
                left = midpoint+1
                continue

            right = midpoint-1 


if __name__ == '__main__':
    sol = Solution()

    # arr = [0,1,0]
    # arr = [0,2,1,0]
    arr = [0,10,5,2]

    print(f"Result:   {sol.peakIndexInMountainArray(arr)}")
