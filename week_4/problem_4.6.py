"""
https://leetcode.com/problems/keyboard-row/
"""


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        
        result_words = []

        for word in words:

            for i in range(3):
                if word[0].lower() in rows[i]:
                    row_num = i
                    break
            
            is_valid = True
            for i in range(1, len(word)):
                if word[i].lower() not in rows[row_num]:
                    is_valid = False
                    break

            if is_valid:
                result_words.append(word)
        
        return result_words
            

if __name__ == '__main__':
    sol = Solution()

    words = ["Hello","Alaska","Dad","Peace"]
    # words = ["omk"]
    # words = ["adsdf","sfd"]

    print(f"Result:   {sol.findWords(words)}")
