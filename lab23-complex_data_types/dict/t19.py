# dict as json
# json is used to communicate between programming languages

# as program first converted into machine code then it run , as in case of apis
# each time program hits is first program converted into machine code then execute api key


# add # merge
d1 = dict(a=1, b=2, c=3)
d2 = dict(a=1, b=2, c=3)

dict1 = dict(zip(d1.keys() , d2.values()))
print(f"dict1 : {dict1}") # key - value pair

dict2 = dict(zip(d1.keys() , d2.keys()))
print(f"dict1 : {dict2}") # key - keys pair

dict3 = dict(zip(d1.values() , d2.values()))
print(f"dict1 : {dict3}") # value - value pair

dict4 = dict(zip(d1.values() , d2.keys()))
print(f"dict1 : {dict4}") # key - value pair


