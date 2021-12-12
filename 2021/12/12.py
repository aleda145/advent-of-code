import util
from collections import defaultdict

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

# Make graph :)

G = defaultdict(list)

for cave in inp:
    start, end = cave.split("-")
    if end == "start" or start == "end":
        # swap!
        start, end = end, start

    G[start].append(end)
    if start != "start" and end != "end":
        G[end].append(start)


def find_all_paths(graph, start, end, small_cave, path=[]):
    path = path + [start]
    if start not in ["start", "end"] and start.islower():
        small_cave = True
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node.isupper():  # big cave can be visited many times
            newpaths = find_all_paths(graph, node, end, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif not small_cave:
            newpaths = find_all_paths(graph, node, end, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node not in path:
            newpaths = find_all_paths(graph, node, end, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


print(G)
all_paths = find_all_paths(G, "start", "end", False)
print(all_paths)
print(len(all_paths))
# print(bfs(G, "start", "end"))
