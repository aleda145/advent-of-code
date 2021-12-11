# opcodes 1, 2, 99
# 99 means finish
# one opcode has 4 numbers total, except 99

# the numbers are indexes in the list

f = open("input","r")
for row in f:
    command_list_from_file=row.split(",")
f.close()
print(command_list_from_file)

command_list_from_file = [int(i) for i in command_list_from_file]
print(command_list_from_file)
#command_list=[1,0,0,0,99]
#command_list = [2,3,0,3,99]
#command_list = [2,4,4,5,99,0]
#command_list = [1,1,1,4,99,5,6,0,99]

# replace position 1 with value 12

# replace position 2 with value 2
command_list=[]
command_list = command_list_from_file.copy()

#command_list=[1002,4,3,4,33]
# print(command_list)
# print(i)
# print(j)
#if parameter == 1, it is a value (immediate mode)

def decode_op(opcode):
    string_op = str(opcode)
    length = len(string_op)
    param_1 = param_2 = param_3 = 0

    if length == 1:
        op = int(string_op)
    elif length == 2: 
        op = int(string_op)
    else:
        op = int(string_op[2:])

    if length == 3:
        param_1 = int(string_op[0])
    if length == 4:
        param_1 = int(string_op[1])
        param_2 = int(string_op[0])
    if length == 5:
        param_1 = int(string_op[2])
        param_2 = int(string_op[1])
        param_3 = int(string_op[0])
    
    return(param_1, param_2, param_3, op)


print(decode_op(1002))
index = 0 
for value in command_list:
    # print(index)
    # print(value)
    modified_index = False

    param_1, param_2, param_3, op = decode_op(command_list[index])
    # print(op)
    
    if op == 1:
        if param_1 == 0:
            first_number = command_list[command_list[index+1]]
        if param_1 == 1:
            first_number = command_list[index+1]
        if param_2 == 0:
            second_number = command_list[command_list[index+2]]
        if param_2 == 1:
            second_number = command_list[index+2]
        if param_3 == 0:
            save_to = command_list[index+3]
            # print(command_list[index+3])
        if param_3 == 1:
            save_to = command_list[index+3]        

        addition = first_number + second_number
        # print(save_to)
        command_list[save_to] = addition
           

    if op == 2:
        # multiply
        if param_1 == 0:
            first_number = command_list[command_list[index+1]]
        if param_1 == 1:
            first_number = command_list[index+1]
        if param_2 == 0:
            second_number = command_list[command_list[index+2]]
        if param_2 == 1:
            second_number = command_list[index+2]
        if param_3 == 0:
            save_to = command_list[index+3]
            #print(command_list[index+3])
        if param_3 == 1:
            save_to = command_list[index+3]        

        mutliplication = first_number * second_number
        # print(save_to)
        command_list[save_to] = mutliplication

    if op == 3:
        # multiply
        val = input("ID?")
        save_to = command_list[index+1]
        command_list[save_to] = int(val)

    if op == 4:
        # multiply
        if param_1 == 0:
            print(command_list[command_list[index+1]])
        if param_1 == 1:
            print(command_list[index+1])
    if op == 5:
        if param_1 == 0:
            first_number = command_list[command_list[index+1]]
        if param_1 == 1:
            first_number = command_list[index+1]
        if param_2 == 0:
            second_number = command_list[command_list[index+2]]
        if param_2 == 1:
            second_number = command_list[index+2]
        
        if first_number !=0:
            index = second_number
            modified_index = True

    if op == 6:

        if param_1 == 0:
            first_number = command_list[command_list[index+1]]
        if param_1 == 1:
            first_number = command_list[index+1]
        if param_2 == 0:
            second_number = command_list[command_list[index+2]]
        if param_2 == 1:
            second_number = command_list[index+2]
        
        if first_number ==0:
            index = second_number
            modified_index = True
    if op == 7:
        if param_1 == 0:
            first_number = command_list[command_list[index+1]]
        if param_1 == 1:
            first_number = command_list[index+1]
        if param_2 == 0:
            second_number = command_list[command_list[index+2]]
        if param_2 == 1:
            second_number = command_list[index+2]
        if param_3 == 0:
            save_to = command_list[index+3]
            #print(command_list[index+3])
        if param_3 == 1:
            save_to = command_list[index+3]   
        if first_number < second_number:
            command_list[save_to] = 1
        else: 
            command_list[save_to] = 0
            
        
    if op == 8:
        if param_1 == 0:
            first_number = command_list[command_list[index+1]]
        if param_1 == 1:
            first_number = command_list[index+1]
        if param_2 == 0:
            second_number = command_list[command_list[index+2]]
        if param_2 == 1:
            second_number = command_list[index+2]
        if param_3 == 0:
            save_to = command_list[index+3]
            #print(command_list[index+3])
        if param_3 == 1:
            save_to = command_list[index+3]   
        if first_number == second_number:
            command_list[save_to] = 1
        else: 
            command_list[save_to] = 0
             


    if op == 1 or op == 2 or op == 7 or op == 8:
        index +=4
    if op == 3 or op == 4:
        index +=2
    if (op == 5 or op == 6) and modified_index == False:
        index +=3
    

    # print(index)
    # print(command_list)

    # if value == 99:
    #     print("stop!")
    #     break

# if command_list[0] == 19690720:
#     print("found")
#     print("break")
#     #print(command_list)
#     print(command_list[1]*100+command_list[2])
#     break
