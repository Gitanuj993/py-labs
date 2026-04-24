# destructor

class Person :
    def __init__ (self) :
        print(" I am a constructor")

    def i_am(self):
        print(" i am a Person")
    def __del__(self):
        print("Destructor is called ")
        # clean up code



if __name__ == "__main__" :
    p = Person()

    # destructor run when object has done its operation
    print(" Before delete ")
    del p
    print(" After deleted")


    # why destructor is called : To clean the resources # Garbage Collector
    # db operation, loose the connection and clean up code.