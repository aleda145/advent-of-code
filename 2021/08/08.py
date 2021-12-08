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

output_sum = 0

for idx, entry in enumerate(display_input):
    input_map = {}
    number_to_input = {}
    for number in entry.split(" "):
        num_chars = len(number)
        if num_chars == 2:
            input_map["".join(sorted(number))] = 1
            number_to_input[1] = number
        elif num_chars == 3:
            input_map["".join(sorted(number))] = 7
            number_to_input[7] = number
        elif num_chars == 4:
            input_map["".join(sorted(number))] = 4
            number_to_input[4] = number
        elif num_chars == 7:
            input_map["".join(sorted(number))] = 8
            number_to_input[8] = number
    for number in entry.split(" "):
        num_chars = len(number)
        if num_chars == 5:
            # can be 5, 2 or 3
            the_four = number_to_input[4]
            for char in number_to_input[1]:
                the_four = the_four.replace(char, "")
            # if num 1 is in the pattern, its a 3
            if number_to_input[1][0] in number and number_to_input[1][1] in number:
                input_map["".join(sorted(number))] = 3
                number_to_input[3] = number
            # remove the 1 from the four, if that is in the pattern its a 5
            elif the_four[0] in number and the_four[1] in number:
                input_map["".join(sorted(number))] = 5
            else:
                input_map["".join(sorted(number))] = 2

    for number in entry.split(" "):
        num_chars = len(number)
        if num_chars == 6:
            # can be 9, 6 or 0
            # 6 does not have the entire 1 in it
            # removing 1 means we have 4 segments left
            check_if_six = number
            for char in number_to_input[1]:
                check_if_six = check_if_six.replace(char, "")

            # 0 does not have the entire 3 in it
            # removing 3 means 2 segments left
            check_if_zero = number
            for char in number_to_input[3]:
                check_if_zero = check_if_zero.replace(char, "")

            if len(check_if_six) == 5:
                input_map["".join(sorted(number))] = 6
            elif len(check_if_zero) == 2:
                input_map["".join(sorted(number))] = 0
            else:
                input_map["".join(sorted(number))] = 9
    # now use input map for output
    print(input_map)
    output_number = ""
    for number in display_output[idx].split(" "):
        output_number += str(input_map["".join(sorted(number))])
    output_sum += int(output_number)
    print(output_number)
print(output_sum)
