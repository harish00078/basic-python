# Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function
# def mygenerator():
#     yield 3
#     yield 2
#     yield 1
    
# g = mygenerator()
# print(g)
    
# # for i in g:
# #     print(i)
    
# value =  next(g)
# print(value)

    
# value =  next(g)
# print(value)

    
# value =  next(g)
# print(value)

    
# value =  next(g)# if there is no yield statement them the generator will show me (stop iteration)
# print(value)

# print(sum(g)) # this is used to find the sum of the generators

# print(sorted(g)) # in this way we can sort the generator

# def countdown(num):
#     print('starting')
#     while num > 0:   # use loop in generator
#         yield num
#         num -= 1
    
    
# cd = countdown(4)

# value = next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

# import sys


# def firstn(n):
#     nums = []      # use list for generator also is this is simple loop
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1 
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num  # this is generator with loop or list
#         num += 1
        
        
        
        
        
        
         
# print(sys.getsizeof(firstn_generator(100000)))    # generator have a lower binary size
# print(sys.getsizeof(firstn(100000)))       # sys.getsizeof (is use for to find out the size of the generator in binary no) (simple loop have a higher binary value as compare to generator loop value)


# def fibonacci(limit):   # use febonacci number in generator
#     #0 1 1 2 3 5 8 13....
#     a,b = 0,1
#     while a < limit: 
#         yield a 
#         a, b = b, a+b
        
# fib = fibonacci(30)
# for x in fib:
#     print(x)
     
import sys

mygenerator = (x for x in range(100000) if x % 2 == 0)
# for x in mygenerator:
#     print(x)
    
print(sys.getsizeof(mygenerator))  # i can also convert generator in list
    
mylist = [x for x in range(100000) if x % 2 == 0]
print(sys.getsizeof(mylist))
