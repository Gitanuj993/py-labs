
# class student

class Students :
    sid = 101
    name = "AT"

    def show(self):
        print(self.sid,self.name)


if  __name__ == '__main__' :
    # object declaration
    s1 = Students()
    # s1 is a reference variable 8 bytes
    # Access show method using dot operator
    s1.show()
    # show() , show is not defined
    print(f" Type of s1 is : {type(s1)}")
    
# <class '__main__.Students'>
# __main__ is a module , 2k class to 1lack classes