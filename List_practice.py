print("----------List pop method practice")
value = ["raju", "mia", "student"]
print(value)
popped_value = value.pop() #deleted last value and which value was deleted that the stort in popped_value variable.
print(value) #show the list without last remove value.
print(popped_value) # show the removing value cz which value was pop --that ws track.

print("----------sort List practice")
sort_list = ["one", "two", "there", "four", "five", "six","amer"]
print(sort_list)
sort_list.sort() # sort method convert all list value by alphabetical order.
print(sort_list)
sort_list.sort(reverse=True) #reverse alphabetically order by passing argument reverse = True
print(sort_list)


print("\nwe can copy list---------")
var1 = list(range(1,5))
var2 = var1[:]
print(var1)
print(var2)
var2.append(22)
print(var2)
var1.remove(1)
print(var1)