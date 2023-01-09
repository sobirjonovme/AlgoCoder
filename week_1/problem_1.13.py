# https://leetcode.com/problems/truncate-sentence/


def truncateSentence(s: str, k: int) -> str:

    index = 0
    word_num = 0
    sen_len = len(s) 

    while word_num < k and index < sen_len:
        if s[index] == ' ':
            word_num += 1
        index += 1

    if index < sen_len:
        return s[:index-1]
    return s

s = "Hello how are you Contestant"
k = 4

print(truncateSentence(s, k))
