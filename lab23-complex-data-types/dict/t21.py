# .get(c)

dict_students1 = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan"
}

# check whether we can access or return values from a key  # input checking : Error handling

# check for roll_number
print(f" is roll_no 1 in dict : {dict_students1[1]}") # if it shows then key exist

# what if want to access a key which is not present in the dict
# print(f" is roll_no 20 in dict : {dict_students1[20]}")
# KeyError: 20

# to counter above problem we created a new method
print(f" is roll_no 1 in dict : {dict_students1.get(1)}") # if it shows then key exist
print(f" is roll_no 20 in dict : {dict_students1.get(20)}")
# retunr None if element or key not found