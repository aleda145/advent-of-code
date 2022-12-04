import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

pairs = 0

for line in inp:
    left, right = line.split(",")
    left_set = set(range(int(left.split("-")[0]), int(left.split("-")[1]) + 1))
    right_set = set(range(int(right.split("-")[0]), int(right.split("-")[1]) + 1))

    if len(left_set) > len(right_set):
        if right_set.issubset(left_set):
            pairs += 1
    else:
        if left_set.issubset(right_set):
            pairs += 1

print(f"part1: {pairs}")
overlaps = 0
for line in inp:
    left, right = line.split(",")
    left_set = set(range(int(left.split("-")[0]), int(left.split("-")[1]) + 1))
    right_set = set(range(int(right.split("-")[0]), int(right.split("-")[1]) + 1))
    if len(left_set & right_set) > 0:
        overlaps += 1
print(f"part2: {overlaps}")
