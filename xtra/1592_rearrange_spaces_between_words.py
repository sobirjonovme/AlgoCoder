"""
https://leetcode.com/problems/rearrange-spaces-between-words/
"""

class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = 0
        num_words = 0
        words = []
        word = ''
        is_word_begin = False

        for i in text:
            if i == " ":
                num_spaces += 1
                if is_word_begin == True:
                    num_words += 1
                    words.append(word)
                    word = ''
                    is_word_begin = False
                continue
            
            if is_word_begin is True:
                word += i
                continue

            is_word_begin = True
            word = i

        if is_word_begin == True:
            num_words += 1
            words.append(word)
        

        if num_words > 1:
            num_words -= 1
            
            num_equal_spaces = num_spaces//num_words
            equal_spaces = "".join([" " for _ in range(num_equal_spaces)])

            result = equal_spaces.join(words)
            for i in range(num_spaces%num_words):
                result += " "
            
            return result
        
        return words[0] + "".join([" " for _ in range(num_spaces)])
            
            
if __name__ == "__main__":
    sol = Solution()
    
    text = "  this   is  a sentence "
    print(sol.reorderSpaces(text))
