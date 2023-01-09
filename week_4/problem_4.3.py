"""
https://leetcode.com/problems/number-of-segments-in-a-string/
"""


class Solution:
    def countSegments(self, s: str) -> int:
        there_is_break = True
        result = 0

        for i in s:
            if i == ' ':
                there_is_break = True
                continue
                
            if there_is_break:
                result += 1
                there_is_break = False
                continue
        
        return result


if __name__ == '__main__':
    sol = Solution()

    s = "Hello, my name is John"
    # s = "Hello"

    print(f"Result:   {sol.countSegments(s)}")
    