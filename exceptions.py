# exception ( this is used for to gave the statement to the code or if we want that code tell us that this is not right code or right function like in (try,catch, if statements))
# from cgi import test
# from email import message
# from logging import exception
# from tkinter import E


# x = -5
# if x < 0:
#     raise exception('x should be positive')


# x= -5
# assert (x>=0), 'x is not positive'

# if i want to handle exception or error in our code

# try:
#     a = 5 / 0
# except exception as e:
#     print(e)

# try:
#     a = 5 / 1 # this is zerodivisionerror
#     b = a + "4" # this is typeerror beacuse (a) had a float value or (4) is a string value, 
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up')

# class valuetoohigherror(exception):
#     pass

# class valuetoosmallerror(exception):
#     def _init_(self, massage, value): #(def_init_) this is not a simple function this is a intialize fuunction ( we create that function under the class)
#         self.message = message
#         self.value = value
        
# def test_value(x): # In this way we create a function
#     if x >100:
#         raise valuetoohigherror('value is too high')
#     if x < 5:
#         raise valuetoosmallerror('value is to small',x)
        
# test_value(200)

# try:
#     test_value()
# except valuetoohigherror as e:
#     print(e)
# except valuetoosmallerror as e:
#     print(e.message, e.value)



