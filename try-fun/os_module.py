"""
Welcome AT
module : 2
aim : to familiar with built in os module
more specifically we will explore what things we can do with os module
"""
import os

# provide a path for your folder 
#for pc :	path = 'folder name' as you already open vs code or pycharm in a folder
# for android phones : '/storage/emulated/0/py/'
path = '/storage/emulated/0/py/'

#lets print our working directory which we can do using terminal commands
print(os.system('pwd')) # why 0 is written in output after printing working directory

#lets check out directories
print(os.system('ls'))

#lets print some more commands
print(os.system(" echo 'Welcome AT ' "))
#lets create a new file using touch command 
print(os.system('touch file.txt'))
print(os.system('ls'))
#lets see the data in file.txt folder
print(os.system('cat file.txt')) # initially no data in the list thus w put data into it
#print(os.system( " echo 'Welcome AT ' >> file.txt"))
#print(os.system('cat file.txt'))  # data will be inserted on the file if we run above command
#














