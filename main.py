import random
names=str(input("Enter your all friends name with a space"))
names_splitted = names.split(" ")
print(names_splitted)
bill_pay_by = random.choice(names_splitted)
print(bill_pay_by)
