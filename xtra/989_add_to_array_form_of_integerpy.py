"""
https://leetcode.com/problems/add-to-array-form-of-integer/
"""

import math


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result = [0] * (max(len(num), int(math.log10(k))+1) + 1)
        result_index = len(result) - 1
        carry = 0

        for i in range(len(num)-1, -1, -1):
            temp = num[i] + k%10 + carry
            result[result_index] = temp%10
            carry = temp//10
            k = k//10
            result_index -= 1

        while k > 0:
            temp = k%10 + carry
            result[result_index] = temp%10
            carry = temp//10
            k = k//10
            result_index -= 1
        
        if carry != 0:
            result[result_index] = carry
        
        if result[0] == 0:
            return result[1:]

        return result


if __name__ == '__main__':
    sol = Solution()

    # example 1
    num = [1, 2, 0, 0]
    k = 34

    # # example 2
    # num = [2, 7, 4]
    # k = 181

    # example 3
    num = [2, 1, 5]
    k = 806

    print(f"Result:   {sol.addToArrayForm(num, k)}")
