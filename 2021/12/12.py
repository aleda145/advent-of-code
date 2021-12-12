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


def find_all_paths(graph, start, end, two_small, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node.isupper():  # big cave can be visited many times
            newpaths = find_all_paths(graph, node, end, two_small, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node not in path:
            newpaths = find_all_paths(graph, node, end, two_small, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif path.count(node) < 2 and two_small == False:
            newpaths = find_all_paths(graph, node, end, True, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# print(G)
all_paths = find_all_paths(G, "start", "end", False)
import pprint

# pprint.pprint(all_paths)
print(len(all_paths))
# print(bfs(G, "start", "end"))
