file = open("input", "r")

database = file.read().splitlines()
# database = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL", "BBBBBBBRRR"]


def find_place(cur_row_lower, cur_row_upper, row_input):
    if row_input == "":
        assert cur_row_lower == cur_row_upper
        return cur_row_upper
    else:
        if row_input[0] in ["F", "L"]:
            return find_place(
                cur_row_lower,
                int(cur_row_lower + ((cur_row_upper - cur_row_lower) / 2)),
                row_input[1:],
            )
        elif row_input[0] in ["B", "R"]:
            return find_place(
                int((cur_row_lower + 1 + cur_row_upper) / 2),
                cur_row_upper,
                row_input[1:],
            )


def get_seat_id(row, column):
    return row * 8 + column


seat_ids = []
for boarding_pass in database:
    print(boarding_pass)
    row = find_place(0, 127, boarding_pass[0:7])
    print(row)
    col = find_place(0, 7, boarding_pass[7:])
    print(col)
    seat_ids.append(get_seat_id(row, col))

    # find_column(boarding_pass)
print(seat_ids)
print(max(seat_ids))

# find missing seat:

sorted_seats = sorted(seat_ids)

print(sorted_seats)

for idx, seat in enumerate(sorted_seats):
    if seat + 1 != sorted_seats[idx + 1]:
        print(seat + 1)
        break