# for-loop in dict

# dict is an unordered pair
my_dict = {
    "name": "Rahul",
    "age": 25,
    "city": "Indore"
}

# lets print name in my_dict
# print(f" -------> my_dict: {my_dict[0]}")
# Error

for i in my_dict :
    print(i)
    print(f"{i} : {my_dict[i]}") # i is key we can access elements by its key


# delete a key value pair in dict

my_dict = {
    "name": "Rahul",
    "age": 25,
    "city": "Indore"
}
print(f" my_dict: {my_dict}")

del my_dict["city"]
print(f" my_dict: {my_dict}")
del my_dict["name"]
del my_dict["age"]
print(f" my_dict: {my_dict}")

