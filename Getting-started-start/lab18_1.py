"""
Welcome AT
aim : Arithematic operators and operations

there is total no of arithematic operators :
1. +
2. -
3. *
4. /
5. //
6. **
7. %

"""
print("------------------------------------------")
a = 10
b = 3
sum = a + b
print(f" a + b is : {sum} thus '+' is used for addition ")
print("---------------      --------------")
mul = a * b
print(f" a * b is : {mul} thus '*' is used for Multiplication ")
div_float = a/b
print(f" a / b is : {div_float} thus '/' is used for division , result in float or decimal")
print(f" type of float division is : {type(div_float)}")
print("---------------      --------------")
div_floor = a // b
print(f" a // b is : {div_floor} thus '//' is used for floor division , result in int type")
print(f" type of floor division is : {type(div_floor)} floor value if 3.3 then it wll become less")
print("---------------      --------------")

sub = a - b
print(f" a - b is : {sub} thus '-' is used for Subtraction , result type depends on operands")

print("---------------      --------------")
remainder = a % b
print(f" a % b is : {remainder} thus '%' is used for remainder , result in int type")
# there is edge cases in remainder
print("---------------      --------------")

a = 12
b = 2
pow = a ** b
print(f" a raise to power b is : {pow}")
print("---------------      --------------")
