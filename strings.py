# strings: ordered, immutable, text representation
# my_string = "hello world"

# my_string = 'hello world'# we can only use single quotation when there no there single quotation
# triple quotation is used for multi-line string also documentation inside your code
# my_string = """hello
# world"""
# print(my_string)

# greeting = "hello"
# char = my_sring[4]
# my_sring[4]

# print(char)

# substring = my_sring[1:5]
# substring = my_sring[::2] # the double dot (::) is basically use for  print the double jump from the string 


# print(substring) # if we want sum portion of our string we can use substring (variaable or extension)

# name =  "tom"
# sentence = greeting +  " " + name
# print(sentence)

# for x in greeting:
#     print(x)

# if 'e' in greeting: # we can use if statement for single word or for group words 
#     print("yes")
# else:
#     print("no")
    
    
    
# if 'ell' in greeting: # we can use if statement for single word or for group words 
#     print("yes")
# else:
#     print("no")


# my_string = '     hello world    '
# my_string = my_string.strip() # strip Is use for remove  the gap or white space  between string 

# print(my_string)


# my_string = 'hello world'
# print(my_string.upper()) # upper used for cpatilize all the characters are in string
    
    
# my_string = 'hello world'
# print(my_string.lower()) # lower is used for lower all the characters in the string 

# my_string  = 'hello world'
# print(my_string.startswith('hello')) # if we want to check out were our code is starting with this alphabet like example(h) or we can also check for word like example( hello)
 
# my_string  = 'hello world'
# print(my_string.endswith('world')) # if we want to check out were our code is ending  with this alphabet like example(d) or we can also check for word like example( world)



# my_string  = 'hello world'
# print(my_string.find('o')) # use for to find the string charater number like (o)

# my_string  = 'hello world'
# print(my_string.count('o')) # use to count our character value and how much same character we had of that value

# my_string  = 'hello world'
# print(my_string.replace('world','universe')) # use replace the word like example of (world) In this method if extension is found the old charater or that  i want to replace charater then it will print the older string(it will not change or replace the character)

# my_string = 'how,are,you,doing'
# my_list = my_string.split(",") # in this way can convert our string as a list
# print(my_list)
# new_string = ' '.join(my_list) # if we want to convert our list into string
# print(new_string)

# from timeit import default_timer as timer
# from tracemalloc import start



# my_list = ['a'] * 100000
# print(my_list)
 
# this is bad code\
# start =  timer()
# my_string = ''
# for x in my_list:
#     my_string += x
# stop = timer()
# print(stop-start)

# good code
# start = timer()
# my_string = ''.join(my_list)
# stop = timer()
# print(start-stop)


# two way to format string

# %, .format(), f-strings

# var = 3.1234
# my_string = "the variable is %.2f" %var
# print(my_string)

# var = 3.1234
# var2 = 6
# my_string = "the variable is {:.2f}and{}".format(var,var2)  #((:) we call them a colon)

# print(my_string)


# var = 3.1234
# var2 = 6
# my_string = f"the variable is {var*2}and{var2}" # this is the latest method to format the string

# print(my_string)









