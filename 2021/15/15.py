import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

import networkx as nx

G = nx.DiGraph()

cur_inp = inp
# make a graph, then dijikstra?
weights = {}
for y in range(len(cur_inp)):
    for x in range(len(cur_inp)):
        weights[(y, x)] = int(cur_inp[y][x])
        if y - 1 >= 0:
            G.add_edge((y, x), (y - 1, x), weight=int(cur_inp[y - 1][x]))
        if y + 1 < len(cur_inp):
            G.add_edge((y, x), (y + 1, x), weight=int(cur_inp[y + 1][x]))
        if x + 1 < len(cur_inp[y]):
            G.add_edge((y, x), (y, x + 1), weight=int(cur_inp[y][x + 1]))
        if x - 1 >= 0:
            G.add_edge((y, x), (y, x - 1), weight=int(cur_inp[y][x - 1]))

import pprint

pprint.pprint(nx.to_dict_of_dicts(G))
shortest_path = nx.shortest_path(
    G, source=(0, 0), target=(len(cur_inp) - 1, len(cur_inp) - 1), weight="weight"
)
print(shortest_path)

# for path in shortest_path:
print(nx.path_weight(G, shortest_path, weight="weight"))
