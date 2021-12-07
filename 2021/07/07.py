import util

inp = util.input_as_lines("input")
crab_list = [int(x) for x in inp[0].split(",")]


# which crab position?
# test brute force
crab_list.sort()
print(crab_list)
first_possible = crab_list[0]
last_possible = crab_list[-1]

print(f"check range {first_possible}, {last_possible}")

best_crab_pos = None
best_crab_fuel = 9999999
for crab_pos in range(first_possible, last_possible):
    cur_crab_fuel = 0
    for crab in crab_list:
        cur_crab_fuel += abs(crab - crab_pos)
    print(f"pos: {crab_pos} used {cur_crab_fuel} fuel")
    if cur_crab_fuel < best_crab_fuel:
        best_crab_fuel = cur_crab_fuel
        best_crab_pos = crab_pos

print(f"Best crab pos was {best_crab_pos} with {best_crab_fuel} fuel")
