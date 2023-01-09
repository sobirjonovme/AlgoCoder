# https://leetcode.com/problems/teemo-attacking/

def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
    total_poisoned_time = 0
    poisone_end_time = 0

    for i in range(len(timeSeries)):
        begin = timeSeries[i]
        end = begin + duration

        if begin < poisone_end_time:
            begin = poisone_end_time
        
        total_poisoned_time += (end - begin)
        poisone_end_time = end
    
    return total_poisoned_time

timeSeries = [1, 4]
duration = 2

timeSeries = [1, 2]
duration = 2

print(findPoisonedDuration(timeSeries, duration))
