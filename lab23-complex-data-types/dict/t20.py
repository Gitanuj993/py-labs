# .items() , no parameters

students1 = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan"
}
# whole dictionary
print(f"students1 : {students1}") # in dictionary

# print key value pairs
print(f" .items() : {students1.items()}")  # list of key-values pairs in tuple
# let's check
print(f" type of .items() : {type(students1.items())}")  # < dict 'keys'>

# print only keys
print(f" .keys() : {students1.keys()}")  # returns list of keys
# let's check

print(f" type of .keys() : {type(students1.keys())}")  # < dict 'keys'>
# print only values
print(f" .values() : {students1.values()}") # list of values
# class explore
print(f" type of .values() : {type(students1.values())}")  # < dict 'keys'>

