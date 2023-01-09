# https://leetcode.com/problems/summary-ranges/


def summaryRanges1(nums: list[int]) -> list[str]:

    n = len(nums)

    if n == 0:
        return []

    results = []

    for i in range(n-1):
        if (nums[i]+1) == nums[i+1]:
            if not is_beg:
                results.append(f"{nums[i]}->")
                is_beg = True
        else:
            if is_beg:
                results[-1] += str(nums[i])
            else:
                results.append(str(nums[i]))
            is_beg = False
    
    if is_beg:
        results[-1] += str(nums[-1])
    else:
        results.append(str(nums[-1]))

    return results


def summaryRanges2(nums: list[int]) -> list[str]:

    n = len(nums)

    if n == 0:
        return []

    results = [str(nums[0])]

    for i in range(1, n-1):
        if nums[i-1]+1 != nums[i]:
            results.append(str(nums[i]))
            continue
        if nums[i]+1 != nums[i+1]:
            results[-1] += f"->{nums[i]}"

    if n > 1:
        if nums[-2]+1 == nums[-1]:
            results[-1] += f"->{nums[-1]}"
        else:
            results.append(str(nums[-1]))

    return results

nums = [0, 2, 3, 4, 6, 8, 9]
nums = [0, 1, 2, 4, 5, 7]

print(summaryRanges2(nums))
