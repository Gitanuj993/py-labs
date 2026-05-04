
from threading import Thread

class Mythread(Thread) :

    def run(self):
        print("Thread is running ")

t1 = Mythread()
t1.run()
# t1.getName()
t1.start()
t1.stop()
# thread , start , wait , running ,sleep