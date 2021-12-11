file = open("input", "r")

database = file.read().splitlines()

# database = """939
# 7,13,x,x,59,x,31,19
# """
# database = """939
# 17,13
# """
# database = """939
# 17,x,13,19
# """

# database = database.splitlines()

timestamp = int(database[0])
buses = list(database[1].split(","))
# part 1
buses = [int(bus) for bus in buses if bus != "x"]

bus_factors = []
bus_dict = {}
import math

for bus in buses:
    bus_factors.append(math.ceil(timestamp / bus) * bus)
    bus_dict[bus] = math.ceil(timestamp / bus) * bus

print(bus_factors)
min_bus_time = min(bus_factors)
chosen_bus = None
for key, value in bus_dict.items():
    if value == min_bus_time:
        chosen_bus = key

print(f"chosen_bus: {chosen_bus}")

waiting_time = min_bus_time - timestamp
print(f"waiting: {waiting_time}")
print(waiting_time * chosen_bus)

# part 2
# Chinese remainder theorem!
buses = list(database[1].split(","))
bus_timestamp = {}
for index, bus in enumerate(buses):
    if bus != "x":
        bus_timestamp[int(bus)] = (int(bus) - index) % int(bus)

print(bus_timestamp)

# find nums that make a remainder 1 for each:
import math
import time

start = time.time()
bus_what_to_mod = {}
result_dict = {}
for key_to_check, value_to_check in bus_timestamp.items():
    print(f"checking: {key_to_check}")
    multiply = []
    for key, value in bus_timestamp.items():
        if key != key_to_check:
            multiply.append(key)
    multiply_base = math.prod(multiply)
    for i in range(0, key_to_check):
        result = multiply_base * i
        if result % key_to_check == 1:
            result_dict[key_to_check] = result
            break

print(result_dict)
result_sum = 0

for key, result in result_dict.items():
    result_sum += result * bus_timestamp[key]

print(result_sum)
what_to_mod = 1
for key, value in bus_timestamp.items():
    what_to_mod = what_to_mod * key

print(result_sum % what_to_mod)
end = time.time()
print(f"took: {end - start}s")