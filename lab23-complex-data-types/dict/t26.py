# dict.fromkets(x,y)
# creates a new dictionary

d1 = { 1 : "A" , 2 : "B" , 3 : "C" }
d2 = { "a" : 1, "b" : 2, "c" : 3 }

print(f" d1 : {d1}")
print(f" d2 : {d2}")
# what does dict.fromkeys(d1,"True")
d3 = d1.fromkeys(d2)
print(f" d3 : {d3}")
print(f" d1 : {d1}")
print(f" d2 : {d2}")

dict1 = d1.fromkeys("True")
print(f" dict1 : {dict1}")

dict2 = d1.fromkeys(d1,"True")
print(f" dict2 : {dict2}")

dict = d2.fromkeys(d2,"True")
print(f" dict : {dict}")

dict = d2.fromkeys(d1,"True")
print(f" dict : {dict}")
