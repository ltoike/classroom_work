user_in = input("Your salary is: ")
salary = int(user_in)

user_in = input("Monthly credit payment is: ")
credit = int(user_in)

user_in = input("Monthly utility bill: ")
utility = int(user_in)

result = salary - credit - utility

print("Your remains: ", result)
