from functools import reduce

def check_if_valid(policy, password):
    lower_index = int(policy.split(" ")[0].split("-")[0])-1
    upper_index = int(policy.split(" ")[0].split("-")[1])-1
    letter = policy.split(" ")[1]
    num_letter = password.count(letter)
    if password[lower_index] != letter and password[upper_index] != letter:
        return False
    elif password[lower_index] == letter and password[upper_index] == letter:
        return False
    else:
        return True

file = open("input","r")

database = file.read().splitlines()
pass_dict = {}
valid = 0
for entry in database:
    policy = entry.split(": ")[0]
    password = entry.split(": ")[1]
    if check_if_valid(policy, password):
        print(policy)
        print(password)
        print("valid!")
        valid+=1
print(valid)