def check_adjacent(num):
    string = str(num)
    for index, char in enumerate(string):
        try:
            if string[index] == string[index+1]:
                return True
        except:
            return False

def check_increase(num):
    string = str(num)
    max = len(string)
    count = 1
    for index, char in enumerate(string):
        try:
            if string[index] <= string[index+1]:
                count += 1
        except:
            pass
    if max == count:
        return True
    else:
        return False

#keys ={0,1,2,3,4,5,6,7,8,9}
def check_set(num):
    string = str(num)
    last_char = ''
    matches = {}
    for index, char in enumerate(string):
        if char == last_char:
            # print(char)
            # print(last_char)
            # print("match")
            if char in matches.keys():
                matches[char] += 1
            else:
                matches[char] = 1
        last_char = char
    for key, values in matches.items():
        if matches[key] == 1:
            return True
    return False


counter = 0

for i in range(248345,746315):
    #print(i)
    if check_adjacent(i) and check_increase(i) and check_set(i):
        counter += 1

# print(check_adjacent(11))
# print(check_adjacent(123789))
# print(check_adjacent(111111))
# print(check_adjacent(122345))

# print(check_increase(122345))
# print(check_increase(223450))

print(counter)

print(check_set(123444))
print(check_set(111122))
