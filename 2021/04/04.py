from collections import defaultdict
import util

inp = util.input_as_lines("input")
# print(inp)
numbers = [int(x) for x in inp[0].split(",")]
board_number = -1

# boards are always 5x5
boards = defaultdict(list)
for line in inp[1:]:
    # print(line)
    if line == "":
        print("new board")
        board_number += 1
    else:
        print([int(x) for x in line.split()])
        boards[board_number].append([int(x) for x in line.split()])


possible_wins = defaultdict(int)
# horizontal
for key, value in boards.items():
    for line in value:
        print(line)
        print(line[::-1])
        possible_wins[str(line)] = key
        possible_wins[str(line[::-1])] = key
# vertical
for key, value in boards.items():
    for i in range(0, 5):
        vertical_win = []
        for line in value:
            vertical_win.append(line[i])
        possible_wins[str(vertical_win)] = key
        possible_wins[str(vertical_win[::-1])] = key

# diagonal
# they dont count lol
# for key, value in boards.items():
#     diagonal_win_down_right = []
#     diagonal_win_up_right = []
#     for i in range(0, 5):
#         diagonal_win_down_right.append(value[i][i])
#         diagonal_win_up_right.append(value[i][4 - i])

#     possible_wins[str(diagonal_win_down_right)] = key
#     possible_wins[str(diagonal_win_down_right[::-1])] = key
#     possible_wins[str(diagonal_win_up_right)] = key
#     possible_wins[str(diagonal_win_up_right[::-1])] = key

print(possible_wins)


def winning_board():
    seen_numbers = []
    from itertools import permutations

    for i in numbers:
        print(i)
        seen_numbers.append(i)
        if len(seen_numbers) >= 5:
            perms = permutations(seen_numbers, 5)
            for perm in list(perms):
                #    print(str(list(perm)))
                if str(list(perm)) in possible_wins:
                    print("found winning board!")
                    print(possible_wins[str(list(perm))])
                    return possible_wins[str(list(perm))], i, seen_numbers


win_board, winning_number, seen_numbers = winning_board()
print(winning_number)

# check which numbers are not in seen_numbers
unmarked = 0
for line in boards[win_board]:
    for num in line:
        if num not in seen_numbers:
            unmarked += num
print(unmarked)
print(unmarked * winning_number)
