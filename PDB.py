import pdb

pdb.set_trace()

# Common pdb cpmmands :
# l -> list of instructions
# n -> next line
# c -> continue the process / finish debugging
# p -> print value of a variable

number_1 = int(input('.:. Enter a num_1 please : '))
number_2 = int(input('.:. Enter a num_2 please : '))
result = number_1 + number_2

print(f" ...result = {result}\n")

def summing(a, b, c) :
    import pdb; pdb.set_trace()
    return a + b + c

print( summing(3, 5, 6) )