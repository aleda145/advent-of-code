import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")
points = 0

for line in inp:
    card, score = line.split(":")
    card_number = card.split(" ")[1]
    winning_numbers, player_numbers = score.split("|")
    winning_numbers_list = winning_numbers.strip().split(" ")
    player_numbers_list = player_numbers.strip().split(" ")
    matches = 0
    for player_number in player_numbers_list:
        if not player_number.isnumeric():
            continue
        if player_number in winning_numbers_list:
            matches += 1
    if matches:
        points += 2 ** (matches - 1)
print(points)

num_cards = 0


def scorecards(card_input, start_line, stop_line):
    cur_line = start_line
    for line in card_input[start_line:stop_line]:
        global num_cards
        num_cards += 1
        card, score = line.split(":")
        card_number = card.split(" ")[1]
        winning_numbers, player_numbers = score.split("|")
        winning_numbers_list = winning_numbers.strip().split(" ")
        player_numbers_list = player_numbers.strip().split(" ")
        matches = 0

        for player_number in player_numbers_list:
            if not player_number.isnumeric():
                continue
            if player_number in winning_numbers_list:
                matches += 1
        # spawn another for each match, but with changing starting lines
        for match in range(matches):
            scorecards(card_input, cur_line + match + 1, cur_line + match + 2)
        cur_line += 1


scorecards(inp, 0, len(inp))
print(num_cards)
