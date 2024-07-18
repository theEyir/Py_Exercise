numbers = [10, 23, 3, 5, 8, 2, 1, 445]

print(f"Original form --------------> {numbers}")
sortedTest = sorted(numbers)
print(f"\nChanged by 'sorted' def is -> {sortedTest}")
print(f"\nOriginal form --------------> {numbers}")
numbers.sort()
print(f"\nChanged by 'sort' def is ---> {numbers}")
print(f"Original form --------------> {numbers}")

print("\n-----------------------------Reverse()-----------------------------\n")

RevsortedTest = sorted(numbers, reverse=True)
print(f"\nChanged by 'Reverse sorted' def is -> {RevsortedTest}")

print("\n-----------------------------sort() in dictionary-----------------------------\n")

Users = [
    {'user' : 'p_1', 'banks' : ['Shahr', 'Melli', 'Mellat', 'Saman'], 'credit' : '10.5 m' },
    {'user' : 'p_2', 'banks' : ['Melli', 'Mellat'],                   'credit' : '2.743 m'},
    {'user' : 'p_3', 'banks' : ['Shahr', 'Saman'],                    'credit' : '0.547 m'}
]

print(sorted(Users, key = lambda user : user['user'], reverse = False))

print("\n-----------------------------Max() & Min()-----------------------------\n")

chars = ['a', 'e', 'A', 'x', 'F']
print(f"max num in numbers list is {max(numbers)} & max char list is '{max(chars)}'.")
print(f"min num in numbers list is {min(numbers)} & min char list is '{min(chars)}'.")

names = ['omid', 'ali', 'mostafa', 'mahan', 'Javad']
res = [len(name) for name in names]
print(res)
print(f"max of names by sorting in char count is {max(names, key = lambda n : len(n))}")
print(f"min of names by sorting in char count is {min(names, key = lambda n : len(n))}")
print(f"names list is {names}")

print("\n-----------------------------reversed()-----------------------------\n")

print(list(reversed(names)))