import util

inp = util.input_as_string("input")

floor = 0
for idx, char in enumerate(inp):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
print(floor)
