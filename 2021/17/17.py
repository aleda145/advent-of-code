import util

inp = util.input_as_string("input")
sample = util.input_as_string("sample_input")

x_inp, y_inp = inp.split("target area: ")[1].split(", ")

x_start, x_end = [int(x) for x in x_inp.split("=")[1].split("..")]
y_start, y_end = [int(y) for y in y_inp.split("=")[1].split("..")]

target_x = range(x_start, x_end + 1)
target_y = range(y_start, y_end + 1)

cur_pos_x = 0

possible_y = []
max_height = []
for y_init in range(-1000, 1000):
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
print(possible_y)
possible_x = []
possible_steps = []
for x_init in range(0, 500):
    step = 1
    x_v = x_init
    cur_pos_x = 0
    while True:
        # print(cur_pos_x)
        cur_pos_x += x_v
        if cur_pos_x in target_x:
            possible_x.append(x_init)
            possible_steps.append(step)
        x_v = x_v - 1
        step += 1
        if x_v - 1 < 0:
            break
        if step > 1000:
            break

# max_step = max(possible_steps)

print(possible_x)

print(f"max height was {max(max_height)}")
uniq_x = set(possible_x)
uniq_y = set(possible_y)

# Let's just try all combinations?

reached_target = 0
for x_v_init in uniq_x:
    for y_v_init in uniq_y:
        print(f"checking {x_v_init}, {y_v_init}")
        step = 1
        cur_pos_x = 0
        cur_pos_y = 0
        height_path = []
        x_v = x_v_init
        y_v = y_v_init
        while True:
            cur_pos_x += x_v
            cur_pos_y += y_v
            height_path.append(cur_pos_y)
            x_v = x_v - 1 if x_v > 0 else 0
            y_v -= 1
            print(f"step: {step}, pos: {cur_pos_x},{cur_pos_y}")
            if cur_pos_x in target_x and cur_pos_y in target_y:
                print("Reached target!")
                reached_target += 1
                break
            if cur_pos_x > target_x[-1] and cur_pos_y < target_y[-1]:
                print("overshot target!")
                break
            if step > 10000:
                print("step limit exceeded")
                break
            step += 1
print(max(max_height))
print(reached_target)
