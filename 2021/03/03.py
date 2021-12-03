from typing import Counter
import util

inp = util.input_as_lines("input")
# print(inp)

ones = Counter()
zeroes = Counter()
for line in inp:
    for index, char in enumerate(line):
        # print(char)
        if char == "0":
            zeroes[index] += 1
        else:
            ones[index] += 1
most_common = ""
least_common = ""
for i in range(12):
    if zeroes[i] - ones[i] > 0:
        # zero most common
        most_common += "0"
        least_common += "1"
    else:
        # one most common
        most_common += "1"
        least_common += "0"

print(most_common)
print(least_common)
print("Part 1:")
print(int(most_common, 2) * int(least_common, 2))
