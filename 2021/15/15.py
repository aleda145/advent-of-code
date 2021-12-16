import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

import networkx as nx

G = nx.DiGraph()

cur_inp = inp
# make a graph, then dijikstra?
# make the new input, its eaiser than adjusting the graph structure

weights = {}
new_inp = []
size = len(cur_inp)
for y in range(size * 5):
    new_row = []
    for x in range(size * 5):
        new_val = int(cur_inp[y % size][x % size]) + (x // size) + (y // size)
        new_val = new_val % 9
        if new_val == 0:
            new_val = 9
        new_row.append(new_val)
    new_inp.append(new_row)

for y in range(len(new_inp)):
    for x in range(len(new_inp)):
        weights[(y, x)] = int(new_inp[y][x])
        if y - 1 >= 0:
            G.add_edge((y, x), (y - 1, x), weight=int(new_inp[y - 1][x]))
        if y + 1 < len(new_inp):
            G.add_edge((y, x), (y + 1, x), weight=int(new_inp[y + 1][x]))
        if x + 1 < len(new_inp[y]):
            G.add_edge((y, x), (y, x + 1), weight=int(new_inp[y][x + 1]))
        if x - 1 >= 0:
            G.add_edge((y, x), (y, x - 1), weight=int(new_inp[y][x - 1]))

shortest_path = nx.shortest_path(
    G,
    source=(0, 0),
    target=((len(cur_inp) * 5) - 1, (len(cur_inp) * 5) - 1),
    weight="weight",
)
print(shortest_path)

# for path in shortest_path:
print(nx.path_weight(G, shortest_path, weight="weight"))
