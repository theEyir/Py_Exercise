#   def function_name () :
#        command

def Say_Hello () :
    print ("HELLO :)\nWelcome to Functions course")
    print ("<-------------------------->\n")

print(Say_Hello())
# ------------------------------------------------
def returnSomeThing () :
    return "The test returned successfully"     # return should be the last code in defs

ReturnTest = returnSomeThing()
print (ReturnTest)

# ------------------------------------------------

def addTwoNums () :
    print("\n")
#    a = int(input("Enter a : "))
#    b = int(input("Enter b : "))
#    return a + b

print(addTwoNums())

# ------------------------------------------------

def sendig (parameter) :
    return int(parameter) + 3

print (sendig(7))

def Users (username, password = 0000) :
    Us_1 = str(username)
    pass_1 = password
    print("\nYour account created successfully\nUsername :", Us_1, "\nPassword :", pass_1)
#    return f"\nYour account created successfully\nUsername : {Us_1}\nPassword : {pass_1}"

Users('The_Ey',1254620)

# ------------------------------------------------
def Sum_some_Nums (*args) :     # gets tuples
    print(args, "\t<<<< This is tuple")
Sum_some_Nums(5, 8, 9, 9, 6, 4, 3)

def Shoes (**kwargs) :      # gets dictionary   ///     # kwargs = key word args
    print(kwargs, "\t<<<< This is dictionary")
Shoes(size = 43 , model = 'rahpa' , brand = 'Melli')

# when we want to send tuple to a def, we should use *arg for access to items
# when we want to send dictionary to a def, we should use **arg for access to values

# end-----------------