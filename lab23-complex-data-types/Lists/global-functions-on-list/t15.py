# list.extend(x) function of class <list> on objects

l1 = [1,2,3,4]
l2 = [9,8,7]

# above reference variables l1 and l2 are objects or instances of the class <list> ,
# It will be discussed in the labs of OOPM : object Oriented Programming and Methodology

print(f" l1 is : {l1} of length : {len(l1)}")
print("------After extend----------")
l1.extend(l2)
print(f" l1 is : {l1} of length : {len(l1)}")

