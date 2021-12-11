sample_input_1 = "1 + 2 * 3 + 4 * 5 + 6"
sample_input = "2 * 3 + (4 * 5)"
sample_input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
sample_input = "1 + (2 * 3) + (4 * (5 + 6))"
# st = sample_input
# print(st)
# st = st[st.find("(") + 1 : st.rfind(")")]
# print(st)
# st = st[st.find("(") + 1 : st.rfind(")")]
# print(st)
# st = st[st.find("(") + 1 : st.rfind(")")]
# print(st)


def calc(expression):
    # find
    print(f"expr is {expression}")
    calculating = True
    while calculating:
        splitted = expression.split(" ")
        print(expression)
        if len(splitted) == 1:
            return expression
        if expression.count("+") > 0 and splitted[1] == "+":
            new_expr = splitted[0] + splitted[1] + splitted[2]
            remaining_expr = splitted[3:]
            remaining_expr.insert(0, eval(new_expr))
            new_str = " "
            expression = new_str.join(map(str, remaining_expr))
        elif expression.count("+") == 0:
            new_expr = splitted[0] + splitted[1] + splitted[2]
            remaining_expr = splitted[3:]
            remaining_expr.insert(0, eval(new_expr))
            new_str = " "
            expression = new_str.join(map(str, remaining_expr))
        elif splitted[1] == "*":
            print("op is *")
            # loook for next +
            for i in range(0, len(expression) - 3):
                if i + 1 >= len(splitted):
                    break
                if splitted[i + 1] == "+":
                    new_expr = splitted[i] + splitted[i + 1] + splitted[i + 2]

                    old_expr = (
                        splitted[i] + " " + splitted[i + 1] + " " + splitted[i + 2]
                    )
                    print(old_expr)
                    print(expression)
                    expression = expression.replace(old_expr, str(eval(new_expr)))

                    print(expression)
                    break


# print(sample_input)
test_input_2 = "1 + 6 + (4 * (5 + 6))"
# new_list = list("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
# print(new_list)

import re

# test_input = test_input_2
file = open("input", "r")

database = file.read().splitlines()
result = []

for row in database:
    test_input = row
    print(test_input)
    new_input_list = re.findall(r"\(([^()]+)\)", test_input)
    # I did not manage to make this regex myself so I stole it from reddit
    # The rest of the code I did myself
    while new_input_list:
        print(new_input_list)
        for new_input in new_input_list:
            calc_input = calc(new_input)
            print(calc_input)
            print(new_input)
            test_input = test_input.replace("(" + new_input + ")", calc_input)
        new_input_list = re.findall(r"\(([^()]+)\)", test_input)
    # now add () around the + and do it again?
    print(test_input)
    print(calc(test_input))
    result.append(int(calc(test_input)))


print(sum(result))

# print(calc("1 + 2 * 3 + 4 * 5 + 6"))
