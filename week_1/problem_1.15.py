# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


def finalValueAfterOperations(operations: list[str]) -> int:
    x = 0
    for operation in operations:
        if '-' == operation[1]:
            x -= 1
        elif '+' == operation[1]:
            x += 1

    return x

operations = ["X++", "++X", "--X", "X--"]

print(finalValueAfterOperations(operations))
