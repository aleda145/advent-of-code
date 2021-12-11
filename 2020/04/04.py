file = open("input","r")

database = file.read().splitlines()

def check_valid_data(pass_dict):
    for key, value in pass_dict.items():
        try:
            if key == "byr":
                if int(value) > 2002 or int(value) < 1920:
                    return False
            if key == "iyr":
                if int(value) > 2020 or int(value) < 2010:
                    return False            
            if key == "eyr":
                if int(value) > 2030 or int(value) < 2020:
                    return False            
            if key == "hgt":
                if value[-1] == "m":
                    if int(value[0:3]) > 193 or int(value[0:3]) < 150:
                        return False           
                elif value[-1] == "n":
                    if int(value[0:2]) > 76 or int(value[0:2]) < 59:
                        return False
                else:
                    return False
            if key == "hcl":
                if value[0] != "#":
                    return False
                if len(value) != 7:
                    return False
                for char in value:
                    if char not in ["#","0","1","2","3","4","5","6","7","8","9","#","a","b","c","d","e","f"]:
                        return False
            if key == "ecl":
                if value not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                    return False
            if key == "pid":
                if len(value) != 9 or not value.isnumeric():
                    return False
            
                        
        except Exception as e:
            print(e)

            print("bad input")
            print(pass_dict)
            print(key)
            print(value)
            return False
    return True

def check_if_valid_passport(passport):
    valid_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    }
    optional = "cid"
    valid_count = 0
    pass_fields = passport.split(" ")
    pass_set = set()
    num_fields = 0
    pass_dict = {}
    for pass_field in pass_fields:
        if pass_field != "":
            pass_key = pass_field.split(":")[0]
            if pass_key != optional:
                pass_value = pass_field.split(":")[1]
                pass_dict[pass_key] = pass_value
                num_fields += 1
                pass_set.add(pass_key)
    if pass_set == valid_fields and num_fields == 7:
        if check_valid_data(pass_dict):
            return True
        else:
            print("bad fields")
    else:
        print("missing:")
        print(valid_fields-pass_set)
        return False


passport = ""
passport_list = []
database.append("")
for row in database:
    passport+=(" "+ row)
    #print(row)
    if row =="": #failing to read the last passport with this method!
        passport_list.append(passport)
        passport = ""


valid_pass = 0
for passport in passport_list:
    #print(passport)
    print(passport)
    if check_if_valid_passport(passport):
        valid_pass += 1
    

print(valid_pass)
    