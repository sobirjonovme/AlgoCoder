# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

def sumZero(n: int) -> list[int]:

    result = [int]*n

    for i in range(0, n-1, 2):
        result[i] = i+1
        result[i+1] = -(i+1)
    
    if n%2 == 1:
        result[n-1] = 0

    return result

n = 5

print(sumZero(5))
