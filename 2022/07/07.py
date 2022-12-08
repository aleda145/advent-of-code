import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")


class Tree:
    def __init__(self, name):
        self.children = []
        self.parent = None
        self.file_names = []
        self.file_sizes = []
        self.name = name
        self.tot_file_size = 0

    def add_data(self, val):
        self.tot_file_size += val
        if self.parent is not None:
            self.parent.add_data(val)


old_dir = None
added_dirs = []
for line in inp:
    if line[0:4] == "$ cd":
        change_dir = line[5:]

        if change_dir == "..":
            cur_dir = cur_dir.parent
        else:
            cur_dir = Tree(change_dir)
            added_dirs.append(cur_dir)
            if old_dir != None:
                cur_dir.parent = old_dir
                old_dir.children.append(cur_dir)
            else:
                root = cur_dir
        old_dir = cur_dir
    elif line == "$ ls":
        pass
    else:
        filesize_or_dir, name = line.split()
        if filesize_or_dir != "dir":
            cur_dir.file_names.append(name)
            cur_dir.file_sizes.append(int(filesize_or_dir))
            cur_dir.add_data(int(filesize_or_dir))


def printTree(self, depth):
    print(f"{depth*' '}- {self.name}")
    for file_name, file_size in zip(self.file_names, self.file_sizes):
        print(f"{(depth+1)*' '}- {file_name} size={file_size}")
    for child in self.children:
        printTree(child, depth + 1)


def calcSize(self, cur_ok_dir_size):
    tot_file_size = 0
    cur_child_size = 0
    for child in self.children:
        child_size, cur_ok_dir_size = calcSize(child, cur_ok_dir_size)
        cur_child_size += child_size
    for file_size in self.file_sizes:
        tot_file_size += file_size
    tot_file_size += cur_child_size
    # print(f"{self.name}, size: {tot_file_size}")
    if tot_file_size <= 100000:
        cur_ok_dir_size += tot_file_size

    return tot_file_size, cur_ok_dir_size


print(f"part1: {calcSize(root, 0)[1]}")

dir_sizes = []
for dir in added_dirs:
    dir_sizes.append(dir.tot_file_size)

dir_sizes.sort()
unused_size = 70_000_000 - root.tot_file_size
dir_to_del_size = 30_000_000 - unused_size
for dir_size in dir_sizes:
    if dir_size >= dir_to_del_size:
        print(f"part2: {dir_size}")
        break
