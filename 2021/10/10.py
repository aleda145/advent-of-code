import util
from collections import Counter

inp = util.input_as_lines("input")


def get_remaining_string(str, skip):
    new_str = ""
    for idx, char in enumerate(str):
        if idx not in skip:
            new_str += char
    return new_str


sign_matching = {")": "(", "]": "[", "}": "{", ">": "<"}
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
for line in inp:
    signs_opened = {
        "(": 0,
        "[": 0,
        "{": 0,
        "<": 0,
    }

    signs_closed = {
        ")": 0,
        "]": 0,
        "}": 0,
        ">": 0,
    }
    print(line)
    skip_indexes = []  # since they have been closed
    for idx, char in enumerate(line):

        if char in open_signs:
            signs_opened[char] += 1
        elif char in closed_signs:
            signs_closed[char] += 1
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
                break
    print("remaining line was:")
    print(get_remaining_string(line, skip_indexes))

    # if signs_opened[sign_matching[char]] - signs_closed[char] < 0:
    #    print(f"corrupt {char}!")

    # break
print(signs_opened)
print(signs_closed)

print(illegal_count)
illegal_sum = 0
for illegal in illegal_count.elements():
    illegal_sum += illegal_values[illegal]

print(illegal_sum)
