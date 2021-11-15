print("-------------Normal range practice.")
number = list(range(1,10))
print(number,"\n")

print("-------------Normal range practice.")
number = list(range(10,1, -1)) # for reverse range .
print(number,"\n")

print("-------------squares list convert practice.")
squares = []
for value in range(1,11):
    # a = value ** 2
    # squares.append(a)
    squares.append(value ** 2) # this code more concisely --all in one line.
    # print(squares)
print(squares,"\n")

squares2 = [ value ** 2 for value in range(1,11)] # more professional efficient code
print(squares2,"\n")