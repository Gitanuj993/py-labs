"""
Welcome AT
module : os : part : 2
aim :  working with files
"""
import os 
print(os.system('pwd'))
path = 'os_module2.py'

#check for file whethe file exists or not 
print(f" path exist : { os.path.exists(path) }") 
 # if exist then ' True wil be written else "False'

#    lets'work with files 
#lets create a dirctory on our working directory
os.mkdir("new directory") # comment out it if program is runned second time
#lets check for the new directory
print(os.system('ls'))
# when you run this program second time do not forget to comment out line no : 16
#lets' delete the created directory
os.rmdir("new directory")
print(os.system('ls'))

#lets rename a directory , first create one then rename it , then deletes 
os.mkdir("file1")
print(os.system('ls')) # you will see file exists  or we can run
print(f"  file1 exist :	  {os.path.exists('file1')}")

os.rename('file1','file2')
print(" file1 renamed to file2")
print(f"  file1 exist :	  {os.path.exists('file1')}")
print(f"  file2 exist :	  {os.path.exists('file2')}")

os.rmdir('file2')

#finally lets list out number of directories and files present in a folder or path 
print(os.listdir()) # show current folder content

