import math

def compute_gcd(x, y):

    while(y):
        x, y = y, x % y
    return abs(x)

def locate_asteroids(grid):
    asteroid_grid =[]
    for y_idx, x_grid in enumerate(grid):
        #print(x_grid)
        for x_idx, char in enumerate(x_grid):
            if char == '#':
               # print('ass')
                asteroid_grid.append([x_idx,y_idx])

    return asteroid_grid

def can_reach(asteroid1, asteroid2,asteroids):
    start_vector_x = asteroid1[0]
    start_vector_y = asteroid1[1]
    end_vector_x = asteroid2[0]
    end_vector_y = asteroid2[1]
    direct_vector_x = (end_vector_x-start_vector_x)
    direct_vector_y = (end_vector_y-start_vector_y)
    gcd = compute_gcd(direct_vector_x,direct_vector_y)
    sub_vector_x = int(direct_vector_x/gcd)
    sub_vector_y = int(direct_vector_y/gcd)
    if asteroid1[0] != asteroid2[0]:
        start = int(direct_vector_x/gcd)
        end = direct_vector_x
    else: 
        start = int(direct_vector_y/gcd)
        end = direct_vector_y
    
    new_vector_x = start_vector_x + sub_vector_x
    new_vector_y = start_vector_y + sub_vector_y    
    while True:
        if ((new_vector_x == end_vector_x) and (new_vector_y == end_vector_y)):
            return True
        check_pos = [new_vector_x, new_vector_y]
        if check_pos in asteroids:
            return False 
        else:
            new_vector_x += sub_vector_x
            new_vector_y += sub_vector_y

    return True

def calc_angle(station, asteroid):
    start_vector_x = station[0]
    start_vector_y = station[1]
    end_vector_x = asteroid[0]
    end_vector_y = asteroid[1]
    dy = end_vector_y-start_vector_y
    dx = end_vector_x-start_vector_x
    return (math.atan2(dy,dx))

def giant_laser():
    pass

f = open("input","r")

grid = []

for row in f:
    grid.append((row.rstrip('\n')))
f.close()


#print(grid)

asteroids =[]
asteroids = locate_asteroids(grid)
# total_asteroids = len(asteroids)
# asteroid_reach_dict ={}
# asteroid_can_not_reach_dict={}
# asteroid_count_reach_dict ={}

# for asteroid1 in asteroids:
#     # print("check:")
#     # print(asteroid1)
#     asteroid_reach_dict[tuple(asteroid1)]=[]
#     asteroid_can_not_reach_dict[tuple(asteroid1)]=[]
#     asteroid_count_reach_dict[tuple(asteroid1)]=0
#     for asteroid2 in asteroids:
#         if asteroid1!=asteroid2:
#            # print("can reach? " + str(asteroid2))
#             if can_reach(asteroid1, asteroid2, asteroids) == True:
#                 asteroid_reach_dict[tuple(asteroid1)].append(asteroid2)
#                 asteroid_count_reach_dict[tuple(asteroid1)]+=1
#             else:
#                 #print("no reach")
#                 asteroid_can_not_reach_dict[tuple(asteroid1)].append(asteroid2)

#print("reach")
#print(asteroid_reach_dict)
# print("no reach")
# print(asteroid_can_not_reach_dict)
#print("count")
#print(asteroid_count_reach_dict)
#best_asteroid = (max(asteroid_reach_dict, key = asteroid_count_reach_dict.get))
# print(best_asteroid)
# print(asteroid_count_reach_dict[best_asteroid])

killed_asteroids = []

test_station = [13,17]

station_reach_dict ={}
station_can_not_reach_dict={}
station_count_reach_dict ={}

angle_station_to_asteroid = {}
station_reach_dict[tuple(test_station)]=[]
station_can_not_reach_dict[tuple(test_station)]=[]
station_count_reach_dict[tuple(test_station)]=0


while len(asteroids)>0:
    for asteroid2 in asteroids:
        if test_station != asteroid2:
            # print("can reach? " + str(asteroid2))
            if can_reach(test_station, asteroid2, asteroids) == True:
                angle = calc_angle(test_station,asteroid2)
                if angle >= - math.pi/2:
                    angle = math.pi/2- angle
                else: 
                    angle = math.pi/2 - angle -2*math.pi
                station_reach_dict[tuple(test_station)].append(asteroid2)
                angle_station_to_asteroid[tuple(asteroid2)] = angle
                station_count_reach_dict[tuple(test_station)]+=1
                
            else:
                #print("no reach")
                station_can_not_reach_dict[tuple(test_station)].append(asteroid2)
    #sorted_dict = {k: v for k, v in sorted(angle_station_to_asteroid.items(), key=lambda item: item[1])}
    #print(sorted_dict)
    while station_reach_dict[tuple(test_station)] != '':
        #if angle_station_to_asteroid
        asteroid_to_kill = (max(angle_station_to_asteroid, key = angle_station_to_asteroid.get))
        # print(asteroid_to_kill)
        # print(station_reach_dict)
        del angle_station_to_asteroid[asteroid_to_kill]
        station_reach_dict[tuple(test_station)].remove(list(asteroid_to_kill))
        asteroids.remove(list(asteroid_to_kill))
        killed_asteroids.append(asteroid_to_kill)
    # print(station_reach_dict)
    # print(killed_asteroids)

print(killed_asteroids[199])
#coords for station is 13, 17

#print(station_reach_dict)
#print(station_can_not_reach_dict)

#print(angle_station_to_asteroid)


# print(calc_angle([8,3],[8,1])) # above, start
# print(calc_angle([8,3],[9,2])) # above, right
# print(calc_angle([8,3],[10,2])) # above, right+1

# print(calc_angle([8,3],[9,3])) #right
# print(calc_angle([8,3],[9,4])) #right below
# print(calc_angle([8,3],[9,5])) #right below+1

# print(calc_angle([8,3],[8,5])) # below
# print(calc_angle([8,3],[7,5])) # below left
# print(calc_angle([8,3],[6,5])) # below left+1

# print(calc_angle([8,3],[7,3])) #left
# print(calc_angle([8,3],[7,2])) #left above
# print(calc_angle([8,3],[7,1])) #left above+1

# print("new")
# print(math.pi/2-calc_angle([8,3],[8,1])) # above, start
# print(math.pi/2-calc_angle([8,3],[9,2])) # above, right
# print(math.pi/2-calc_angle([8,3],[10,2])) # above, right+1

# print(math.pi/2-calc_angle([8,3],[9,3])) #right
# print(math.pi/2-calc_angle([8,3],[9,4])) #right below
# print(math.pi/2-calc_angle([8,3],[9,5])) #right below+1

# print(math.pi/2-calc_angle([8,3],[8,5])) # below
# print(math.pi/2-calc_angle([8,3],[7,5])) # below left
# print(math.pi/2-calc_angle([8,3],[6,5])) # below left+1

# print(math.pi/2-calc_angle([8,3],[7,3])) #left
# print(math.pi/2-calc_angle([8,3],[7,2])-2*math.pi) #left above
# print(math.pi/2-calc_angle([8,3],[7,1])-2*math.pi) #left above+1


# print(calc_angle([0,0],[0,1]))
# print(calc_angle([0,0],[1,0]))
# print(calc_angle([0,0],[1,1]))

# print(calc_angle([0,0],[0,-1]))
# print(calc_angle([0,0],[1,0]))
# print(calc_angle([0,0],[1,-1]))

# print(calc_angle([0,0],[0,1]))
# print(calc_angle([0,0],[-1,0]))
# print(calc_angle([0,0],[-1,-1]))

# print(calc_angle([0,0],[0,1]))
# print(calc_angle([0,0],[-1,0]))
# print(calc_angle([0,0],[-1,1]))

