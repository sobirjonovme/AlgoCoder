"""
https://leetcode.com/problems/shortest-distance-to-a-character/
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        s_lenth = len(s) 
        c_indices = []
        answer = [int] * s_lenth

        for i in range(s_lenth):
            if s[i] == c:
                c_indices.append(i)
        
        for i in range(c_indices[0]+1):
            answer[i] = c_indices[0] - i

        for i in range(len(c_indices)-1):
            left = c_indices[i]
            right = c_indices[i+1]
            for j in range((right-left)//2+1):
                answer[left+j] = j
                answer[right-j] = j
        
        for i in range(c_indices[-1], s_lenth):
            answer[i] = i - c_indices[-1]
        
        return answer


if __name__ == '__main__':
    sol = Solution()

    # example 1
    s = "loveleetcode"
    c = "e"

    # # example 2
    # s = "aaab"
    # c = "b"

    print(f"Result:   {sol.shortestToChar(s, c)}")
