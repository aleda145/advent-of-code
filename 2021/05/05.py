from typing import Counter
import util

inp = util.input_as_lines("input")
# print(inp)

seen_coords = Counter()

for line in inp:
    start_coord, end_coord = line.split(" -> ")
    x_start, y_start = [int(x) for x in start_coord.split(",")]
    x_end, y_end = [int(x) for x in end_coord.split(",")]
    if x_start == x_end:
        if y_start > y_end:
            y_start, y_end = y_end, y_start
        for y in range(y_start, y_end + 1):
            # print(f"{x_start},{y}")
            seen_coords[f"{x_start},{y}"] += 1
    elif y_start == y_end:
        if x_start > x_end:
            x_start, x_end = x_end, x_start
        for x in range(x_start, x_end + 1):
            # print(f"{x},{y_start}")
            seen_coords[f"{x},{y_start}"] += 1
    else:
        # 6,4 -> 2,0
        # swap?
        # 2, 0 -> 6,4
        #
        # 2, 0
        # 3, 1
        # 4, 2
        # 5, 3
        # 6, 4
        #
        # diagonal case
        if x_start > x_end:
            x_start, x_end = x_end, x_start
            y_start, y_end = y_end, y_start
        coords_moved = 0
        for x in range(x_start, x_end + 1):
            if y_start > y_end:
                print(f"{x},{y_start-coords_moved}")
                seen_coords[f"{x},{y_start-coords_moved}"] += 1
            else:
                print(f"{x},{y_start+coords_moved}")
                seen_coords[f"{x},{y_start+coords_moved}"] += 1
            coords_moved += 1

# print(seen_coords)
more_than_two = 0
for key, val in seen_coords.items():
    if val >= 2:
        more_than_two += 1
print(more_than_two)
