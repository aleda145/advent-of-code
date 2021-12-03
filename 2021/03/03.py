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

# Recursion!?
# or maybe just discard entire columns?
ones = Counter()
zeroes = Counter()

remaining_numbers = inp
for idx in range(12):
    for line in remaining_numbers:
        if line[idx] == "0":
            zeroes[idx] += 1
        else:
            ones[idx] += 1

    if ones[idx] - zeroes[idx] >= 0:
        # one most common
        most_common = "1"
        least_common = "0"
    else:
        most_common = "0"
        least_common = "1"
    # Remove lines from remaining numbers
    new_remaining_numbers = []
    for line in remaining_numbers:
        if line[idx] == most_common:
            new_remaining_numbers.append(line)

    remaining_numbers = new_remaining_numbers.copy()

oxygen = int(str(remaining_numbers[0]), 2)
print(oxygen)
ones = Counter()
zeroes = Counter()

remaining_numbers = inp
for idx in range(12):
    for line in remaining_numbers:
        if line[idx] == "0":
            zeroes[idx] += 1
        else:
            ones[idx] += 1

    if ones[idx] - zeroes[idx] >= 0:
        # one most common
        most_common = "1"
        least_common = "0"
    else:
        most_common = "0"
        least_common = "1"
    # Remove lines from remaining numbers
    new_remaining_numbers = []
    for line in remaining_numbers:
        if line[idx] == least_common:
            new_remaining_numbers.append(line)

    remaining_numbers = new_remaining_numbers.copy()
    if len(remaining_numbers) == 1:
        break

scrubber = int(str(remaining_numbers[0]), 2)
print("Part 2:")
print(oxygen * scrubber)
