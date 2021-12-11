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
        self.relative_base = 0


    # def get_first_number_0(self):
    #     return(self.command_list[self.command_list[self.index+1]])
    # def get_first_number_1(self):
    #     return(self.command_list[self.index+1])
    # def get_first_number_2(self):
    #    # return(self.command_list[self.command_list[self.relative_base]])
    #     return(self.command_list[self.relative_base])

    # def get_second_number_0(self):
    #     return self.command_list[self.command_list[self.index+2]]
    # def get_second_number_1(self):
    #     return self.command_list[self.index+2]
    # def get_second_number_2(self):
    #     return(self.command_list[self.command_list[self.relative_base]])
    def get_first_number_0(self):
        return(self.command_list[self.index+1])
    def get_first_number_1(self):
        return(self.command_list[self.index+1])
    def get_first_number_2(self):
       # return(self.command_list[self.command_list[self.relative_base]])
        return(self.command_list[self.index+1])

    def get_second_number_0(self):
        return self.command_list[self.index+2]
    def get_second_number_1(self):
        return self.command_list[self.index+2]
    def get_second_number_2(self):
        return self.command_list[self.index+2]
          
    def runintcode(self, in_value):
    
        # print(self.index)
        # print(value)
        while self.index <= len(self.command_list):
            modified_index = False

            param_1, param_2, param_3, op = decode_op(self.command_list[self.index])
            #print(op)
            if op == 1 or op == 2 or op == 5 or op == 6 or op == 7 or op == 8:
                if param_1 == 0:
                    first_number = self.get_first_number_0()
                elif param_1 == 1: 
                    first_number = self.get_first_number_1()
                elif param_1 == 2: 
                    first_number = self.get_first_number_2()
                if param_2 == 0:
                    second_number = self.get_second_number_0()
                elif param_2 == 1:
                    second_number = self.get_second_number_1()
                elif param_2 == 2:
                    second_number = self.get_second_number_2()
            if op == 9 or op == 4: 
                if param_1 == 0:
                    first_number = self.get_first_number_0()
                elif param_1 == 1: 
                    first_number = self.get_first_number_1()
                elif param_1 == 2: 
                    first_number = self.get_first_number_2() 
            if op == 99:
                print("stop")
                break
            
            elif op == 1:

                if param_1 == 0:
                    num1 = self.command_list[first_number]
                elif param_1 == 1: 
                    num1 = first_number 
                elif param_1 == 2: 
                    num1 = self.command_list[first_number + self.relative_base]
                
                if param_2 == 0:
                    num2 = self.command_list[first_number]
                elif param_2 == 1: 
                    num2 = first_number 
                elif param_2 == 2: 
                    num2 = self.command_list[first_number + self.relative_base]
                
                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    # print(self.command_list[self.index+3])
                elif param_3 == 1:
                    save_to = self.index+3
                elif param_3 == 2:
                    save_to = self.command_list[self.relative_base]

                addition = num1 + num2
                # print(save_to)
                self.command_list[save_to] = addition
            elif op == 2:
                # multiply
                if param_1 == 0:
                    num1 = self.command_list[first_number]
                elif param_1 == 1: 
                    num1 = first_number 
                elif param_1 == 2: 
                    num1 = self.command_list[first_number + self.relative_base]
                
                if param_2 == 0:
                    num2 = self.command_list[first_number]
                elif param_2 == 1: 
                    num2 = first_number 
                elif param_2 == 2: 
                    num2 = self.command_list[first_number + self.relative_base]
                
                
                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    #print(self.command_list[self.index+3])
                elif param_3 == 1:
                    save_to = self.index+3
                elif param_3 == 2:
                    save_to = self.command_list[self.relative_base]  




                mutliplication = num1 * num2
                # print(save_to)
                self.command_list[save_to] = mutliplication
            elif op == 3:
                if param_1 ==0:
                    val = in_value
                    save_to = self.command_list[self.index+1]
                    self.command_list[save_to] = int(val)
                elif param_1 == 1:
                    val = in_value
                    save_to = val
                    self.command_list[save_to] = int(val)

                elif param_1 ==2:
                    val = in_value
                    save_to = self.command_list[self.relative_base]
                    self.command_list[save_to] = int(val)

            elif op == 4:
                if param_1 == 0 or param_1 == 1:
                    index_to_return = first_number
                    self.index = self.index+2
                elif param_1 == 2:
                    index_to_return = first_number + self.relative_base
                    self.index = self.index + 2 
                if param_1 == 0 or param_1 == 2:
                    print(self.command_list[index_to_return])
                if param_1 == 1:
                    #print(self.command_list[index_to_return])
                    print(index_to_return)
            # elif op == 4:
            #     if param_1 == 0:
            #         #temp_idx = self.index+1
            #         index_to_return = first_number
            #         self.index = self.index+2
            #     elif param_1 == 1: 
            #         index_to_return = first_number
            #     elif param_1 == 2:
            #         index_to_return = self.command_list[self.relative_base + first_number]
            #         self.index = self.index + 2 
            #     if param_1 == 0 or param_1 == 2:
            #         print(self.command_list[index_to_return])
            #     if param_1 == 1:
            #         print(index_to_return)

            elif op == 5:
                if param_1 == 0:
                    num1 = self.command_list[first_number]
                elif param_1 == 1: 
                    num1 = first_number 
                elif param_1 == 2: 
                    num1 = self.command_list[first_number + self.relative_base]
                
                if param_2 == 0:
                    num2 = self.command_list[first_number]
                elif param_2 == 1: 
                    num2 = first_number 
                elif param_2 == 2: 
                    num2 = self.command_list[first_number + self.relative_base]

                if num1 !=0:
                    self.index = num2
                    modified_index = True

            
            elif op == 6:
                if param_1 == 0:
                    num1 = self.command_list[first_number]
                elif param_1 == 1: 
                    num1 = first_number 
                elif param_1 == 2: 
                    num1 = self.command_list[first_number + self.relative_base]
                
                if param_2 == 0:
                    num2 = self.command_list[first_number]
                elif param_2 == 1: 
                    num2 = first_number 
                elif param_2 == 2: 
                    num2 = self.command_list[first_number + self.relative_base]

                if num1 ==0:
                    self.index = num2
                    modified_index = True

            elif op == 7:

                if param_1 == 0:
                    num1 = self.command_list[first_number]
                elif param_1 == 1: 
                    num1 = first_number 
                elif param_1 == 2: 
                    num1 = self.command_list[first_number + self.relative_base]
                
                if param_2 == 0:
                    num2 = self.command_list[first_number]
                elif param_2 == 1: 
                    num2 = first_number 
                elif param_2 == 2: 
                    num2 = self.command_list[first_number + self.relative_base]

                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    #print(self.command_list[self.index+3])
                elif param_3 == 1:
                    save_to = self.index+3
                elif param_3 == 2:
                    save_to = self.command_list[self.relative_base] 


                if num1 < num2:
                    self.command_list[save_to] = 1
                else: 
                    self.command_list[save_to] = 0
                    
                
            elif op == 8:
                if param_1 == 0:
                    num1 = self.command_list[first_number]
                elif param_1 == 1: 
                    num1 = first_number 
                elif param_1 == 2: 
                    num1 = self.command_list[first_number + self.relative_base]
                
                if param_2 == 0:
                    num2 = self.command_list[first_number]
                elif param_2 == 1: 
                    num2 = first_number 
                elif param_2 == 2: 
                    num2 = self.command_list[first_number + self.relative_base]

                if param_3 == 0:
                    save_to = self.command_list[self.index+3]
                    #print(self.command_list[self.index+3])
                elif param_3 == 1:
                    save_to = self.index+3
                elif param_3 == 2:
                    save_to = self.command_list[self.relative_base]
                if num1 == num2:
                    self.command_list[save_to] = 1
                else: 
                    self.command_list[save_to] = 0

            elif op == 9:
                if param_1 == 0:
                    self.relative_base = self.relative_base + self.command_list[first_number]
                elif param_1 == 1:
                    self.relative_base = self.relative_base + first_number
                elif param_1 == 2:
                    self.relative_base = self.relative_base + self.command_list[self.relative_base + first_number]
            else:
                print("unknown opceode!")

            if op == 1 or op == 2 or op == 7 or op == 8:
                self.index +=4
            if op == 3 or op == 9:
                self.index +=2
            if (op == 5 or op == 6) and modified_index == False:
                self.index +=3

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


f = open("input","r")
for row in f:
    command_list_from_file=row.split(",")
f.close()
# print(command_list_from_file)

command_list_from_file = [int(i) for i in command_list_from_file]

# add some zeroes to the command_list! 

# print(command_list_from_file)
#command_list=[1,0,0,0,99]
#command_list = [2,3,0,3,99]
#command_list = [2,4,4,5,99,0]
#command_list = [1,1,1,4,99,5,6,0,99]

# replace position 1 with value 12

# replace position 2 with value 2
command_list=[]
output= 0
#command_list_from_file=[1102,34915192,34915192,7,4,7,99,0]
#command_list_from_file = [104,1125899906842624,99]

#command_list_from_file=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

#command_list_from_file=[109, -1, 4, 1, 99]
#command_list_from_file=[109, -1, 104, 1, 99]
#command_list_from_file=[109, -1, 204, 1, 99]
#command_list_from_file=[109, 1, 9, 2, 204, -6, 99]
#command_list_from_file = [109, 1, 109, 9, 204, -6, 99]
command_list_from_file = [109, 1, 209, -1, 204, -106, 99]
#command_list_from_file = [109, 1, 3, 3, 204, 2, 99]
#command_list_from_file=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
#]
command_list_from_file=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
for i in range(0,5000):
    command_list_from_file.append(0)

output = (True, 0)
amplifierA = Amplifier(command_list_from_file)
#print(amplifierA.command_list)
print("running")
amplifierA.runintcode(0)
