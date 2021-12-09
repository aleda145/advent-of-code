import util

inp = util.input_as_lines("input")

risk_level = 0

for y in range(len(inp)):
    for x in range(len(inp[y])):
        cur_height = inp[y][x]
        print(f"{x},{y} has height {cur_height}")
        # check all directions
        lower_than_north = False
        lower_than_south = False
        lower_than_east = False
        lower_than_west = False
        try:
            # North
            if cur_height < inp[y - 1][x]:
                lower_than_north = True
        except:
            # No index there, so it is automatically lower
            lower_than_north = True
        try:
            # south
            if cur_height < inp[y + 1][x]:
                lower_than_south = True
        except:
            # No index there, so it is automatically lower
            lower_than_south = True
        try:
            # east
            if cur_height < inp[y][x + 1]:
                lower_than_east = True
        except:
            # No index there, so it is automatically lower
            lower_than_east = True
        try:
            # west
            if cur_height < inp[y][x - 1]:
                lower_than_west = True
        except:
            # No index there, so it is automatically lower
            lower_than_west = True
        if (
            lower_than_north
            and lower_than_south
            and lower_than_east
            and lower_than_west
        ):
            risk_level += int(cur_height) + 1
print(risk_level)
