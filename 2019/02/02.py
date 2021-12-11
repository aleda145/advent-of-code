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
for i in range(0,100):
    for j in range(0,100):
        command_list = command_list_from_file.copy()

        command_list[1] = i
        command_list[2] = j
        # print(command_list)
        # print(i)
        # print(j)
        for index, value in enumerate(command_list):
            # print(index)
            # print(value)
            try:
                if index % 4 == 0:
                    # print("this is opcode:")
                    #print(value)
                    if value == 1:
                        # print("make addition")
                        # print("values to add together: "+ str(command_list[command_list[index+1]]) +" and " + str(command_list[command_list[index+2]]))
                        # print("save to position:" + str(command_list[index+3]))
                        command_list[command_list[index+3]] = command_list[command_list[index+1]] + command_list[command_list[index+2]]
                    if value == 2:
                        # print("values to multiply together: "+ str(command_list[command_list[index+1]]) +" and " + str(command_list[command_list[index+2]]))
                        # print("save to position:" + str(command_list[index+3]))
                        command_list[command_list[index+3]] = command_list[command_list[index+1]] * command_list[command_list[index+2]]
                    if value == 99:
                       # print("stop!")
                        break
                # if value == 99:
                #     print("stop!")
                #     break
            except: 
                print("try next")
        if command_list[0] == 19690720:
            print("found")
            print("break")
            #print(command_list)
            print(command_list[1]*100+command_list[2])
            break
