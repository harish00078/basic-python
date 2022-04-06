# # import random

# # random is basically use for create a random numbers or floats
# a = random.random()
# print(a)

# # uniform is used to ristrict the data or we can gave him a length from start to end

# a = random.uniform(1, 10)
# print(a)

# # randint is use if we want to use the interger value
# a = random.randint(1, 10)
# print(a)

# # we can also use the randrange for integer or if want the perfectly integer range between the start to end point
# a = random.randrange(1, 10)
# print(a)
# # this is use for statistics 
# a = random.normalvariate(0,1) # here (0) is mean or (1) is standard deviation
# print(a)

# mylist = list("ABCDEFGH")
# a = random.choice(mylist) # this is use for to choose a random string from our list
# print(a)

# mylist = list("ABCDEFGH")
# a = random.sample(mylist, 3) # this is use for if we want to pick a unique string or not repeated string
# print(a)



# mylist = list("ABCDEFGH")
# a = random.choices(mylist, k=3) # this is use for if we want to pick a elements in multiple times 
# print(a)

# mylist = list("ABCDEFGH")
# random.shuffle(mylist) # this is use for if we want to shuffle our elements 
# print(mylist)

# # The seed() method is used to initialize the random number generator
# # The random number generator needs a number to start with (a seed value), to be able to generate a random number.

# random .seed(1) # we can run seed method as many time i want
# print(random.random())
# print(random.randint(1, 10))

# random .seed(2) # we can also run seed method with different values
# print(random.random())
# print(random.randint(1, 10))


# random .seed(1) # we can run seed method as many time i want
# print(random.random())
# print(random.randint(1, 10))

# random .seed(2) # we can also run seed method with different values
# print(random.random())
# print(random.randint(1, 10))

# import secrets  # secrets module is used for to generate a secure random number.
# # because the simple random  module is not secure.
# # secrets module only have a three functions

# a = secrets.randbelow(10) #  this is use for produce a secure random interger or other data types

# print(a)



# a = secrets.randbits(4) # in this randbits method  we have a four differnet random binary values or highest possible random four number value'

# print(a)

# mylist = list("ABCDEFGH") # this will pick a secretly random character 

# a = secrets.choice(mylist)
# print(a)
import numpy as np

arr = np.array([[1,2,3,],[4,5,6],[7,8,9]]) # in this way we can create a many dimensional array 
print(arr)
np.random.shuffle(arr) # we can also shuffle our array using shuffle method
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))


