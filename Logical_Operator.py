# logical operators
#   and , or , not

UserAge = input("Enter your age : ")
UserGender = input("Enter your gender : ")
UserAge = int (UserAge)
if UserAge >= 18 and UserGender == 'male' :
    print(" You have to go to Soldiery :)")
else:
    print("it's your chance :) ")

print("----------------------")
print(f" True  and True   -> {True  and True} ")
print(f" True  and False  -> {True  and False}")
print(f" False and True   -> {False and True} ")
print(f" False and False  -> {False and False}")
print("----------------------")

print(f" True  or True   -> {True  or True} ")
print(f" True  or False  -> {True  or False}")
print(f" False or True   -> {False or True} ")
print(f" False or False  -> {False or False}")
print("----------------------")

IsBrotherComing = False
if not IsBrotherComing :    # here 'not' will return False to True
    print("My brother says: I won't com")

print(f" Not True   -> {not True} ")
print(f" Not False  -> {not False}")