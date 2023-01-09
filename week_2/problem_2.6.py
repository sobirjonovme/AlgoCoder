# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

def busyStudent(startTime: list[int], endTime: list[int], queryTime: int) -> int:

    count = 0

    for i in range(len(startTime)):
        if startTime[i] <= queryTime and queryTime <= endTime[i]:
            count += 1
    
    return count


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4

startTime = [4]
endTime = [4]
queryTime = 4

print(busyStudent(startTime, endTime, queryTime))
