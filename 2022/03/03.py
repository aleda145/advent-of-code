import util
from collections import Counter
import string

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

scores = {}
for idx, ch in enumerate(string.ascii_letters):
    scores[ch] = idx + 1

scores_sum = 0
for line in inp:
    half_way = len(line) // 2
    first_comp = line[0:half_way]
    second_comp = line[half_way:]
    first_counter = Counter(first_comp)
    second_counter = Counter(second_comp)
    intersection = first_counter & second_counter
    scores_sum += scores[list(intersection.keys())[0]]

print(f"part1: {scores_sum}")

elf_group = 1
group = []
p2_scores = 0
for line in inp:
    group.append(Counter(line))
    if elf_group % 3 == 0:
        p2_scores += scores[list((group[0] & group[1] & group[2]).keys())[0]]

        group = []
    elf_group += 1
print(f"part2: {p2_scores}")
