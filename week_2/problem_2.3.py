# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square

def countGoodRectangles(rectangles: list[list[int]]) -> int:

    max_length = 0
    count = 0

    for i in range(len(rectangles)):
        length = min(rectangles[i])
        if max_length == length:
            count += 1
        elif max_length < length:
            max_length = length
            count = 1
    
    return count

rectangles = [[5,8],[3,9],[5,12],[16,5]]

print(countGoodRectangles(rectangles))
