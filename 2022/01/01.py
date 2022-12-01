import util
inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

elf_list = [0]
elf_idx = 0
for line in inp:
    if not line:
        elf_idx+=1
        elf_list.append(0)
    else:
        elf_list[elf_idx]+=int(line)
print(f"part1: {max(elf_list)}")
elf_list.sort()
print(f"part2: {sum(elf_list[-3:])}")
