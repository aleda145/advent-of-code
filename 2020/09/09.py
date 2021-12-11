# database = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576"""

# database = database.splitlines()

file = open("input", "r")
database = file.read().splitlines()

preamble_num = 25


def get_possible_numbers(number_list):
    possible_nums = []
    for num_1 in number_list:
        for num_2 in number_list:
            if num_1 + num_2 not in possible_nums:
                possible_nums.append(num_1 + num_2)
    return possible_nums


def check_if_num_is_valid(number, previous):
    print(number)
    num_list = list(map(int, previous))
    possible_numbers = get_possible_numbers(num_list)
    possible_numbers.sort()
    print(possible_numbers)
    if number in possible_numbers:
        return True
    else:
        return False


# parta 1
for index, num in enumerate(database):
    if index < preamble_num:
        print(num)
    else:
        previous_num = database[index - preamble_num : index]
        if not check_if_num_is_valid(int(num), previous_num):
            print("found!")
            print(num)
            break


# part 2
# find continous sum of nums that is 21806024 (or 127 for test case)
# double hashmap? Try brute force first!


def count_sum(start_index, database, goal_num):
    cur_sum = 0
    for cur_index, num in enumerate(database[start_index:]):
        cur_sum += num
        if cur_sum == goal_num:
            print(cur_sum)
            print("found!")
            print("list was:")
            list_of_nums = database[start_index : cur_index + start_index + 1]
            print(list_of_nums)
            print("smallest in list was:")
            print(min(list_of_nums))
            print("largest in list was")
            print(max(list_of_nums))
            print("summed:")
            print(min(list_of_nums) + max(list_of_nums))
            return True
    return False


goal_num = 21806024
database = list(map(int, database))

for index, starting_num in enumerate(database):
    if count_sum(index, database, goal_num):
        break