import util
from collections import Counter

inp = util.input_as_lines("input")


def get_remaining_string(str, skip):
    new_str = ""
    for idx, char in enumerate(str):
        if idx not in skip:
            new_str += char
    return new_str


sign_matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
illegal_count = Counter()
illegal_values = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
open_signs = ["(", "[", "{", "<"]
closed_signs = [
    ")",
    "]",
    "}",
    ">",
]
remaining_lines = []
for line in inp:
    print(line)
    skip_indexes = []  # since they have been closed
    corrupt_line = False
    for idx, char in enumerate(line):
        if char in closed_signs:
            # check backwards, until it matches an opened, if it doesnt, its corrupt
            found_match = False
            for i in range(idx - 1, -1, -1):
                if i not in skip_indexes:
                    if line[i] != sign_matching[char]:
                        print(f"Found wrong char: {line[i]}")
                        break
                    if line[i] == sign_matching[char]:
                        skip_indexes.append(i)
                        skip_indexes.append(idx)
                        found_match = True
                        break
            if not found_match:
                print(f"no match found for {char} at {idx}")
                print(skip_indexes)
                illegal_count[char] += 1
                corrupt_line = True
                break
    if corrupt_line:
        print("Line was corrupt, skipping")
    else:
        print("remaining line was:")
        print(get_remaining_string(line, skip_indexes))
        remaining_lines.append(get_remaining_string(line, skip_indexes))


def get_score(str):
    score_table = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for char in str:
        score = score * 5
        score += score_table[char]
    return score


scores = []
for line in remaining_lines:
    matching_line = ""
    for char in reversed(line):
        matching_line += sign_matching[char]
    print(matching_line)
    print(get_score(matching_line))
    scores.append(get_score(matching_line))

import statistics

illegal_sum = 0
for illegal in illegal_count.elements():
    illegal_sum += illegal_values[illegal]
print("Answer part 1:")
print(illegal_sum)
print("Answer part 2:")
print(statistics.median(scores))
