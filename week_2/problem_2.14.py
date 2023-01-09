# https://leetcode.com/problems/defuse-the-bomb

def decrypt(code: list[int], k: int) -> list[int]:
    
    n = len(code)
    result_code = [0]*n

    if k > 0:
        for i in range(n):
            next_k_sum = 0
            for j in range(i+1, i+1+k):
                j = j % n
                next_k_sum += code[j]

            result_code[i] = next_k_sum
    
    elif k < 0:
        k = abs(k)
        for i in range(n):
            previous_k_sum = 0
            for j in range(i-1, i-1-k, -1):
                j = (n + j) % n
                previous_k_sum += code[j]

            result_code[i] = previous_k_sum

    return result_code
code = [1, 2, 3, 4]
k = 0

code = [5, 7, 1, 4]
k = 3

code = [2, 4, 9, 3]
k = -2
    
print(decrypt(code, k))
