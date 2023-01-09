# https://leetcode.com/problems/minimum-time-visiting-all-points

def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    count = 0
    for i in range(len(points)-1):
        delta_x = abs(points[i][0] - points[i+1][0])
        delta_y = abs(points[i][1] - points[i+1][1])
        count += delta_x if delta_x > delta_y else delta_y

    return count

points = [[1,1],[3,4],[-1,0]]

print(minTimeToVisitAllPoints(points))
    