import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")
points = 0

for line in inp:
    print(line)
    card, score = line.split(":")
    card_number = card.split(" ")[1]
    winning_numbers, player_numbers = score.split("|")
    winning_numbers_list = winning_numbers.strip().split(" ")
    player_numbers_list = player_numbers.strip().split(" ")
    print(card_number, winning_numbers_list, player_numbers_list)
    matches = 0
    for player_number in player_numbers_list:
        if not player_number.isnumeric():
            continue
        if player_number in winning_numbers_list:
            matches += 1
    print(matches)
    if matches:
        points += 2 ** (matches - 1)
print(points)
