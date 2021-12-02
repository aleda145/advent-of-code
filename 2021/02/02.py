import util

inp = util.input_as_lines("input")
# print(inp)
horizontal = 0
depth = 0
for line in inp:
    direction = line.split(" ")[0]
    value = int(line.split(" ")[1])

    if direction == "forward":
        horizontal += value
    elif direction == "up":
        depth -= value
    elif direction == "down":
        depth += value

print(depth * horizontal)


horizontal = 0
aim = 0
depth = 0
for line in inp:
    direction = line.split(" ")[0]
    value = int(line.split(" ")[1])

    if direction == "forward":
        horizontal += value
        depth += value * aim
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value

print(depth * horizontal)
