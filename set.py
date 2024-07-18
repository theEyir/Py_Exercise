numbers = {1, 2, 3, 4, 4, 4, 5, 5, 5, 'cd', 'z', 'ali'}       # all duplicate or more items, will count just once
print(numbers)
print("\n", 4 in numbers)

for item in numbers :
    print(item)

someList = ['ali', 'amir', 'arman', 'ahmad']
someList_Set = set(someList)
print("\nsome List as Set : ", someList_Set)       # in set we don't have access to items
print("\nsome Set as List : ", list(numbers)[6])   # when change set to list, items came to list unique

# .add() ------> add a unique item
# .remove() ---> remove an item  == .discard() --------> if item doean't exist don't show err
# .copy() -----> copy items
# .clear() ----> make a empty set

# میتوانیم اجتماع و اشتراک بگیریم

print( "\nUnion of two sets : ", numbers | someList_Set )     # اجتماع
print( "\nIntersection  of two sets : ", numbers & someList_Set )     # اشتراک


characters = { char for char in "Hello Every People, Welcom:)" }
print("\n>>", characters, "\n<<")

# end of Sets