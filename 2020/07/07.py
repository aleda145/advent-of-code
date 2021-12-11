def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start != "shiny gold":
        start = start[2:]
    if start == end:
        return True
    for node in graph[start]:
        if node not in path:
            newpath = find_all_paths(graph, node, end, path)
            if newpath:
                return newpath


file = open("input", "r")

database = file.read().splitlines()

# database = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """
# database = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# """
# database = database.splitlines()
bag_graph = {}

# shiny gold bag is the root
for row in database:
    bags = row.replace(".", "")
    split_str = bags.split(" bags contain ")
    key = split_str[0]
    if split_str[1] == "no other bags":
        bag_graph[key] = ""
    else:
        value = split_str[1].replace(" bags", "").replace(" bag", "")
        # bag_graph[key] = [val[2:] for val in value.split(", ")]
        bag_graph[key] = value.split(", ")

for dic in bag_graph.items():
    print(dic)

# num_paths = 0
# # part 1
# for key_bag in bag_graph.keys():
#     if find_all_paths(bag_graph, key_bag, "shiny gold") and key_bag != "shiny gold":
#         print(key_bag + " can reach golden")
#         num_paths += 1

# print(num_paths)


# part 2
def bag_count(graph, start):
    count = 1
    num_bags = 1

    for bag in graph[start]:
        if bag != "shiny gold":
            num_bags = int(bag[0])
            next_bag = bag[2:]
            print(bag)
            count += num_bags * bag_count(graph, next_bag)
    return count


print(bag_count(bag_graph, "shiny gold") - 1)
