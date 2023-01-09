# https://leetcode.com/problems/decompress-run-length-encoded-list/


def decompressRLElist(nums: list[int]) -> list[int]:

    results = []

    for i in range(0, len(nums), 2):
        results += [nums[i+1]]*nums[i]

    return results

nums = [1,2,3,4]
print(decompressRLElist(nums))
