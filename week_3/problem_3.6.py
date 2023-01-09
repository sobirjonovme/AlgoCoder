"""
https://leetcode.com/problems/defanging-an-ip-address/
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ''

        for i in address:
            if i == '.':
                result += '[.]'
                continue
            result += i

        return result


if __name__ == '__main__':
    sol = Solution()

    # address = "1.1.1.1"
    address = "255.100.50.0"

    print(f"Result:   {sol.defangIPaddr(address)}")
