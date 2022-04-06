# points related to thread.
# 1 when we perform a big program in that program we had a small programs or function that is know as thread
# 2 small , small processes is know as thraed
# 3 basically in under processes we had a small processes that is call thread
# 4 thread is very usefull in big programs executions we can execute big programs very fast using threads
# 5 creating  thread we can use full power of our system cores or cpu
# 6 main point is that in thread use target method that will basically target a particular fucntion or value in program that we want to execute as a thread 



#  use python debugger to execute the thread or process program because sometime i had error in terminal (or try in jupyter notebook)
# this is the first way to create the thread
# example of how thread works
# from threading import Thread
# def  show():
#     print("this is a child thread")
    
# t = Thread(target=show()) # in this way we can create the thread 
# t.start()  # in this way we can start the thread

# print("this is parent thread")



# this is the second way to create the thread
# from threading import Thread
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("\nthis is a child class")
            
# t = MyThread()
# t.start()
# for i in range(5):
#     print("\nthis is the main thread") 

# this is the third way to create the thread
from threading import Thread
class demo:
    def show(self):
        for i in range(5):
            print("this is the child thread")
            
obj=demo()
t=Thread(target=obj.show())
t.start()
for i in range(5):
    print("this is the parent thread")
        
