# https://leetcode.com/problems/shuffle-the-array/


def shuffle(nums: list[int], n: int) -> list[int]:
    temp = nums[n:]
    #print(temp)

    j = 2*n - 2
    for i in range(n-1, 0, -1):
        nums[j] = nums[i]
        j -= 2

    for i in range(n):
        nums[2*i+1] = temp[i]
    
    return nums

arr = [1, 3, 5, 7, 2, 4, 6, 8]

print(shuffle(arr, 4))
