#raise IndexError("You Entered a WRONG value :(")      
# ctrl + space

#raise ValueError('Invalid Value')

def stus(name, grade) :
    if type(name) is not str :
        raise ValueError('invalid value entered :(')
    else :
        print(f"\nStudent {name} status is {grade}\n")

stus("Shahrooz", 90.5)

myname = 'klhkgjfhfg'
try :
    print(myname)
except KeyError :
    print("\nan Err accured")
except IndexError :
    print(None)
except NameError :
    print("\nthere is no name")
else :
    print("\nMission Complete...\n")
finally :
    print("The finally section")

print("\n------------------- Q -------------------\n")

def divider(frst, scnd) :
    try :
        return frst / scnd
    except ZeroDivisionError :
        print("\nZero Division Error accured\ntry again please")
    except TypeError as err:
        print(err)
        print("do again\n")
    finally :
        print("\nMission Complete...\n")

print(divider(5, 'hkhjl'))