# .popitem(x)

std1 = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan"
}

print(std1)

std1.popitem()
print(std1)
std1.popitem()
print(std1)

std1.popitem()
print(std1)
std1.popitem()
print(std1) # empty list

# can't delete empty dict
# std1.popitem()
#KeyError: 'popitem(): dictionary is empty'

