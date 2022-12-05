import util
import re

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

parse_crates = True
parse_instructions = False
crates = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
}
instructions = []
for line in inp:
    if parse_crates:
        if line[1] == "1":
            parse_crates = False
            parse_instructions = True
            print(f"parsed starting: {crates}")

        if line[1] != " ":
            crates["1"].insert(0, line[1])
        if line[5] != " ":
            crates["2"].insert(0, line[5])
        if line[9] != " ":
            crates["3"].insert(0, line[9])
        if line[13] != " ":
            crates["4"].insert(0, line[13])
        if line[17] != " ":
            crates["5"].insert(0, line[17])
        if line[21] != " ":
            crates["6"].insert(0, line[21])
        if line[25] != " ":
            crates["7"].insert(0, line[25])
        if line[29] != " ":
            crates["8"].insert(0, line[29])
        if line[33] != " ":
            crates["9"].insert(0, line[33])
    if parse_instructions and line[0:1] == "m":
        num_to_move = re.search("move (.*) from", line).group(1)
        move_from = re.search("from (.*) to", line).group(1)
        move_to = re.search("to (.*)", line).group(1)
        instructions.append([num_to_move, move_from, move_to])
print(instructions)
for instruction in instructions:
    for num in range(0, int(instruction[0])):
        crate_to_move = crates[instruction[1]].pop()
        crates[instruction[2]].append(crate_to_move)
print(crates)

message = ""
for k, v in crates.items():
    message += v[-1]

print(f"part1: {message}")

parse_crates = True
parse_instructions = False
crates = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
}
instructions = []
for line in inp:
    if parse_crates:
        if line[1] == "1":
            parse_crates = False
            parse_instructions = True
            print(f"parsed starting: {crates}")

        if line[1] != " ":
            crates["1"].insert(0, line[1])
        if line[5] != " ":
            crates["2"].insert(0, line[5])
        if line[9] != " ":
            crates["3"].insert(0, line[9])
        if line[13] != " ":
            crates["4"].insert(0, line[13])
        if line[17] != " ":
            crates["5"].insert(0, line[17])
        if line[21] != " ":
            crates["6"].insert(0, line[21])
        if line[25] != " ":
            crates["7"].insert(0, line[25])
        if line[29] != " ":
            crates["8"].insert(0, line[29])
        if line[33] != " ":
            crates["9"].insert(0, line[33])
    if parse_instructions and line[0:1] == "m":
        num_to_move = re.search("move (.*) from", line).group(1)
        move_from = re.search("from (.*) to", line).group(1)
        move_to = re.search("to (.*)", line).group(1)
        instructions.append([num_to_move, move_from, move_to])
print(instructions)
for instruction in instructions:
    popped_crates = []
    for num in range(0, int(instruction[0])):
        popped_crates.append(crates[instruction[1]].pop())
    for crate in reversed(popped_crates):
        crates[instruction[2]].append(crate)
print(crates)

message = ""
for k, v in crates.items():
    message += v[-1]
print(f"{message}")
