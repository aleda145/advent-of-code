import util

inp = util.input_as_string("input")
sample = util.input_as_string("sample_input")

x_inp, y_inp = inp.split("target area: ")[1].split(", ")

x_start, x_end = [int(x) for x in x_inp.split("=")[1].split("..")]
y_start, y_end = [int(y) for y in y_inp.split("=")[1].split("..")]

target_x = range(x_start, x_end + 1)
target_y = range(y_start, y_end + 1)
print(target_x)
print(target_y)

cur_pos_x = 0

possible_y = []
max_height = []
for y_init in range(0, 10000):
    step = 1
    y_v = y_init
    cur_pos_y = 0
    height_path = []
    while True:
        # print(cur_pos_x)
        cur_pos_y += y_v
        height_path.append(cur_pos_y)
        if cur_pos_y in target_y:
            possible_y.append(y_init)
            max_height.append(max(height_path))
        y_v = y_v - 1
        step += 1
        if step > 1000:
            break
print(max(max_height))
