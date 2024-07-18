simpleList  = [1, 2, 3, 4, 5, 6]
simpleTuple = (1, 2, 3, 4, 5, 6)    #immutable List     ///     safer codes

print(simpleTuple[0])

# Good Example for tuple : locations

locations = {
    (39.5, 45, 54) : 'Tehran',
    (44, 53.6, 32) : 'Rasht',
    (45, 34, 83.7) : 'NY'
}
print(locations[(39.5, 45, 54)])

print("\n---------------------\n")

print(simpleTuple.index(4))

