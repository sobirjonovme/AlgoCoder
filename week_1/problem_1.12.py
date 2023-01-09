# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    
    line1 = ''
    line2 = ''

    for word in word1:
        line1 += word
    for word in word2:
        line2 += word

    return line1 == line2

word1 = ["ab", "c"]
word2 = ["a", "bc"]

# word1 = ["a", "cb"]
# word2 = ["ab", "c"]

print(arrayStringsAreEqual(word1, word2))
