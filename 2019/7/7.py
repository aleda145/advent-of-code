# opcodes 1, 2, 99
# 99 means finish
# one opcode has 4 numbers total, except 99
# the numbers are indexes in the list
import itertools 

class Amplifier():
    
    def __init__(self, command_list):
        self.command_list = command_list.copy()
        self.phase = ''
        self.index = 0

    def runintcode(self, phase, in_value):
    
        # print(self.index)
        # print(value)
        while self.index <= len(self.command_list):
            modified_index = False

            param_1, param_2, param_3, op = decode_op(self.command_list[self.index])
            #print(op)

            if op == 99:
                return False,-1
            
            if op == 1:
                if param_1 == 0:
                    first_number = self.command_list[self.command_list[self.index+1]]
                if param_1 == 1:
                    first_number = self.command_list[self.index+1]
                if param_2 == 0:
                    second_number = self.command_list[self.command_list[self.index+2]]
                if param_2 == 1:
                    second_number = self.command_list[self.index+2]
                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    # print(self.command_list[self.index+3])
                if param_3 == 1:
                    save_to = self.command_list[self.index+3]        

                addition = first_number + second_number
                # print(save_to)
                self.command_list[save_to] = addition
                

            if op == 2:
                # multiply
                if param_1 == 0:
                    first_number = self.command_list[self.command_list[self.index+1]]
                if param_1 == 1:
                    first_number = self.command_list[self.index+1]
                if param_2 == 0:
                    second_number = self.command_list[self.command_list[self.index+2]]
                if param_2 == 1:
                    second_number = self.command_list[self.index+2]
                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    #print(self.command_list[self.index+3])
                if param_3 == 1:
                    save_to = self.command_list[self.index+3]        

                mutliplication = first_number * second_number
                # print(save_to)
                self.command_list[save_to] = mutliplication

            if op == 3:
                # val = input("ID?")
                if self.phase != '':

                    val = in_value
                    save_to = self.command_list[self.index+1]
                    self.command_list[save_to] = int(val)
                else: 
                    self.phase = phase 
                    val = phase
                    save_to = self.command_list[self.index+1]
                    self.command_list[save_to] = int(val)



            if op == 4:
                # multiply
                index_to_return = self.index+1
                self.index = self.index+2
                
                if param_1 == 0:
                    return True, (self.command_list[self.command_list[index_to_return]])
                if param_1 == 1:
                    return True, (self.command_list[index_to_return])
            if op == 5:
                if param_1 == 0:
                    first_number = self.command_list[self.command_list[self.index+1]]
                if param_1 == 1:
                    first_number = self.command_list[self.index+1]
                if param_2 == 0:
                    second_number = self.command_list[self.command_list[self.index+2]]
                if param_2 == 1:
                    second_number = self.command_list[self.index+2]
                
                if first_number !=0:
                    self.index = second_number
                    modified_index = True

            if op == 6:

                if param_1 == 0:
                    first_number = self.command_list[self.command_list[self.index+1]]
                if param_1 == 1:
                    first_number = self.command_list[self.index+1]
                if param_2 == 0:
                    second_number = self.command_list[self.command_list[self.index+2]]
                if param_2 == 1:
                    second_number = self.command_list[self.index+2]
                
                if first_number ==0:
                    self.index = second_number
                    modified_index = True
            if op == 7:
                if param_1 == 0:
                    first_number = self.command_list[self.command_list[self.index+1]]
                if param_1 == 1:
                    first_number = self.command_list[self.index+1]
                if param_2 == 0:
                    second_number = self.command_list[self.command_list[self.index+2]]
                if param_2 == 1:
                    second_number = self.command_list[self.index+2]
                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    #print(self.command_list[self.index+3])
                if param_3 == 1:
                    save_to = self.command_list[self.index+3]   
                if first_number < second_number:
                    self.command_list[save_to] = 1
                else: 
                    self.command_list[save_to] = 0
                    
                
            if op == 8:
                if param_1 == 0:
                    first_number = self.command_list[self.command_list[self.index+1]]
                if param_1 == 1:
                    first_number = self.command_list[self.index+1]
                if param_2 == 0:
                    second_number = self.command_list[self.command_list[self.index+2]]
                if param_2 == 1:
                    second_number = self.command_list[self.index+2]
                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    #print(self.command_list[self.index+3])
                if param_3 == 1:
                    save_to = self.command_list[self.index+3]   
                if first_number == second_number:
                    self.command_list[save_to] = 1
                else: 
                    self.command_list[save_to] = 0
                    


            if op == 1 or op == 2 or op == 7 or op == 8:
                self.index +=4
            if op == 3 or op == 4:
                self.index +=2
            if (op == 5 or op == 6) and modified_index == False:
                self.index +=3



f = open("input","r")
for row in f:
    command_list_from_file=row.split(",")
f.close()
# print(command_list_from_file)

command_list_from_file = [int(i) for i in command_list_from_file]
# print(command_list_from_file)
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


#print(decode_op(1002))
    

    # print(index)
    # print(command_list)

    # if value == 99:
    #     print("stop!")
    #     break



f = open("input","r")
for row in f:
    command_list_from_file=row.split(",")
f.close()
# print(command_list_from_file)

command_list_from_file = [int(i) for i in command_list_from_file]
# print(command_list_from_file)
#command_list=[1,0,0,0,99]
#command_list = [2,3,0,3,99]
#command_list = [2,4,4,5,99,0]
#command_list = [1,1,1,4,99,5,6,0,99]

# replace position 1 with value 12

# replace position 2 with value 2
command_list=[]
output= 0

#possible_phases = [0,1,2,3,4]
possible_phases = [5,6,7,8,9]

phase_settings = itertools.permutations(possible_phases)
phase_settings = list(phase_settings)
print(phase_settings)
#command_list_from_file=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#command_list_from_file = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
#101,5,23,23,1,24,23,23,4,23,99,0,0]
# command_list_from_file = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

# command_list_from_file=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

largest_output = 0
largest_phase = 0
best_phase =[]
cont = True
output_value = 0
for phase_setting in phase_settings:
    output = (True, 0)
    print(phase_setting)
    amplifierA = Amplifier(command_list_from_file)
    amplifierB = Amplifier(command_list_from_file)
    amplifierC = Amplifier(command_list_from_file)
    amplifierD = Amplifier(command_list_from_file)
    amplifierE = Amplifier(command_list_from_file)

    print(amplifierA.command_list)
    print(amplifierA.phase)
    while output[0] == True:
        output = (amplifierA.runintcode(phase_setting[0], output[1]))
        output = (amplifierB.runintcode(phase_setting[1], output[1]))
        output = (amplifierC.runintcode(phase_setting[2], output[1]))
        output = (amplifierD.runintcode(phase_setting[3], output[1]))
        output = (amplifierE.runintcode(phase_setting[4], output[1]))
        print(output)
        if output[1]!=-1:
            output_value = output[1]
        print("lopd")

    # output = amplifierA.runintcode(0)
    if output_value>largest_output:
        largest_output = output_value
    #print(amplifierB.runintcode(1,5))
    #print(amplifierC.runintcode(2,54))
    # print(amplifierD.runintcode(455))
    # print(amplifierE.runintcode(4100))


    
        #     command_list = command_list_from_file.copy()
        # # print(phase)
        #     cont, output = runintcode(phase,output,command_list)
        #     if cont == False:
        #         print("stop!")
        #         break
        #     print(output)

# print(output)
print(largest_output)
#print(best_phase)

# 5
# 54
# 543
# 5432
# 54321
