
# . setdefault(key,value)
# we can add a default key in a dictionary , default behavior


students1 = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan"
}

print(f" students1 is : {students1}")

students1.setdefault("Manav") # key : None
print(f" students1 is : {students1}")

students1.setdefault(20,"Ram")
print(f" students1 is : {students1}")

# make existing element as default

new_defalut_name = "Naman"
students1.setdefault(1,new_defalut_name)
print(f" students1 is : {students1}") # no change in
