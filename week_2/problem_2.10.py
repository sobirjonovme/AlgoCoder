# https://leetcode.com/problems/number-of-lines-to-write-string/
import string

string.ascii_lowercase

def numberOfLines(widths: list[int], s: str) -> list[int]:
    letters = list(string.ascii_lowercase)
    letters_dict = {}

    for i in range(len(letters)):
        letters_dict[letters[i]] = i

    line_count = 0
    line_width = 0

    for i in s:
        pixel = widths[letters_dict[i]]

        if line_width + pixel <= 100:
            line_width += pixel
        else:
            line_width = pixel
            line_count += 1

    return [line_count+1, line_width]
 
widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
s = "abcdefghijklmnopqrstuvwxyz"

widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
s = "bbbcccdddaaa"

print(numberOfLines(widths, s))
