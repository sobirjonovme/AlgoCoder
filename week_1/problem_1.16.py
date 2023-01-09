# https://leetcode.com/problems/shuffle-string/


def restoreString(s: str, indices: list[int]) -> str:
    shuffled = s

    for i in range(len(indices)):
        shuffled = shuffled[:indices[i]] + s[i] + shuffled[indices[i]+1:]
    
    return shuffled

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

print(restoreString(s, indices))
