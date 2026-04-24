# destructor

class Person :
    def __init__ (self) :
        print(" I am a constructor")

    def i_am(self):
        print(" i am a Person")
    def __del__(self):
        print("i am a Destructor")



if __name__ == "__main__" :
    p = Person()
    # p.i_am()
    # destructor run when object has done its operation