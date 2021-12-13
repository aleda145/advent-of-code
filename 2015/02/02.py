import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")
paper = 0
ribbon = 0
for present in inp:
    print(present.split("x"))
    l, w, h = [int(x) for x in present.split("x")]
    paper += 2 * l * w + 2 * w * h + 2 * h * l
    # then find slack
    paper += min([l * w, w * h, l * h])
    # ribbon
    ribbon += sum([x * 2 for x in (sorted([l, w, h])[0:2])])
    # feet of ribbon
    ribbon += l * w * h
print(paper)
print(ribbon)
