import util

inp = util.input_as_ints("input")
# print(inp)

last = 0
increases = 0
for num in inp:
    if last != 0:
        if num > last:
            increases += 1
    last = num
# part 1
print(increases)


sliding_window = []
window_sum = 0
window_increases = 0
for num in inp:
    if len(sliding_window) < 3:
        sliding_window.append(num)
        continue
    if window_sum == 0:
        # special case
        window_sum = sum(sliding_window)
        continue

    # swap the positions
    sliding_window[0] = sliding_window[1]
    sliding_window[1] = sliding_window[2]
    sliding_window[2] = num
    if sum(sliding_window) > window_sum:
        window_increases += 1
    window_sum = sum(sliding_window)

print(window_increases)
