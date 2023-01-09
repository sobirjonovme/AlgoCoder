# https://leetcode.com/problems/count-items-matching-a-rule/


def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    count = 0
    for i in range(len(items)):
        if ruleKey == 'type':
            if items[i][0] == ruleValue:
                count += 1
        elif ruleKey == 'color':
            if items[i][1] == ruleValue:
                count += 1
        elif ruleKey == 'name':
            if items[i][2] == ruleValue:
                count += 1

    return count

items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "phone"], 
    ["phone", "gold", "iphone"]
    ]
ruleKey = "type"
ruleValue = "phone"

print(countMatches(items, ruleKey, ruleValue))
