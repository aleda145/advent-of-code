import util

inp = util.input_as_lines("input")

# energy increase by one on all octopus
# if octopus == 9, all adjacent octopuses increase by 1
# if octopus > 9, it flashes
# the next step after flash, set energy to 0

# make octograph!

G = {}
octopus_energy = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        G[(y, x)] = []
        if y - 1 >= 0:
            # up
            G[(y, x)].append([(y - 1, x)])
            octopus_energy[(y - 1, x)] = int(inp[y - 1][x])
            if x + 1 < len(inp[y]):
                # up right
                G[(y, x)].append([(y - 1, x + 1)])
                octopus_energy[(y - 1, x + 1)] = int(inp[y - 1][x + 1])
            if x - 1 >= 0:
                # down left
                G[(y, x)].append([(y - 1, x - 1)])
                octopus_energy[(y - 1, x - 1)] = int(inp[y - 1][x - 1])

        if y + 1 < len(inp):
            # down
            G[(y, x)].append([(y + 1, x)])
            octopus_energy[(y + 1, x)] = int(inp[y + 1][x])

            if x - 1 >= 0:
                G[(y, x)].append([(y + 1, x - 1)])
                octopus_energy[(y + 1, x - 1)] = int(inp[y + 1][x - 1])

                # down left
            if x + 1 < len(inp[y]):
                # down right
                G[(y, x)].append([(y + 1, x + 1)])
                octopus_energy[(y + 1, x + 1)] = int(inp[y + 1][x + 1])

        if x + 1 < len(inp[y]):
            # right
            G[(y, x)].append([(y, x + 1)])
            octopus_energy[(y, x + 1)] = int(inp[y][x + 1])

        if x - 1 >= 0:
            # left
            G[(y, x)].append([(y, x - 1)])
            octopus_energy[(y, x - 1)] = int(inp[y][x - 1])

print(G[(2, 2)])
print(len(G[(2, 2)]))
import pprint

pprint.pprint(octopus_energy)
tot_flashes = 0
for step in range(0, 100):
    # increase all energy by one
    print(step)
    flashing_keys = []
    for key in G.keys():
        octopus_energy[key] += 1
        if octopus_energy[key] > 9:
            flashing_keys.append(key)
    # Increase energy on adjacent
    for flashing_key in flashing_keys:
        for adj_octopuses in G[flashing_key]:
            for adj_octopus in adj_octopuses:
                octopus_energy[adj_octopus] += 1
                if octopus_energy[adj_octopus] > 9 and adj_octopus not in flashing_keys:
                    flashing_keys.append(adj_octopus)
    # Reset to 0
    for flashing_key in flashing_keys:
        octopus_energy[flashing_key] = 0
    tot_flashes += len(flashing_keys)

pprint.pprint(octopus_energy)
print(tot_flashes)
