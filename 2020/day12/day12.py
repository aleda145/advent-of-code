# database = """F10
# N3
# F7
# R90
# F11
# """

# database = database.splitlines()

file = open("input", "r")

database = file.read().splitlines()

east_west_pos = 0  # east is pos, west is neg
north_south_pos = 0  # north is pos, south is neg
facing = "E"

east_west_waypoint = 10  # east is pos, west is neg
north_south_waypoint = 1  # north is pos, south is neg


def calc_facing(cur_facing, left_or_right, degrees):
    facing_dict = {"E": 0, "S": 90, "W": 180, "N": 270}

    cur_deg = facing_dict[cur_facing]
    if left_or_right == "L":
        new_deg = cur_deg - degrees
    elif left_or_right == "R":
        new_deg = cur_deg + degrees
    new_deg = new_deg % 360
    for key, val in facing_dict.items():
        if val == new_deg:
            return key


def rotate_waypoint(cur_east_west_wp, cur_north_south_wp, left_or_right, degrees):
    new_east_west_wp = None
    new_north_south_wp = None

    if left_or_right == "L":
        new_deg = -1 * degrees
    elif left_or_right == "R":
        new_deg = degrees
    new_deg = new_deg % 360  # rotate by this much!

    if new_deg == 90:
        new_east_west_wp = cur_north_south_wp
        new_north_south_wp = -1 * cur_east_west_wp
    elif new_deg == 180:
        new_east_west_wp = -1 * cur_east_west_wp
        new_north_south_wp = -1 * cur_north_south_wp
    elif new_deg == 270:
        new_east_west_wp = -1 * cur_north_south_wp
        new_north_south_wp = cur_east_west_wp
    if new_east_west_wp == None or new_north_south_wp == None:
        raise ValueError
    print(f"old wp was: {cur_east_west_wp}, {cur_north_south_wp}")
    print(f"new is: {new_east_west_wp}, {new_north_south_wp}")
    return new_east_west_wp, new_north_south_wp


for instruction in database:
    command = instruction[0]
    value = int(instruction[1:])
    print(f"command: {command} value: {value}")
    if command == "N":
        north_south_waypoint += value
    elif command == "S":
        north_south_waypoint -= value
    elif command == "E":
        east_west_waypoint += value
    elif command == "W":
        east_west_waypoint -= value
    elif command == "L" or command == "R":
        # facing = calc_facing(facing, command, value)
        east_west_waypoint, north_south_waypoint = rotate_waypoint(
            east_west_waypoint, north_south_waypoint, command, value
        )
        # rotate_waypoint(east_west_waypoint, north_south_waypoint, command, value)
    elif command == "F":
        print(f"move from {east_west_pos}, {north_south_pos}")
        east_west_pos = east_west_waypoint * value + east_west_pos
        north_south_pos = north_south_waypoint * value + north_south_pos
        print(f"to {east_west_pos}, {north_south_pos}")
print(abs(east_west_pos) + abs(north_south_pos))
