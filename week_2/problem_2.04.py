# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from itertools import count


def oddCells(m: int, n: int, indices: list[list[int]]) -> int:
    matrix = []
    for i in range(m):
        matrix.append([0]*n)
    
    for i in range(len(indices)):
        for j in range(n):
            matrix[indices[i][0]][j] += 1
        
        for j in range(m):
            matrix[j][indices[i][1]] += 1

    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]%2 == 1:
                count += 1
    
    return count
    
m = 2
n = 3
indices = [[0, 1], [1, 1]]

print(oddCells(m, n, indices))
    