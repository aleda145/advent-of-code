import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

start_polymer = inp[0]
print(start_polymer)

polymer_rules = {}

for line in inp[2:]:
    rule, insertion = line.split(" -> ")
    polymer_rules[rule] = insertion

polymer = start_polymer

for step in range(1, 11):
    new_polymer = ""
    for i in range(0, len(polymer)):
        if i == 0:
            new_polymer += polymer[i]
            continue
        pair = f"{polymer[i-1]}{polymer[i]}"
        if pair in polymer_rules:
            new_polymer += f"{polymer_rules[pair]}{polymer[i]}"
    print(f"step: {step}")
    print(new_polymer)
    polymer = new_polymer
print(polymer)

from collections import Counter

char_count = Counter()
for char in set(polymer):
    char_count[char] = polymer.count(char)

print(char_count)
print(char_count.most_common()[0][1] - char_count.most_common()[-1][1])
