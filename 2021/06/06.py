import util
from collections import defaultdict

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
# fish_sum

fish_sum = len(fish_list)  # original fishes
# fish_sum = 1
# fish_list = [3]
# fish_list = [3]
new_fishes = defaultdict(int)
adult_fishes = defaultdict(int)
# add fish_list to adult_fishes
for spawn_days in range(0, 256, 7):
    for fish in fish_list:
        adult_fishes[fish - 6 + spawn_days] += 1
print(adult_fishes)
for day in range(0, 257):

    # adult fishes
    next_adult_hatch_day = day - 7
    if next_adult_hatch_day in adult_fishes.keys():
        new_young_fishes = adult_fishes[next_adult_hatch_day]
        print(f"Adding {new_young_fishes} new fishes")
        fish_sum += new_young_fishes
        new_fishes[day] += new_young_fishes

    # count new fishes once!
    next_young_hatch_day = day - 9
    if next_young_hatch_day in new_fishes.keys():
        new_adult_fishes = new_fishes[next_young_hatch_day]
        print(f"Converting to {new_adult_fishes} adult fishes")
        new_young_fishes = adult_fishes[next_young_hatch_day]
        print(f"Adding {new_young_fishes} new fishes")
        new_fishes[day] += new_young_fishes
        fish_sum += new_young_fishes

        for spawn_days in range(day, 256, 7):
            adult_fishes[spawn_days] += new_adult_fishes

    print(f"{day} : num {fish_sum}")
print(new_fishes)
print(adult_fishes)
print(fish_sum)
