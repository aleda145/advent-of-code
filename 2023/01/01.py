import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

num_list = []
for line in inp:
    line_nums = ""
    for char in line:
        if char.isnumeric():
            line_nums += char
            break
    for char in reversed(line):
        if char.isnumeric():
            line_nums += char
            break
    num_list.append(int(line_nums))
print(sum(num_list))
