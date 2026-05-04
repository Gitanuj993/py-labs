# .pop()

students1 = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan"
}

print(students1)

# x = students1["Aarav"] # KeyError: 'Aarav' , value given

# x = students1.pop() # TypeError: pop expected at least 1 argument, got 0

x = students1.pop(1)
print(x)
print(students1)

# what if we give a key which dosn't exist
# x = students1.pop(100)
# print(x)
# print(students1)
# KeyError: 100 gives an error if key is not found
