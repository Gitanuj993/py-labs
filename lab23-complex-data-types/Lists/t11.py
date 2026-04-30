# accessing elements of list

marks = [1 ,2 ,3,4,5 ,89 ,45 ,32 ,45,23]

# To traverse the list
for mark in  marks :
    print(mark , end=" ")

updatedMarks = [ x + 5 for x in marks]
print(updatedMarks)
show = [ print(x) for x in  marks]
print(show)