from typing import Counter
import util

inp = util.input_as_lines("input")
fish_list = [int(x) for x in inp[0].split(",")]
# print(fish_list)


def fish_cycle(fishes):
    old_fishes = []
    new_fishes = []
    for fish in fishes:
        if fish == 0:
            old_fishes.append(6)
            new_fishes.append(8)
        else:
            old_fishes.append(fish - 1)
    return old_fishes + new_fishes


print(f"Initial State {fish_list}")
for day in range(1, 257):
    fish_list = fish_cycle(fish_list).copy()
    # print(f"After {day} day: {fish_list}")
    print(f"After {day}: {len(fish_list)}")
