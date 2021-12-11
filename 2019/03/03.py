

def trace_cable(cable, x_start, y_start,wire_num, steps_dict):
    x = 0
    y = 0 
    if cable[0] == 'R':
        # print("right")
        distance = int(cable[1:])
        # print(distance)
        for i in range(distance):
            x = x_start
            y = y_start+i+1

            rows[x][y] += wire_num
            steps_dict[x,y] = steps_dict[x,y-1]+1
    if cable[0] == 'L':
        # print("left")
        distance = int(cable[1:])

        # print(int(cable[1:]))
        for i in range(distance):
            x = x_start
            y = y_start-i-1

            rows[x][y] += wire_num
            steps_dict[x,y] = steps_dict[x,y+1]+1

    if cable[0] == 'D':
        # print("Down")
        distance = int(cable[1:])

        # print(int(cable[1:]))
        for i in range(distance):
            x = x_start+i+1
            y = y_start

            rows[x][y] += wire_num
            steps_dict[x,y] = steps_dict[x-1,y]+1

    if cable[0] == 'U':
        # print("up")
        distance = int(cable[1:])

        # print(int(cable[1:]))
        for i in range(distance):
            x = x_start-i-1
            y = y_start
            rows[x][y] += wire_num
            steps_dict[x,y] = steps_dict[x+1,y]+1
    return(x,y, steps_dict)

# index1 is height || (y)
# index 2 is --> length (x)
def find_intersections(rows):
    intersections = []
    for index1, row in enumerate(rows): 
        for index2, val in enumerate(row):
            if val == 3:
                print("found")
                print(index1)
                print(index2)
                intersections.append([index1,index2])
    return intersections

def find_closest_to_start(intersections, start):
    closest = 1000000000000
    for intersection in intersections:
        y = abs(start[0]- intersection[0])
   #     print(y)
        x = abs(start[1] - intersection[1])
  #      print(x)
        if (y+x) < closest: 
            closest = y+x 
    
    return closest

#trace_cable(test_cable1,10,0)

# for i in range(distance):
#     rows[0][-i] = 1


f = open("input","r")
cables=[]
for row in f:
    cables.append(row.split(","))
f.close()
print(cables)

#What is the Manhattan distance from the central port to the closest intersection?
print("first:")

print(cables[0])

print("second:")
print(cables[1])

# test_cable1 = ['R8','U5','L5','D3']
# test_cable2 = ['U7','R6','D4','L4']
# test_cable1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# test_cable2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# test_cable1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# test_cable2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

# cables[0] = test_cable1
# cables[1] = test_cable2
columns =[]
start_x = 10000
start_y = 10000
for i in range(int(start_x*2)):
    columns.append(0)
rows = []
for i in range(int(start_y*2)):
    rows.append(list(columns))


# for row in rows:
#     print(row)


# for row in rows:
#     print(row)

rows[start_x][start_y]=5
x = start_x
y = start_y
steps_dict_1 = {}
steps_dict_2 = {}
steps_dict_1[start_x, start_y] = 0 
steps_dict_2[start_x, start_y] = 0
for sub_cable in cables[0]:
    x, y, steps_dict_1 = trace_cable(sub_cable,x,y,1, steps_dict_1)

x = start_x
y = start_y
for sub_cable in cables[1]:
    x, y, steps_dict_2 = trace_cable(sub_cable,x,y,2,steps_dict_2)

# for row in rows:
#     print(row)

intersections = find_intersections(rows)

def steps_by_intersection(intersections):
    intersection_steps_list = []
    for intersection in intersections:
     #   print(steps_dict_1[intersection[0],intersection[1]])
      #  print(steps_dict_2[intersection[0],intersection[1]])
        steps_for_intersection = steps_dict_2[intersection[0],intersection[1]]+ steps_dict_1[intersection[0],intersection[1]]
       # print(steps_for_intersection)
        intersection_steps_list.append(steps_for_intersection)
    return min(intersection_steps_list)

#print(intersections)
print("closest")
# print(steps_dict_2)
print(find_closest_to_start(intersections, [start_x,start_y]))

print("lowest steps:")
print(steps_by_intersection(intersections))
