# class


# class
class Python_course :
    enroll_count = 0

    def __init__(myself , s_name , ):
        myself.s_name = s_name
        Python_course.enroll_count +=1

    @classmethod # python decorator
    def showCountEnroll(cls):
        print(f" current enrollment of students is : {cls.enroll_count}")


print(f" current enrollment of students is : {Python_course.enroll_count}")
s1 = Python_course("Anamika")
s2 = Python_course("Sarika")
s3 = Python_course("Ambika")
s4 = Python_course("Amba")
s5 = Python_course("Ambalika")
s6 = Python_course("Sheetal")
print(f" current enrollment of students is : {Python_course.enroll_count}")
# class method is accessed by object
s1.showCountEnroll() # calling using class method



