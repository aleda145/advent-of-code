# make 3 dimensional grid
# x,y,z
# list of lists that are [x,y,z]


def get_neighbors(pos):
    # can diff by at most one!
    pos = eval(pos)  # eval it to a list
    x = int(pos[0])
    y = int(pos[1])
    z = int(pos[2])
    w = int(pos[3])
    possible_x = [x - 1, x, x + 1]
    possible_y = [y - 1, y, y + 1]
    possible_z = [z - 1, z, z + 1]
    possible_w = [w - 1, w, w + 1]
    neighbors = []
    for pos_x in possible_x:
        for pos_y in possible_y:
            for pos_z in possible_z:
                for pos_w in possible_w:
                    if pos_x != x or pos_y != y or pos_z != z or pos_w != w:
                        # dont add itself
                        neighbors.append([pos_x, pos_y, pos_z, pos_w])

    return neighbors


def print_grid(the_grid):
    keys = []
    for key in the_grid.keys():
        keys.append(eval(key))
    from operator import itemgetter

    keys = sorted(keys, key=itemgetter(3, 2, 1, 0))
    cur_w = keys[0][3]
    cur_z = keys[0][2]
    cur_y = [keys[0][1]]
    print(f"z={cur_z}")
    print(f"w={cur_w}")
    for key in keys:
        if cur_w != key[3]:
            cur_w = key[3]
        if cur_z != key[2]:
            print("\n")
            cur_z = key[2]
            print(f"z={cur_z}")
            print(f"w={cur_w}")
        if cur_y != key[1]:
            print("")
            cur_y = key[1]
        print(the_grid[str(key)], end="")
    print("")


grid = {}

database = """.#.
..#
###
"""

database = database.splitlines()

file = open("input", "r")

database = file.read().splitlines()

cycle = 0

print(database)
start_z = 0
start_w = 0
for y_idx, row in enumerate(database):
    for x_idx, col in enumerate(row):
        print(col)
        grid[str([x_idx, y_idx, start_z, start_w])] = col


for i in range(0, 6):  # just do 6 cycles
    # add all neighbors to grid, give them inactive
    # if they are not in the grid!
    print(f"cur cycle :{i}")
    new_grid = grid.copy()
    for position, value in grid.items():
        for neighbor in get_neighbors(position):
            if str(neighbor) not in grid:
                new_grid[str(neighbor)] = "."

    new_new_grid = new_grid.copy()

    for position, value in new_grid.items():
        num_neighbors_active = 0
        for neighbor in get_neighbors(position):
            if str(neighbor) in new_grid:
                if new_grid[str(neighbor)] == "#":
                    num_neighbors_active += 1
        if value == "#" and num_neighbors_active not in [2, 3]:
            # then change it
            new_new_grid[position] = "."
        elif value == "." and num_neighbors_active == 3:
            # then change it
            new_new_grid[position] = "#"
        grid = new_new_grid.copy()
    print_grid(new_new_grid)

# print(grid)
# # print(new_grid)

# print_grid(grid)
# print_grid(new_grid)
count_active = 0
for key, value in new_new_grid.items():
    if value == "#":
        count_active += 1

print(count_active)
