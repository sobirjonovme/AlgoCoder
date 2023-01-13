"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_sentence = ''
        
        words = s.split(' ')

        for i in range(len(words)-1):
            reverse_sentence += words[i][::-1] + ' '
        
        reverse_sentence += words[-1][::-1]

        return reverse_sentence


if __name__ == '__main__':
    sol = Solution()

    # s = "Let's take LeetCode contest"
    s = "God Ding"

    print(f"Result:   {sol.reverseWords(s)}")
