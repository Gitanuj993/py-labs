# File handling , working with files

# open is a global function or built-in function which return a string object
f = open("test1.txt","r",encoding = 'utf-8')
# f.write("Welcome AT")
data = f.read() # .read() is a global function which reads the data from the file and return a strings
f.close()

print(data)
print(f" Type of file f : {type(f)}")
#