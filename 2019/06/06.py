def find_parent(node, orbit_path):
    if node == 'COM':
        return orbit_path
    for planet in graph.keys():
        if node in graph[planet]:

            orbit_path.append(planet)
            find_parent(planet, orbit_path)
    return orbit_path


f = open("input","r")
orbit_list = []
for row in f:
    orbit_list.append(row.rstrip('\n'))
f.close()
#print(orbit_list)

graph = {}

for orbit in orbit_list:
    orbit_left = orbit[:3]
    orbit_right = orbit[4:]
    if orbit_left in graph.keys():
        graph[orbit_left].append(orbit_right)
    else:
        graph[orbit_left] = []
        graph[orbit_left].append(orbit_right)


orbits = 0 

for orbit in orbit_list:
    orbit_right = orbit[4:]
    orbit_path = find_parent(orbit_right,[])
    orbits += len(orbit_path)
print(orbits)


YOU_path = find_parent('YOU',[])
SAN_path = find_parent('SAN',[])

path_to_SAN = SAN_path.copy()
path_to_YOU = YOU_path.copy()


for orbit in YOU_path:
    if orbit in SAN_path:
        path_to_SAN.remove(orbit)

for orbit in SAN_path:
    if orbit in YOU_path:
        path_to_YOU.remove(orbit)


print(len(path_to_SAN)+len(path_to_YOU))