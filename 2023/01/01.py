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

# replace substrings to numeric and then run the first solution again
num_list = []
for line in inp:
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eighth8eight")
    line = line.replace("nine", "nine9nine")
    line_nums = ""
    print(line)
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
