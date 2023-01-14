"""
https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        s_length = len(s)

        step_index = 0

        while step_index+2*k <= s_length:
            for i in range(step_index+k-1, step_index-1, -1):
                result += s[i]
            for i in range(step_index+k, step_index+2*k):
                result += s[i]
            
            step_index += 2*k
        
        if s_length - step_index >= k:
            for i in range(step_index+k-1, step_index-1, -1):
                result += s[i]
        
            for i in range(step_index+k, s_length):
                result += s[i]
             
            return result
        
        for i in range(s_length-1, step_index-1, -1):
            result += s[i]

        return result


if __name__ == '__main__':
    sol = Solution()

    # # example 1
    # s = "abcdefg"
    # # s = '1234567890123'
    # k = 2

    # example 2
    s = "abc"
    k = 4

    print(f"Result:   {sol.reverseStr(s, k)}")
