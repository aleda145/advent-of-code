from collections import defaultdict

numbers = [0, 3, 6]
numbers = [11, 18, 0, 20, 1, 7, 16]
# numbers = [3, 2, 1]
spoken_numbers = []
spoken_num_occ = defaultdict(int)
spoken_num_turns = defaultdict(list)
turn = 1
last_num = 0
while True:
    if turn <= len(numbers):
        num = numbers[turn - 1]
        spoken_num_turns[num].append(turn)
    else:
        # done all start nums
        if spoken_num_occ[last_num] == 1:
            num = 0
        else:
            seen_turns = spoken_num_turns[last_num]
            last_spoken_turn = seen_turns[-1]
            last_last_spoken_turn = seen_turns[-2]
            num = last_spoken_turn - last_last_spoken_turn
    spoken_num_turns[num].append(turn)
    spoken_num_occ[num] += 1
    if turn % 100000 == 0:
        print(f"turn: {turn}: {num}")
    last_num = num
    if turn >= 30000000:
        break
    turn += 1