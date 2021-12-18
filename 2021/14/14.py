import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

start_polymer = inp[0]
last_char = start_polymer[-1]
print(start_polymer)

polymer_rules = {}

for line in inp[2:]:
    rule, insertion = line.split(" -> ")
    polymer_rules[rule] = [rule[0] + insertion, insertion + rule[1]]

print(polymer_rules)
from collections import Counter

polymer = start_polymer

pairs = Counter()
for i in range(0, len(polymer)):
    if i == 0:
        continue
    pair = f"{polymer[i-1]}{polymer[i]}"
    pairs[pair] += 1

print(pairs)
for step in range(1, 41):
    new_pairs = Counter()
    char_counter = Counter()
    for key in pairs.keys():
        rule_output = polymer_rules[key]
        num_of_rules = pairs[key]
        for rule in rule_output:
            print(f"key {key} gave rule {rule}")
            new_pairs[rule] += num_of_rules
            char_counter[rule[0]] += num_of_rules
    pairs = new_pairs.copy()
    print(f"step: {step}")
    print(pairs)
    print(char_counter)

# +1 since there is always the last_char in the series we dont count
char_counter[last_char] += 1
print(char_counter.most_common()[0][1] - char_counter.most_common()[-1][1])
