from functools import reduce
file = open("input","r")
expenses = []
for expense in file: 
    expenses.append(int(expense))

expense_dict = {}

# solution 1 O(n)
for expense in expenses:
    expense_dict[expense]=expense
    diff = 2020 - expense
    if diff in expense_dict:
        print(expense*expense_dict[diff])

diff_dict = {}
# solution 2 O(n^2)
for expense_second in expenses:
    for expense_first in expenses:
        diff = 2020 - expense_second - expense_first
        diff_dict[diff] = [expense_first,expense_second]

for expense in expenses:
    if expense in diff_dict:
        expenses_list = diff_dict[expense]
        expenses_list.append(expense)
        print(expenses_list)
        print(reduce(lambda x,y: x*y, expenses_list))