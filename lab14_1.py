"""
Welcome AT
continued lab-14
"""
# converting string to float and checking test-cases ,edge-cases and constraints

st = "1234"
print(f" st = {st} of type = {type(st)} in int is {int(st)} with type {type(int(st))}")
print(f" st = {st} of type = {type(st)} in float is {float(st)} with type {type(float(st))}")

x = None
# None2int = int(x) #type-error as float() doesn't accept None type

# int, float , bool and None into string 'str'

# converting bool type to str
var = True
print(f" var = {var} in string type is : {str(var)}")
var = False
print(f" var = {var} in string type is : {str(var)}")

# tackling None to str
var = None
None2str = str(None)
print(f" var = {var} in string is : {None2str}")
# why no error as converting None type to int , float and bool throw errors

