import util
import math

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

max_num_cubes = {"red": 12, "green": 13, "blue": 14}

invalid_id = 0
all_ids = 0
for line in inp:
    print(line)
    game, bags = line.split(":")
    game_id = game.split(" ")[1]
    print(game_id)
    all_ids += int(game_id)
    # maybe needed part two?
    # sub_sets = bags.strip(" ").split(";")
    # for sub_set in sub_sets:
    #     print(sub_set)
    #     print(sub_set.split(","))
    cubes = bags.replace(",", ";").split(";")
    for cube in cubes:
        cube_num, cube_color = cube.strip(" ").split(" ")
        print(cube_num, cube_color)
        if int(cube_num) > max_num_cubes[cube_color]:
            print("invalid")
            invalid_id += int(game_id)
            break
print(all_ids - invalid_id)

products = 0
for line in inp:
    print(line)
    game, bags = line.split(":")
    game_id = game.split(" ")[1]
    print(game_id)
    all_ids += int(game_id)
    cubes = bags.replace(",", ";").split(";")
    smallest = {"green": 0, "blue": 0, "red": 0}
    for cube in cubes:
        cube_num, cube_color = cube.strip(" ").split(" ")
        if int(cube_num) > smallest[cube_color]:
            smallest[cube_color] = int(cube_num)
    print(smallest)
    products += math.prod(smallest.values())

print(products)
