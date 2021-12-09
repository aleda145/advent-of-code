import util

inp = util.input_as_lines("input")

risk_level = 0

low_points = []
for y in range(len(inp)):
    for x in range(len(inp[y])):
        cur_height = inp[y][x]
        print(f"{x},{y} has height {cur_height}")
        # check all directions
        lower_than_north = False
        lower_than_south = False
        lower_than_east = False
        lower_than_west = False
        try:
            # North
            if cur_height < inp[y - 1][x]:
                lower_than_north = True
        except:
            # No index there, so it is automatically lower
            lower_than_north = True
        try:
            # south
            if cur_height < inp[y + 1][x]:
                lower_than_south = True
        except:
            # No index there, so it is automatically lower
            lower_than_south = True
        try:
            # east
            if cur_height < inp[y][x + 1]:
                lower_than_east = True
        except:
            # No index there, so it is automatically lower
            lower_than_east = True
        try:
            # west
            if cur_height < inp[y][x - 1]:
                lower_than_west = True
        except:
            # No index there, so it is automatically lower
            lower_than_west = True
        if (
            lower_than_north
            and lower_than_south
            and lower_than_east
            and lower_than_west
        ):
            low_points.append((y, x))
            risk_level += int(cur_height) + 1
print(risk_level)

G = {}
# Let's do a graph instead
for y in range(len(inp)):
    for x in range(len(inp[y])):
        G[(y, x)] = []
        try:
            if y - 1 >= 0:
                G[(y, x)].append([(y - 1, x), int(inp[y - 1][x])])
        except:
            print("list out of range")
        try:
            if y + 1 < len(inp):
                G[(y, x)].append([(y + 1, x), int(inp[y + 1][x])])
        except:
            print("list out of range")
        try:
            if x + 1 < len(inp[y]):
                G[(y, x)].append([(y, x + 1), int(inp[y][x + 1])])
        except:
            print("list out of range")
        try:
            if x - 1 >= 0:
                G[(y, x)].append([(y, x - 1), int(inp[y][x - 1])])
        except:
            print("list out of range")
print(G)
print(G.keys())
print(G[(4, 9)])


def find_basins(graph, start_node):
    visited_nodes = []
    next_nodes = [start_node]
    while next_nodes:
        next_node = next_nodes.pop()
        for node in graph[tuple(next_node)]:
            if node not in visited_nodes:
                if node[1] == 9:
                    print(f"{node[0]} is a peak!")
                else:
                    print(f"{node[0]} is not a peak!")
                    visited_nodes.append(node)

                    next_nodes.append(node[0])

    print(visited_nodes)
    print(len(visited_nodes))
    return len(visited_nodes)


basin_size = []

for points in low_points:
    #  From the graph, find all basins!
    print(points)
    print(G[points], points)
    basin_size.append(find_basins(G, points))

basin_size.sort()
import math

print(basin_size[-3::])
print(math.prod(basin_size[-3::]))
