"""
https://leetcode.com/problems/goat-latin/
"""


class Solution:
    vowels =  ('a', 'e', 'i', 'o', 'u')

    def toGoatLatin(self, sentence: str) -> str:
        extra_a = 'a'
        result_sentence = ''
        i = 0
        if sentence[0].lower() in self.vowels:
            first_letter = ''
        else:
            first_letter = sentence[0]
            i += 1

        while i < len(sentence):
            if sentence[i] == ' ':         
                if first_letter:
                    result_sentence += first_letter
                result_sentence += 'ma' + extra_a + ' '

                if sentence[i+1].lower() in self.vowels:
                    first_letter = ''
                    i += 1
                else:
                    first_letter = sentence[i+1]
                    i += 2
                extra_a += 'a'
                continue

            result_sentence += sentence[i]
            i += 1
        
        if first_letter:
            result_sentence += first_letter
        result_sentence += 'ma' + extra_a
        
        return result_sentence


if __name__ == '__main__':
    sol = Solution()

    sentence = "I speak Goat Latin"
    sentence = "The quick brown fox jumped over the lazy dog"

    print(f"Result:   {sol.toGoatLatin(sentence)}")
