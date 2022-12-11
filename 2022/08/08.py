import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

# only calculate once if a tree is visible or not
# use positions to define trees

tree_height = {}
tree_visibility = {}
tree_score = {}
visibility_directions = ["up"]

max_y = len(inp) - 1
max_x = len(inp[0]) - 1
unknown_trees = []
edge_trees = []
for y, line in enumerate(inp):
    for x, tree in enumerate(line):
        tree_score[(x, y)] = [0, 0, 0, 0]
        if x in [0, max_x]:
            tree_height[(x, y)] = int(tree)
            tree_visibility[(x, y)] = [
                True,
                True,
                True,
                True,
            ]
            edge_trees.append((x, y))
        elif y in [0, max_y]:
            tree_height[(x, y)] = int(tree)
            tree_visibility[(x, y)] = [
                True,
                True,
                True,
                True,
            ]
            edge_trees.append((x, y))
        else:
            tree_height[(x, y)] = int(tree)
            tree_visibility[(x, y)] = [
                None,
                None,
                None,
                None,
            ]
            unknown_trees.append((x, y))

# traverse in each directory until find tree that is higher than it
for tree in unknown_trees:
    cur_tree_height = tree_height[tree]
    visible = False
    # up
    for y in range(1, tree[1] + 1):
        check_tree = (tree[0], tree[1] - y)
        height = tree_height[check_tree]
        if cur_tree_height > height:
            # then we need to check if that tree is visible from that direction
            tree_score[tree][0] += 1
            if tree_visibility[check_tree][0]:
                tree_visibility[tree][0] = True
        else:
            tree_visibility[tree][0] = False
            tree_score[tree][0] += 1
            break
    # down
    for y in range(1, 1 + max_y - tree[1]):
        check_tree = (tree[0], tree[1] + y)
        height = tree_height[check_tree]
        if cur_tree_height > height:
            # then we need to check if that tree is visible from that direction
            tree_score[tree][1] += 1
            if tree_visibility[check_tree][1]:
                tree_visibility[tree][1] = True
        else:
            tree_visibility[tree][1] = False
            tree_score[tree][1] += 1
            break
    # left
    for x in range(1, tree[0] + 1):
        check_tree = (tree[0] - x, tree[1])
        height = tree_height[check_tree]
        if cur_tree_height > height:
            # then we need to check if that tree is visible from that direction
            tree_score[tree][2] += 1
            if tree_visibility[check_tree][2]:
                tree_visibility[tree][2] = True
        else:
            tree_score[tree][2] += 1
            tree_visibility[tree][2] = False
            break
    for x in range(1, 1 + max_x - tree[0]):
        check_tree = (tree[0] + x, tree[1])
        height = tree_height[check_tree]
        if cur_tree_height > height:
            tree_score[tree][3] += 1
            # then we need to check if that tree is visible from that direction
            if tree_visibility[check_tree][3]:
                tree_visibility[tree][3] = True
        else:
            tree_score[tree][3] += 1
            tree_visibility[tree][3] = False
            break
visible_trees = 0
for k, v in tree_visibility.items():
    visible_trees += 1 if True in v else 0
    if k in edge_trees:
        continue
print(f"part1: {visible_trees}")
import math

max_score = 0
for k, v in tree_score.items():
    if math.prod(v) > max_score:
        max_score = math.prod(v)
print(f"part2: {max_score}")
