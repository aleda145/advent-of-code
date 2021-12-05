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
possible_wins_list = []
for key, value in boards.items():
    for line in value:
        print(line)
        print(line[::-1])
        possible_wins[str(line)] = key
        possible_wins[str(line[::-1])] = key
        possible_wins_list.append(line.copy())
        possible_wins_list.append(line.copy()[::-1])
# vertical
for key, value in boards.items():
    for i in range(0, 5):
        vertical_win = []
        for line in value:
            vertical_win.append(line[i])
        possible_wins[str(vertical_win)] = key
        possible_wins[str(vertical_win[::-1])] = key
        possible_wins_list.append(vertical_win.copy())
        possible_wins_list.append(vertical_win.copy()[::-1])

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


# We dont need to generate a permutation that has already been generated
# so lets keep it in memory, and not generate it again?
generated_permutations = []


def generate_permutation(seen_numbers, new_number):
    # if we have 1,2,3,4,5,
    # generate all those permutations,
    # then we also get a 6, so generate only the newly possible permutations
    # 1,2,3,4,6
    # 1,2,3,5,6 and so on
    pass


def winning_board():
    seen_numbers = []

    winning_board_order = []
    for i in numbers:
        print(f"new number: {i}")
        seen_numbers.append(i)
        for idx, possible_win in enumerate(possible_wins_list):
            if i in possible_win:
                print("the number is in that seq, replace with x")
                possible_wins_list[idx].append("x")
                if possible_wins_list[idx].count("x") == 5:
                    if possible_wins[str(possible_win[0:5])] not in winning_board_order:
                        print("winning board added!")
                        winning_board_order.append(
                            possible_wins[str(possible_win[0:5])]
                        )
                        if len(winning_board_order) == len(boards.keys()):

                            winning_number = i
                            winning_seen_numbers = seen_numbers
                            return (
                                winning_board_order[-1],
                                winning_number,
                                winning_seen_numbers,
                            )

    print(winning_board_order)


win_board, winning_number, seen_numbers = winning_board()
print(f"board num: {win_board} num: {winning_number} seen: {seen_numbers}")
# check which numbers are not in seen_numbers
unmarked = 0
print(boards[win_board])
for line in boards[win_board]:
    for num in line:
        if num not in seen_numbers and num != "x":
            unmarked += num
print(unmarked)
print(unmarked * winning_number)
