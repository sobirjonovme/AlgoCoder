"""
https://leetcode.com/problems/add-strings/
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        on_mind = 0
        result = ''

        length1 = len(num1)
        length2 = len(num2)

        if length1 < length2:
            num2, num1 = num1, num2
            length2, length1 = length1, length2
        
        for i in range(1, length2+1):
            temp_sum = int(num1[-i]) + int(num2[-i]) + on_mind
            on_mind = temp_sum//10
            result += str(temp_sum%10)
        
        for i in range(length2+1, length1+1):
            temp_sum = int(num1[-i]) + on_mind
            on_mind = temp_sum//10
            result += str(temp_sum%10)
        
        if on_mind:
            result += str(on_mind)

        return result[::-1]


if __name__ == '__main__':
    sol = Solution()

    # # example 1
    # num1 = "11"
    # num2 = "123"

    # # example 2
    # num1 = "456"
    # num2 = "77"

    # example 3
    num1 = "0"
    num2 = "0"

    print(f"Result:   {sol.addStrings(num1, num2)}")
