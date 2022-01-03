#a simple example

car= ['adi','raju','jakir','asif']
for cars in car:
    if cars == 'raju': # only one canditon is true that why raju will be upercase.
        print(cars.upper())
    else:
        print(cars.title()) # 1,3,4 number vlue print this condition cz car not equal 'raju'