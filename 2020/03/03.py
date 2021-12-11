file = open("input","r")

database = file.read().splitlines()
map_list = []
# load input
for row in database:
    row_map = []
    for obstacle in row:
        row_map.append(obstacle)
    map_list.append(row_map)
    
trees = 0
current_index = 0


indexes = [1,3,5,7,1]
trees_list = []
for enum_ind, ind in enumerate(indexes):
    trees = 0
    current_index = 0
    for index, row in enumerate(map_list):
        if enum_ind == 4:
            if index % 2 == 0:
                if row[current_index] == "#":
                    trees=trees+1
                current_index = current_index + 1
                if current_index >= len(row):
                    current_index = current_index - len(row)
        else:
            if row[current_index] == "#":
                trees=trees+1
            current_index = current_index + ind
            if current_index >= len(row):
                current_index = current_index - len(row)
    trees_list.append(trees)

print(trees_list)
from functools import reduce
print(reduce(lambda x,y: x*y, trees_list))
