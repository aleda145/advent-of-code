import util

inp = util.input_as_lines("input")

display_input = []
display_output = []
for line in inp:
    display_input.append(line.split(" | ")[0])
    display_output.append(line.split(" | ")[1])

print(display_output)
# convert output to num chars
answer = 0
for entry in display_output:
    for number in entry.split(" "):
        num_chars = len(number)
        if num_chars in [2, 3, 4, 7]:
            answer += 1
print(answer)
