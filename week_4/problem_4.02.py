"""
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        there_is_break = False
        result = ''

        for i in s:
            if i == ' ':
                there_is_break = True
                continue
                
            if there_is_break:
                result = i
                there_is_break = False
                continue

            result += i
        
        return len(result)
            


if __name__ == '__main__':
    sol = Solution()

    s = "Hello World"
    # s = "   fly me   to   the moon  "
    # s = "luffy is still joyboy"

    print(f"Result:   {sol.lengthOfLastWord(s)}")
