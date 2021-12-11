database = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""
database = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""
database = database.splitlines()
file = open("input", "r")

database = file.read().splitlines()

from collections import defaultdict

checking_req = True
checking_my_ticket = False
checking_nearby_ticket = False
req_dict = {}
ticket_dict = {}
ticket_num = 0
my_ticket = None
for row in database:
    if checking_req:
        if "" == row:
            checking_req = False
            checking_my_ticket = True
            continue
        split_req = row.split(":")
        ranges = split_req[1].replace(" ", "").split("or")
        req_dict[split_req[0]] = ranges
    if checking_my_ticket:
        if "" == row:
            checking_my_ticket = False
            checking_nearby_ticket = True
            continue
        my_ticket = row.split(",")
    if checking_nearby_ticket and row != "nearby tickets:":
        ticket_dict[ticket_num] = row.split(",")
        ticket_num += 1


print(req_dict)
print(ticket_dict)
range_dict = defaultdict(list)
possible_ranges = []
for key, val in req_dict.items():
    print(key)
    for ticket_range in val:
        print(ticket_range)
        lower = int(ticket_range.split("-")[0])
        upper = int(ticket_range.split("-")[1])
        range_dict[key].append(range(lower, (upper + 1)))
        possible_ranges.append(range(lower, (upper + 1)))
print(possible_ranges)
invalid_range = []
invalid_tickets = []
for ticket, ticket_ranges in ticket_dict.items():
    print(f"{ticket}, ranges: {ticket_ranges}")
    for ticket_range in ticket_ranges:
        if (any([int(ticket_range) in rng for rng in possible_ranges])) == False:
            invalid_range.append(int(ticket_range))
            invalid_tickets.append(ticket)
# part 1
print(invalid_range)
print(sum(invalid_range))

# part 2:
print(invalid_tickets)
for invalid_ticket in invalid_tickets:
    ticket_dict.pop(invalid_ticket, None)

print(range_dict)
print(ticket_dict)
column = [set() for _ in range(len(my_ticket))]
for ticket, val in ticket_dict.items():
    for idx, num in enumerate(val):
        column[idx].add(int(num))
print(column)

# Now find which column can NOT be which field?
not_idx_dict = defaultdict(list)
for idx, col in enumerate(column):
    print(col)
    for col_val in col:
        for key, val in range_dict.items():
            if (any([col_val in rng for rng in val])) == False:
                print(f"{col} is not {key}")
                not_idx_dict[idx].append(key)
    if not not_idx_dict[idx]:  # add nothing, makes it easier to compare later
        not_idx_dict[idx].append("")

# we know now that this column can NOT be these
# do elimination
ticket_keys = set(range_dict.keys())
print(ticket_keys)
print(not_idx_dict)
picked_descriptions = {}
added_descriptions = set()
match = 1
while len(picked_descriptions) < len(not_idx_dict):
    for key, val in not_idx_dict.items():
        possible_description = ticket_keys - set(val)
        print(f"{key} can be {possible_description}")
        if len(possible_description) == match:
            picked_descriptions[key] = possible_description - added_descriptions
            added_descriptions.update(possible_description)
            match += 1
print(picked_descriptions)

my_departure_ticket_indexes = []
for key, val in picked_descriptions.items():
    if "departure" in repr(val):  # repr make stringy
        my_departure_ticket_indexes.append(key)

print(my_departure_ticket_indexes)

values_to_multiply = []

for idx in my_departure_ticket_indexes:
    values_to_multiply.append(int(my_ticket[idx]))
print(values_to_multiply)
import math

print(math.prod(values_to_multiply))