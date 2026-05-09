# f-string or formatted string :     industry prefer it .

name = "Anuj"
age = 19
p_lang = "python"
PI = 3.1415
print(f" your name is : {name}")
print(f" Your age is {age} and you are currently working on {p_lang} ")

#  alignments 
print(f" {name: <20} left alignment ")
print(f" {name: >20} right alignment ")
print(f" {name: ^20} center alignment ")
print(f" {name:*^50} filling * ")

# floating point precisions

print(f" PI .2f is : {PI: .2f} ")
print(f" PI .6f is : {PI: .6f} ") # zero is added at the last
PI = 22/7
print(PI)

# precision at certain digits , say
precision = 3
print(" certain precision is : ",precision,"decimal places")
print(f" PI upto precision is :  {PI: .{precision}f} ")

