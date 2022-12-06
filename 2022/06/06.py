import util

inp = util.input_as_string("input")
sample = util.input_as_string("sample_input")

chars = []

for idx, char in enumerate(inp):
    chars.append(char)
    if len(chars) > 4:
        chars.pop(0)
    if len(set(chars)) == 4:
        print(f"part1: {idx + 1}")
        break

chars = []
for idx, char in enumerate(inp):
    chars.append(char)
    if len(chars) > 14:
        chars.pop(0)
    if len(set(chars)) == 14:
        print(f"part2: {idx + 1}")
        break
