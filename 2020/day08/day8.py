database = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
database = database.splitlines()

file = open("input", "r")

database = file.read().splitlines()

inst_list = []
true_inst_list = []
for instruction in database:
    inst_list.append(instruction)
    true_inst_list.append(instruction)

change_index = 0
success = False
while not success:
    inst_list = true_inst_list.copy()
    op_to_change = inst_list[change_index][0:3]
    value_for_op = inst_list[change_index][3:]
    if op_to_change == "nop":
        new_op = "jmp"
        inst_list[change_index] = new_op + value_for_op
    elif op_to_change == "jmp":
        new_op = "nop"
        inst_list[change_index] = new_op + value_for_op
    change_index += 1
    index = 0
    accum = 0
    visited_indexes = []
    booting = True

    while booting:
        op = inst_list[index][0:3]
        print("cur op " + inst_list[index])
        visited_indexes.append(index)
        if op == "nop":
            index += 1
        elif op == "acc":
            if inst_list[index][4] == "+":
                accum += int(inst_list[index][5:])
            elif inst_list[index][4] == "-":
                accum -= int(inst_list[index][5:])
            index += 1

        elif op == "jmp":
            if inst_list[index][4] == "+":
                index += int(inst_list[index][5:])
            elif inst_list[index][4] == "-":
                index -= int(inst_list[index][5:])
            if index in visited_indexes:
                booting = False
                print("boot loop found, exit")
        if index >= len(inst_list):
            booting = False
            success = True
            print("found it!")
print(accum)