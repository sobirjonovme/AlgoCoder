# https://leetcode.com/problems/concatenation-of-array/


def getConcatenation1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)

    ans = [None]*(n*2)

    for i in range(n):
        ans[i] = nums[i]
        ans[i+n] = nums[i]

    return ans

def getConcatenation2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in nums:
        ans.append(i)
    for i in nums:
        ans.append(i)
    return ans  

def getConcatenation3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = nums*2
    return ans    


arr = [1, 2, 3]
print(getConcatenation3(arr))
