f = open("input","r")

layers = []

for row in f:
    data = row
f.close()

print(data)
#data = '0222112222120000'
print(len(data))
last = 0
for i in range(25*6,len(data)+25*6,25*6):
    print(i)
    layers.append(data[last:i])
    last = i

print(layers)

def count_number(input_list, number):
    count = 0 
    for value in input_list:
        if value == number:
            count +=1

    return count

# min_zeroes = 900000
# check_layer = []
# for layer in layers: 
#     if min_zeroes > count_number(layer, '0'):
#         check_layer = layer
#         min_zeroes = count_number(layer, '0')


# print(check_layer)

# ones = count_number(check_layer, '1')
# twos = count_number(check_layer, '2')

# print(ones)
# print(twos)
# print(ones*twos)

message = [3] *150
written_indexes = [0] *150

print(written_indexes)
for layer in layers:
    for index, number in enumerate(layer):
        # print(number)
        if written_indexes[index] == 0:
            if number == '0':
                message[index] = '□'
            if number == '1':
                message[index] = '■'
            if number != '2':
                written_indexes[index] = 1
print(message)

for index, number in enumerate(message):
    print(number, end ='')
    if (index+1) % 25 == 0:
        print("")

