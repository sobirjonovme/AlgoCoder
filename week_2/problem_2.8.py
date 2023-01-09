# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate

def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    smallest_index = -1
    n = len(points)
    for i in range(n):
        if points[i][0] == x or points[i][1] == y:
            smallest_distance = abs(points[i][0]-x) + abs(points[i][1]-y)
            smallest_index = i
            break
    
    for j in range(i+1, n):
        if points[j][0] == x or points[j][1] == y:
            distance = abs(points[j][0]-x) + abs(points[j][1]-y)
            if distance < smallest_distance:
                smallest_distance = distance
                smallest_index = j

    return smallest_index


x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]

x = 3
y = 4
points = [[2, 3]]

print(nearestValidPoint(x, y, points))
