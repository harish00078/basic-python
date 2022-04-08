# from threading import Thread



# def square_numbers():
#     for i in range(100):
#         i*i
        
        
# if __name__ == "__main__":
#     threads = []
#     num_threads = 10   # number of thread is ten
    
#     # create threads 
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
        
#     # start thread
#     for thread in threads:
#         thread.start()
        
        
#     # join threads: wait for them to complete
#     for thread in threads:
#         thread.join()
        
        
#     print('end main')

from threading import Thread, Lock
import time


database_value = 0

def increase(lock):
    global database_value
    # lock is use for having a better result in thread ( when you start the lock you have to end it also otherwise this will gave error to you)
    # if i do not want to gave a start or release function to the lock we can gave a lock function to our function were we use the lock
    with lock: # in this we can also create the lock to the thread 
        
    # lock.acquire()
        local_copy = database_value
     
    # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
        # lock.release()
    

if __name__ =="__main__":
    
    lock = Lock()
    
    print('start value',database_value)
    
    
    thread1 = Thread(target=increase,args=(lock,))
    thread2 = Thread(target=increase,args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value',database_value)
    
    print('end main')
    
    
    
    
    
    
    