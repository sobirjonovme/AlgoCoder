# https://leetcode.com/problems/plus-one/


def plusOne(digits: list[int]) -> list[int]:
    
    n = len(digits)

    for i in range(n-1, -1, -1):
        
        if digits[i] + 1 < 10:
            digits[i] += 1
            return digits
        
        digits[i] = 0
    
    digits.insert(0, 1)
    return digits


digits = [9]

digits = [1, 2, 4, 9, 9, 9]

print(plusOne(digits))
