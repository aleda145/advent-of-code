file = open("input", "r")

database = file.read().splitlines()

# database = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """

# database = database.splitlines()

# top left is x=0, y=0
# x is first, y is second


def get_adjacent_seats(seat_pos):
    up_seat = (seat_pos[0], seat_pos[1] - 1)
    down_seat = (seat_pos[0], seat_pos[1] + 1)
    left_seat = (seat_pos[0] - 1, seat_pos[1])
    right_seat = (seat_pos[0] + 1, seat_pos[1])

    up_left_seat = (seat_pos[0] - 1, seat_pos[1] - 1)
    up_right_seat = (seat_pos[0] + 1, seat_pos[1] - 1)
    down_left_seat = (seat_pos[0] - 1, seat_pos[1] + 1)
    down_right_seat = (seat_pos[0] + 1, seat_pos[1] + 1)

    return [
        up_seat,
        down_seat,
        left_seat,
        right_seat,
        up_left_seat,
        up_right_seat,
        down_left_seat,
        down_right_seat,
    ]


def get_visible_seats(seat_pos, seat_dictionary):
    # get up seats:
    up_seat = seat_pos
    down_seat = seat_pos
    left_seat = seat_pos
    right_seat = seat_pos

    up_left_seat = seat_pos
    up_right_seat = seat_pos
    down_left_seat = seat_pos
    down_right_seat = seat_pos

    # print(f"examining seat {seat_pos}")

    visible_seats = {}
    cur_seats_dict = {}
    looking_for_seats = True

    for i in range(0, 100):
        up_seat = (up_seat[0], up_seat[1] - 1)
        down_seat = (down_seat[0], down_seat[1] + 1)
        left_seat = (left_seat[0] - 1, left_seat[1])
        right_seat = (right_seat[0] + 1, right_seat[1])

        up_left_seat = (up_left_seat[0] - 1, up_left_seat[1] - 1)
        up_right_seat = (up_right_seat[0] + 1, up_right_seat[1] - 1)
        down_left_seat = (down_left_seat[0] - 1, down_left_seat[1] + 1)
        down_right_seat = (down_right_seat[0] + 1, down_right_seat[1] + 1)

        cur_seats_dict["up"] = up_seat
        cur_seats_dict["down"] = down_seat
        cur_seats_dict["left"] = left_seat
        cur_seats_dict["right"] = right_seat

        cur_seats_dict["up_left"] = up_left_seat
        cur_seats_dict["up_right"] = up_right_seat
        cur_seats_dict["down_left"] = down_left_seat
        cur_seats_dict["down_right"] = down_right_seat

        for key, cur_seat in cur_seats_dict.items():
            if cur_seat in seat_dictionary:
                if key not in visible_seats:
                    if seat_dictionary[cur_seat] != ".":
                        # print(f"found visible {cur_seat}")
                        visible_seats[key] = cur_seat

    return list(visible_seats.values())


def count_num_adjacent_occupied(seat_dictionary, adjacents):
    occupied = 0
    for adjacent_seat in adjacents:
        if adjacent_seat in seat_dictionary:
            if seat_dictionary[adjacent_seat] == "#":
                occupied += 1

    return occupied


print(get_adjacent_seats([5, 5]))

seat_dict = {}  # dictionary with tuple as key and value is seat
for row_index, row in enumerate(database):
    for column_index, seat in enumerate(row):
        seat_dict[(column_index, row_index)] = seat

print(seat_dict)

new_seat_dict = {}
num_runs = 0
while True:
    for seat_position, value in seat_dict.items():
        # adjacent_seats = get_adjacent_seats(seat_position)
        if value != ".":
            adjacent_seats = get_visible_seats(seat_position, seat_dict)

            new_seat_dict[seat_position] = seat_dict[seat_position]
            if value == "L":
                if count_num_adjacent_occupied(seat_dict, adjacent_seats) == 0:
                    new_seat_dict[seat_position] = "#"
            elif value == "#":
                if count_num_adjacent_occupied(seat_dict, adjacent_seats) >= 5:
                    new_seat_dict[seat_position] = "L"

    if new_seat_dict == seat_dict:
        print("Stabilized")
        break
    print(f"Run:{num_runs}")
    num_runs += 1
    seat_dict = new_seat_dict.copy()
    # list_of_seat_lists = []
    # seat_list = []
    # for key, value in new_seat_dict.items():
    #     seat_list.append(value)
    #     if key[1] == 9:
    #         list_of_seat_lists.append(seat_list)
    #         seat_list = []
    # print("")
    # for s_list in list_of_seat_lists:
    #     print("".join(s_list))
    # print("")


occupied_seats = 0
for key, value in new_seat_dict.items():
    if value == "#":
        occupied_seats += 1

print(occupied_seats)