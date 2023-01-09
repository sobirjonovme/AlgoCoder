# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:

    max_candies = 0

    for i in candies:
        if max_candies < i:
            max_candies = i
    
    n = len(candies)
    results = [True]*n

    for i in range(n):
        if candies[i]+extraCandies < max_candies:
            results[i] = False
        
    return results

candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies(candies, extraCandies))
