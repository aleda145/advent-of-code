import util
inp = util.input_as_lines("input")
# sample = util.input_as_lines("sample_input")
left_list = []
right_list = []
for row in inp:
    split_lines = row.split("   ")
    left, right = split_lines[0], split_lines[1]
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

zipped = zip(left_list, right_list)

diff_sum = 0
for val in zipped:
    diff_sum += abs(val[0]-val[1])
print(diff_sum)

from collections import Counter
count = Counter(right_list)
sim_sum = 0
for val in left_list:
    sim_sum += val*count[val]
print(sim_sum)