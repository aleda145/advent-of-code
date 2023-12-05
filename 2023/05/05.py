import util
from collections import defaultdict

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")


def almanac_checker(number, destination_range, source_range, range_length):
    # 79 should be in 52,50,48 because 79 is in [50, (50+48 = 98)] range.
    # Then just add the diff (52-50) to 79 to get 81

    min_source = source_range
    max_source = source_range + range_length - 1
    if min_source <= number <= max_source:
        diff = destination_range - source_range
        return number + diff
    return False


print(almanac_checker(79, 50, 98, 2))
print(almanac_checker(53, 52, 50, 48))

seeds = [79, 14, 55, 13]


# If false for all in the map, then new value is just the same
current_objects = []
current_maps = []
for line in inp:
    colon_split = line.split(":")
    if colon_split[0] == "seeds":
        current_objects = [int(x) for x in colon_split[1].strip().split(" ")]
    elif colon_split[0].split(" ")[-1] == "map":
        print("new map")
    elif line == "" or line == inp[-1]:
        # check current objects
        for idx, current_object in enumerate(current_objects):
            for current_map in current_maps:
                return_value = almanac_checker(
                    current_object, current_map[0], current_map[1], current_map[2]
                )
                if return_value:
                    current_objects[idx] = return_value
                    break
        current_maps = []
        print(current_objects)
    else:
        current_maps.append([int(x) for x in line.strip().split(" ")])
    if line == inp[-1]:
        print("finish")
        print(min(current_objects))
