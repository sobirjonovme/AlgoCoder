# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/


class Solution:

    def count_words(self, s: str) -> int:
        if s == '':
            return 0
        count = 0
        for letter in s:
            if letter == ' ':
                count += 1
        return count+1

    def mostWordsFound(self, sentences: list[str]) -> int:
        max_length = 0
        for i in range(len(sentences)):
            length = self.count_words(sentences[i])
            if length > max_length:
                max_length = length
        
        return max_length


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

a = Solution()
print(Solution.mostWordsFound(a, sentences))
        