# https://leetcode.com/problems/create-target-array-in-the-given-order/


def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
    
    results = []

    for i in range(len(index)):
        results.insert(index[i], nums[i]) 

    return results

nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

print(createTargetArray(nums, index))    
