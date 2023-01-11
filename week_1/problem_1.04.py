# https://leetcode.com/problems/richest-customer-wealth/


def maximumWealth(accounts: list[list[int]]) -> int:
    max_wealth = 0

    n = len(accounts)
    m = len(accounts[0])

    for i in range(n):
        wealth = 0
        for j in range(m):
            wealth += accounts[i][j]
        if wealth > max_wealth:
            max_wealth = wealth
    
    return max_wealth
    
        