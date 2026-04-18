# global function : enumerate() , previously it shows (index,element)
# Now it will enumerate (index,key)
# enumerate return address of an iterator which runs only once

d1 = { }
dict_students = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan",
    5: "Arjun",
    6: "Sai",
    7: "Reyansh",
    8: "Krishna",
    9: "Ishaan",
    10: "Rohan"
}

print(dict_students)
# method - returns address of iterator
enumerated = enumerate(dict_students)
# converting enumerate into dictionary
dict_enumerated = dict(enumerate(dict_students))
# print dictionary
print(f" dict_enumerated : {dict_enumerated}")
# type of enumerate
print(f" type(enumerated) = {type(enumerated)}")
# type of enumerated address
print(f" Type of address is : {type(enumerate(dict_students))}")
# convering address of enumerate into list
print(list(enumerated))


# using for loop key value pair and for loop using two iterators
for index,value in enumerated:
    print(f"index : {index}  and value : {value}")


# 40% python