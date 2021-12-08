file = open("input", "r")

database = file.read().splitlines()

# database = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# """
# database = database.splitlines()


def generate_addresses(address_list):
    # find where there are X's.
    x_list = []
    for idx, char in enumerate(address_list):
        if char == "X":
            x_list.append(idx)

    import itertools

    # generate possible
    new_x_list = list(itertools.product(["0", "1"], repeat=len(x_list)))
    print(new_x_list)
    new_addresses = []
    for new_x in new_x_list:
        new_list = address_list.copy()
        for x_index, x in enumerate(x_list):
            new_list[x] = new_x[x_index]
        new_addresses.append(new_list)
    new_adress_str_list = []
    for address in new_addresses:
        new_adress_str_list.append(int("".join(address), 2))
    return new_adress_str_list


mem = {}
mask = ""
for row in database:
    if "mask" in row:
        mask = row.split(" = ")[1]
    elif "mem" in row:
        number = int(row.split(" = ")[1])
        address = int(row.split(" = ")[0].split("mem[")[1][:-1])
        # apply mask
        print(bin(number))
        result = []
        last_index = 0
        result = [char if char != "X" else "0" for char in mask]
        for index, num in enumerate(reversed(bin(number)[2:])):  # [2:] to skip 0b
            print(f"idx: {index}, num: {num}")
            mask_val = mask[len(mask) - index - 1]
            print(f"mask_val : {mask_val}")
            if mask_val == "0" or mask_val == "1":
                print("make change!")
                result[len(result) - index - 1] = mask_val
            else:
                result[len(result) - index - 1] = num
        print("".join(result))
        # writing to mem
        new_adress = [char for char in mask]
        for index, adress_num in enumerate(reversed(bin(address)[2:])):
            mask_val = mask[len(mask) - index - 1]
            if mask_val == "0":
                new_adress[len(new_adress) - index - 1] = adress_num
            elif mask_val == "1":
                print("adress change")
                new_adress[len(new_adress) - index - 1] = "1"
            elif mask_val == "X":
                new_adress[len(new_adress) - index - 1] = "X"
        print(f"og adress: {bin(address)[2:]}")
        print("".join(new_adress))
        # now generate new strings from the possible combinations with the X.
        adresses = generate_addresses(new_adress)
        for new_adress in adresses:
            mem[new_adress] = int(number)


print(sum(mem.values()))
