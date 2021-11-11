First_name = "raju"
Second_name = "mia"
full_name = f"{First_name} {Second_name}"
print(f"Hello, my name is {full_name.title()}!")
full_name2 = "{} {}".format(First_name, Second_name)
print(full_name2)

#----------------
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

#----------------
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

#String format()
text = 44
my = "my age is {} and i am from bangladesh"
print(my.format(22))

#Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

