"""
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

expenses = [2200, 2350, 2600, 2130, 2190]

print(expenses[1] - expenses[0], " dollars spent extra in Feb")
print(
    "Total Expenses in First quarter is %d" % (expenses[0] + expenses[1] + expenses[2])
)

if 2000 in expenses:
    print(" Exists that expense in one month ")
else:
    print("Not exists in any month!")

expenses.append(1980)
print(expenses)

refund_Exp = expenses[3] - 200
expenses.remove(2130)
expenses.insert(3, refund_Exp)
print(expenses)
