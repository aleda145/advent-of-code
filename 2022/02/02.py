import util

inp = util.input_as_lines("input")
sample = util.input_as_lines("sample_input")

scores = {"rock": 1, "paper": 2, "scissors": 3, "win": 6, "draw": 3}

score_sum = 0

for line in inp:
    if line[2] == "X":
        score_sum += scores["rock"]
        if line[0] == "A":
            score_sum += scores["draw"]
        if line[0] == "C":
            score_sum += scores["win"]
    if line[2] == "Y":
        score_sum += scores["paper"]
        if line[0] == "B":
            score_sum += scores["draw"]
        if line[0] == "A":
            score_sum += scores["win"]
    if line[2] == "Z":
        score_sum += scores["scissors"]
        if line[0] == "C":
            score_sum += scores["draw"]
        if line[0] == "B":
            score_sum += scores["win"]

print(score_sum)
score_sum = 0
for line in inp:
    if line[2] == "X":
        # Lose
        if line[0] == "A":
            score_sum += scores["scissors"]
        if line[0] == "B":
            score_sum += scores["rock"]
        if line[0] == "C":
            score_sum += scores["paper"]
    if line[2] == "Y":
        # Draw
        score_sum += scores["draw"]
        if line[0] == "A":
            score_sum += scores["rock"]
        if line[0] == "B":
            score_sum += scores["paper"]
        if line[0] == "C":
            score_sum += scores["scissors"]
    if line[2] == "Z":
        # Win
        score_sum += scores["win"]
        if line[0] == "A":
            score_sum += scores["paper"]
        if line[0] == "B":
            score_sum += scores["scissors"]
        if line[0] == "C":
            score_sum += scores["rock"]

print(score_sum)
