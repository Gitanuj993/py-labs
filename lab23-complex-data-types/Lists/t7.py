
# built in functions in sequence of elements

test1 = [print()]

test2 = [print("IIT")]

test3 = [ len(test1)]

print(f" test1 : {test1}  ")
print(f" test2 : {test2}  ")
print(f" test3 : {test3}  ")


print(print()) # None

print(print("AT")) # None

# conclusion : print(print())  , inner print() return None 