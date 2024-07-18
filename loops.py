# for , while

#   for
#syntax:
# for item in collection
#   pass
#some kindes of collections : list of Numbers, list of characters in  a string, range of numbers like range (1, 5), etc.

ListofNum = [2, 3, 5, 20, 18, 92, 43]
for num in ListofNum:
    print(num)

MyNAme = 'Sammet'
for char in MyNAme:
    print(char)

RangeofNumber = range(1,10)
for n in RangeofNumber:
    print(n)
print(list(range(0,10,2)))  # [0, 2, 4, 6, 8]
print(list(range(10,0,-1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("-----------while-----------")

# while True/False (expression):
#       command

password = input("Please enter your password : ")

while password != "1234":
    print("You ener wrong value; Please try again : ")
    password = input ()

print("Welcom :)")








