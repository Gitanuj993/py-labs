# class
class Python_course :
    enroll_count = 0

    def __init__(myself , s_name , ):
        myself.s_name = s_name
        myself.enroll_count += 1 # changing the value
        print(myself.enroll_count)
        print(Python_course.enroll_count) # myself unable to change the class variable.
        print(myself.enroll_count)




s = Python_course("Ok")