# https://leetcode.com/problems/three-consecutive-odds

from itertools import count


def threeConsecutiveOdds(arr: list[int]) -> bool:
    count = 0

    for i in range(len(arr)):
        if arr[i]%2 == 0:
            count = 0
            continue
        
        count += 1
        if count ==3 :
            return True
        
    return False


arr = [2, 6, 4, 1]
arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]

print(threeConsecutiveOdds(arr))
