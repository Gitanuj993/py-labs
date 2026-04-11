st = "Hello"
print(f"id of {st} is : {id(st)}")
st = " Hello"
print(f"id of {st} is : {id(st)}")
st = "Welcome"
print(f"id of {st} is : {id(st)}")

# we can not change any string , string object st is immutable
# we can create a new object st which can store a new string value

# from the above code
"""
st at code line 1 has different string
st at code line 2 has different string
"""
