import util
from collections import Counter

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")
sample2 = util.input_as_lines("sample2")


def get_adjacent(list_of_coords):
    x_min = list_of_coords[0][0]
    x_max = list_of_coords[len(list_of_coords) - 1][0]
    y = list_of_coords[0][1]
    radius_coords = []
    for r in range(x_min, x_max + 1):

        radius_coords.append([r - 1, y - 1])
        radius_coords.append([r, y - 1])
        radius_coords.append([r + 1, y - 1])
        radius_coords.append([r - 1, y])
        radius_coords.append([r + 1, y])
        radius_coords.append([r - 1, y + 1])
        radius_coords.append([r, y + 1])
        radius_coords.append([r + 1, y + 1])
    return radius_coords


coords = {}
symbols = []
cnt = Counter()
sum = 0
for y, line in enumerate(inp):
    number_coords = []
    number = ""
    for x, char in enumerate(line):
        if char != "." and not char.isnumeric():
            symbols.append([x, y])
for y, line in enumerate(inp):
    number_coords = []
    number = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            print(char)
            number_coords.append([x, y])
            number += char
            if x != len(line) - 1:
                continue
        # if char != ".":
        #     symbols.append((x, y))
        # check if there are any adjacent symbols
        if number_coords:
            check_coords = get_adjacent(number_coords)
            print(f"checking {number}")
            for check_coord in check_coords:
                if check_coord in symbols:
                    print("found")
                    print(number)
                    sum += int(number)
                    break
        # if number:
        #     cnt[number] += 1
        number_coords = []
        number = ""

print(sum)

# print(coords)
# print(symbols)

# part_numbers_sum = 0
# added_numbers = []
# for symbol in symbols:
#     check_coords = []
#     check_coords.append([symbol[0] - 1, symbol[1] - 1])
#     check_coords.append([symbol[0], symbol[1] - 1])
#     check_coords.append([symbol[0] + 1, symbol[1] - 1])
#     check_coords.append([symbol[0] - 1, symbol[1]])
#     check_coords.append([symbol[0] + 1, symbol[1]])
#     check_coords.append([symbol[0] - 1, symbol[1] + 1])
#     check_coords.append([symbol[0], symbol[1] + 1])
#     check_coords.append([symbol[0] + 1, symbol[1] + 1])
#     for coord in check_coords:
#         if tuple(coord) in coords:
#             check_number = coords[tuple(coord)]
#             if cnt[str(check_number)] > 0:
#                 part_numbers_sum += check_number
#                 cnt[str(check_number)] -= 1

# # print(check_coords)
# # print(cnt)
# # print(cnt)
# # print(part_numbers_sum)
