# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

def findKDistantIndices(nums: list[int], key: int, k: int) -> list[int]:
    last = -1
    results = []
    n = len(nums)

    for i in range(n):
        if nums[i] == key:
            begin = i - k
            end = i + k
            print(begin, end)
            if begin <= last:
                begin = last+1
            if end >= n:
                end = n-1
            last = end
            results += list(range(begin, end+1))
    
    return results


nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1

nums = [2, 2, 2, 2, 2]
key = 2
k = 2

nums = [1]
key = 1
k = 1

print(findKDistantIndices(nums, key, k))
