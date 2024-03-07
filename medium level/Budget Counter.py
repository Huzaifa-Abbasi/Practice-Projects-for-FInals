'''Budget Calculator:
1.Write a program that asks the user for their monthly income and expenses.
2.Calculate the difference between income and expenses.
3.If the difference is positive, display a message indicating how much the user can save.
4.If the difference is negative, display a message indicating how much the user is overspending.'''

income = int(input("Enter your Monthly Income: "))
expenses = int(input("Enter your Monthly expenses: "))

difference = income - expenses
if income > expenses:
    print(f"You can save {difference}$ amount ")
else:
    print(f"You overspent {difference}$ amount ")