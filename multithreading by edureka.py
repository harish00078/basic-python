# a model where multi threads within a process execute independently while sharing the same resources is called multi threading


from threading import *
import time
class demo:
    def num(self):
        for i in range(1,6):
            print("the number is",i)
            time.sleep(1)   # time module sleep function  is used for to break down the thread for a particular time (this is basically use for when we have a multiple threads so that they counld not mixup)
    def double(self):
        for i in range(1,6):
            print("the double of the number is",2*i)
            time.sleep(1) #here the time module sleep is not working well so that i will put sleep function in the thread starting function (in under all class fucntions the sleep fucntion is not working in correct way)
    def square(self):
        for i in range(1,6):
            print("the square of the number is",i*i)
            time.sleep(1)
            
obj=demo()
t1=Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
time.sleep(0.2)   # in under class functions the sleep function is not working good (that's why i put this function in under thread function)

t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print("this is the main thread  ")





    