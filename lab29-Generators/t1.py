
def gen_student_id(n) :
    i = 1
    while True :
        yield i
        i +=1

my_gen = gen_student_id(100)
print(my_gen)
print(next(my_gen))
print(next(my_gen))

for i in my_gen :
    print(i)