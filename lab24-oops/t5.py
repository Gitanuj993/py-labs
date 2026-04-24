# class variable
#
class Student : # it is good practice to start class name with a capital letter
    fee = 50000
    clg = "SDITS"

    def __init__(self,name,id): # parameters of method # local variables.
        self.s_name = name # 'name' is a local variable. # s_name is a instance variable
        self.id = id # left side variables are instance variable.

    def show(self):
        print(f" Student's id : {self.id} and name : {self.s_name}")
        print(f" Student's college name : {self.clg} has to submit : {self.fee} fee on time")

# s1 = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'id'

std_name = str(input("Enter student's name : "))
std_id = int(input(" Enter student's id : "))
# std_name = "AT"
# std_id = 123
s1 = Student(std_name,std_id)
s1.show()
Student.fee = 20000
s1.show() # Type of s1.show() is : <class 'NoneType'>

print(f" Type of s1.show() is : {type(s1.show())}")

# local variables :  variables which are accessed within a scope ,
# local variables defined in the functions
# local variables not accessible outside class