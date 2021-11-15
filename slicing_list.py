
list_valu = []
for i in range(1,10):
    list_valu.append(i)
print(list_valu)
print(list_valu[1:4],"\n")


num = list(range(1,11))
print(num)
print(num[-3:])
print(num[-3:-1])
print(num[-7:7],"\n")

loop_slice = ['amer', 'soner', 'bangla', 'ani', 'tmai', 'valubashi']
for value in loop_slice[:3]:
    print(value.title())
print("\n")

values = list(range(1,15))
print(values)
print("\n")
for value in values[:3]:
    print(value)