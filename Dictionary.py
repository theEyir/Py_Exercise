# lists
#Shoping card
#    item 1
#        price
#        numbers
#        name 
#    item 2
#        price
#        numbers
#        name 
#    item 3
#        price
#        numbers
#        name

#Dictionary =
#{
#    'key' = value
#}

#MyDict = {
#    "name" : "item 1",
#    "price": 4700,
#    "count": 3
#}

#print(MyDict)

MyDict_2 = dict(password_u1 = '123456' , user = 'ebram')
print(MyDict_2)
print(MyDict_2['password_u1'])
print(MyDict_2['user'])

for value in MyDict_2.values() :
    print('---------------------')
    print(value)

print('\n-----------access to keys----------\n')
print(MyDict_2.values())
print(MyDict_2.keys())

print('\n-----------another access to values----------\n')
for key in MyDict_2.keys() :
    print(MyDict_2[key])


print('\n-----------access to all items----------\n')
for item in MyDict_2.items() :
    print(item)

print('\n-----------another access to all items----------\n')
for key, value in MyDict_2.items() :
    print(key,' : ', value)

isExist = 'email' in MyDict_2
print('\n-----------check some items are in our dict or not----------')
print(isExist)
if 'email' in MyDict_2 :
    print(MyDict_2[email])
else :
    print("key NOT found :(")

print('\n-----------check some values are in our dict or not----------')
if 'ebram' in MyDict_2.values() :
    print('True')
else :
    print("value NOT found :(")


# .fromkeys ---> used to generating default values
# .get --------> used to check some values or keys are exit in dict without code err
# .pop --------> used to delete key & value     //////      pop method will return the value wich will delete
# .popitem ----> used to delete last key & value
# .update -----> used to write or over write a dict on other dict

# Comprehension in Dicrionary
times = dict(
    first = 1,
    second = 2,
    third = 3,
)
squareNums = { key : value ** 2 for key , value in times.items() } 
print("\n", squareNums.values())
SimpleNums = { num : ("even" if num%2==0 else "odd") for num in [1, 2, 3, 4, 5, 6, 34, 485, 87438]}
print("\n--------", SimpleNums)


print("\n\n------\tEnd of Dictionary\t------")