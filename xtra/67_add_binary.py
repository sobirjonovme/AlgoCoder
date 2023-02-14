"""
https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a = len(a)-1
        index_b = len(b)-1
        result = ''
        carry = 0

        while index_a >= 0 and index_b >= 0:
            temp = int(a[index_a]) + int(b[index_b]) + carry
            result += str(temp%2)
            carry = temp//2
            index_a -= 1
            index_b -= 1

        while index_a >= 0:
            temp = int(a[index_a]) + carry
            result += str(temp%2)
            carry = temp//2
            index_a -= 1
        
        while index_b >= 0:
            temp = int(b[index_b]) + carry
            result += str(temp%2)
            carry = temp//2
            index_b -= 1

        if carry != 0:
            result += str(carry)

        return result[::-1]


if __name__ == '__main__':
    sol = Solution()

    # example 1
    a = "11"
    b = "1"

    # # example 2
    # a = "1010"
    # b = "1011"

    print(f"Result:   {sol.addBinary(a, b)}")
