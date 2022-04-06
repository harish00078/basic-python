# something or some programs are working on system that is called process(basically it means that anything or something is running on our system is known as process)

import multiprocessing
import time


# study the muliprocessing with example
###
# create two processes
# a. first is to calculate square of all numbers
# b. second one is to calculate cube of numbers ###


def calc_square(numbers):
    for n in numbers:
        print('sqaure' + str(n*n))    # here (n) have a values of array list
        
        

    
def calc_cube(numbers):
    for n in numbers:
        print('cube' +str(n*n*n))
        
        
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))  # agrs =  we want to make a multiply function that takes any number of arguments and able to multiply them all ( basically args is used to if i want to add another values that are not  in the functions)
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    


print("done!")
    
    
