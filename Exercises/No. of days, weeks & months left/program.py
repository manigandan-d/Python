age = int(input("Enter your age: "))

yearsLeft = 100 - age
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left")
