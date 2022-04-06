
# # A decorator is a function that takes another function as an argument and extends its behavior without changing the original function explicitly(combine fuctions without changing the current function)
# # we have two types of decorators
# # 1 = function decorators
# # 2 = class decorators


# # @mydecorator
# # def dosomething():
# #     pass

# import functools    

# def my_decorator(func):
#     @functools.wraps(func)


#     def wrapper(*args, **kwargs):#( args = arguments, kwargs = keyword argument)
#         # do...
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

        
  
# # print_name = start_end_decorator(print_name) in this way we can create a decorator (or in this way the decorator work)
# # @start_end_decorator  
# @my_decorator
# def add5(x):
#     return x + 5



# # def print_name():
# #     print('alex')

# # def add5(x):
# #     return x + 5
    

# # # print_name = start_end_decorator(print_name)


# # # print_name()


# # print(help(add5))
# # print(add5.__name__)
    
# import functools
# from unittest import result

# def repeat(num_times):
#     def decorator_repeat(func):

#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):    # this is loop decorator beacuse we use here forloop
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
        

    

# @repeat(num_times=5)
# def greet(name):
#     print(f'hello {name}')
    
    
# greet("harish")
  
# nested decorator
# from distutils.log import debug
# import functools
# def start_end_decorator_4(func):

#     @functools.wraps(func)
    

#     def wrapper(*args, **kwargs):#( args = arguments, kwargs = keyword argument)
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper



# # a decorator function that prints debug information about the wrapped function
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper


# @debug
# @start_end_decorator_4
# def say_hello(name):
#     greeting = f'hello {name}'
#     print(greeting)
#     return greeting
    
    
    
# say_hello("harish")  

# class countcalls:
    
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0
        
        
#     def __call__(self, *args, **kwargs):
#         # print('hi there')
#         self.num_calls += 1
#         print(f'this is excuted {self.num_calls}times')
#         return self.func(*args, **kwargs)

        

        
        
        
# # cc = countcalls(None)
# # cc()

        
# # this decorator is use for how much time i will executed the program
# @countcalls
# def say_hello():
#     print('hello')
    
    
# say_hello
    
import functools
# in this way we can count much time our code will we executed or create a counting execution decoratorf
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print("Hello!")
    
say_hello(5)
say_hello(5)
  
