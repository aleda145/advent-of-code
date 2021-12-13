import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

paper = {}
fold_instructions = []
for line in inp:
    if line:
        if "fold along" in line:
            fold_instruction = line.split("along ")[1]
            fold_instructions.append(fold_instruction)
        else:
            x, y = line.split(",")
            paper[(int(x), int(y))] = "."

print(paper)
og_paper = paper.copy()

for instruction in fold_instructions:
    print(instruction)
    axis, index = instruction.split("=")
    new_paper = {}
    if axis == "y":
        print("horizontal fold")
        # Add the dots that aren't affected:
        for coord in paper.keys():
            if coord[1] < int(index):
                new_paper[coord] = "."
            elif coord[1] > int(index):
                new_y = int(index) - (coord[1] - int(index))
                new_paper[coord[0], new_y] = "."
        print(new_paper)
        paper = new_paper.copy()
    elif axis == "x":
        # Add the dots that aren't affected:
        for coord in paper.keys():
            if coord[0] < int(index):
                new_paper[coord] = "."
            elif coord[0] > int(index):
                new_x = int(index) - (coord[0] - int(index))
                new_paper[new_x, coord[1]] = "."
        print(new_paper)
        paper = new_paper.copy()
import pprint

pprint.pprint(og_paper)
print(len(og_paper))
pprint.pprint(new_paper)
print(len(new_paper))

print(new_paper.keys())
x_values = []
y_values = []
for key in new_paper.keys():
    x_values.append(key[0])
    y_values.append(key[1])

for y in range(0, max(y_values) + 1):
    for x in range(0, max(x_values) + 1):
        if (x, y) in new_paper.keys():
            print("#", end="")
        else:
            print(".", end="")
    print("")
