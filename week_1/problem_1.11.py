# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


def sumOddLengthSubarrays(arr: list[int]) -> int:
    n = len(arr)
    total = 0
    
    for i in range(n):
        sub_sum = arr[i]
        total += sub_sum

        for j in range(i+2, n, 2):
            sub_sum += arr[j-1] + arr[j]
            total += sub_sum
    
    return total

arr = [1, 4, 2, 5, 3]

print(sumOddLengthSubarrays(arr))
            
