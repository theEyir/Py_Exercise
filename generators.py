# generators are used for functions wich works part by part during the execution
# it's used for memory safe
# remember last state
# when I don't know how much number i have or when using many numbers and I want use less memory
def firstn ():
    yield 3
    yield 2
    yield 1

for i in firstn() :
    print(i)

print("------------------------------")

def lastn(n) :
    i = 0
    while (i<n) :
        yield i
        i += 1

for i in lastn(10) :
    print(i)
