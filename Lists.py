print("---------------LIST---------------")
item1 = "python"
item2 = "C++"
item3 = "NetWork"

myList = [item1, item2, item3, 20.2]

# len() ---> length of List
print(len(myList))

print(myList[1])    # like array in c++
print(myList[-1])   # if enter a - number, list starts from end

isexist = "NetWork" in myList
print(isexist)
print("\n-----------------------------")

for skill in myList:
    if type(skill) == str:
        print(f"your skill is {skill}")
    else:
        print(f"{skill} is not a skill but exist in your list")

print("\n-------------Functions for lists-------------")
print("    ---------   add new object  ---------")
myList.append("Java")   # Just add one arguman   # You can  add a another list to your defult list
print(myList)

myList.extend(["html", "css"])
print(myList)

myList.insert(2, "C")    # you can add a - number
print(myList)

print("\n    ---------delete one or more object---------")
# myList.clear()    # remove all elements
# print(myList)

NotStr = myList.pop(4)
print(myList)   # if () be empty then delete the last element   # if (number), remove an element with number index
print(f"{NotStr} is not one of my skill")

myList.remove("C")  # find first "value" in list and remove it
myList.remove("Java")
print(myList)

print("\n-------------Index function-------------")
html_Index = myList.index("html")   # if have more than one "value" in list we can ("value",1,4) search from 1 to 4
print(f"The index of html is {html_Index}")

html_counts = myList.count("html")
print(f"The count of html is {html_counts}\n")

print(myList)
myList.reverse()
print(myList)

print("\nNow we want to sort our list, but we have char, then it sorts by ASCII code")
myList.sort()
print(myList)

print("\n----------------------------------")
myList_1 = " , ".join(myList)   # put all elements in a string
print(myList_1)

print("\n-------------Slicing-------------")
selectedSkills = myList[1:3:1]      # list_name [start : end : step]
print(selectedSkills)       # copying some elements of list to a new list
selectedSkills_1 = myList[1:]
print(selectedSkills_1)
selectedSkills_2 = myList[-3:]
print(selectedSkills_2)
selectedSkills_3 = myList[:2]
print(selectedSkills_3)
selectedSkills_4 = myList[::3]
print(selectedSkills_4)

print("\n--------------------------a hint")
copyoflist = myList[:]
print(myList)
print(copyoflist)
print(myList == copyoflist)
print(myList is copyoflist)

print("\n-------------fun-------------")
myName = "Ali Alizadeh"
print(myName[::-1])