file = open("input", "r")

database = file.read().splitlines()

database.append("")
database.insert(0, "")
answers_list = []
answers = ""
num_persons = 0
persons_list = []
for row in database:
    answers += row
    num_persons += 1
    if row == "":
        answers_list.append(answers)
        persons_list.append(num_persons)
        answers = ""
        num_persons = -1

print(answers_list)

# get unique chars in each string
# just make it a list of sets!
answers_set = []
for answers in answers_list:
    answers_set.append(set(answers))

count = 0

for unique_chars, answers, num_persons in zip(answers_set, answers_list, persons_list):
    print(unique_chars)
    print(answers)
    print(num_persons)
    for char in unique_chars:
        if answers.count(char) == num_persons:
            count += 1
