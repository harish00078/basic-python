# lambda arguments:expression
# this is basically used for giving a function to variable 



# x = lambda x: x +10
# print(x(5))


# compare lambda with functions 

# def add10_func(x):
#     return x+10



# lambda function for multiple variables:

# mult = lambda x,y: x*y
# print(mult(2,7 ))




# put the lambda function in list

# points2d = [(1,2),(15,1),(5,-1),(10,4)]


# def sort_by_y(x):
#     return x[1]
    

# points2d_sorted = sorted(points2d,key=lambda x: x[0] + x[1])

# print(points2d)
# print(points2d_sorted)

# map(func, seq) this is use for if we want to multiply something 
# a = [1,2,3,4,5]
# b = map(lambda x: x*2,a)
# print(list(b))


# c =[x*2 for x in a]
# print(c)


# filter(func,seq) this is use for if we want to fillter out something using lambda function
# a = [1,2,3,4,5,6]
# b = filter(lambda x:x%2==0, a)
# print(list(b))



# fillter out something using list comparihension filter function

# c = [x for x in a if x%2==0]
# print(c)

# reduce(func,seq)
# reduce function is used for to find out the hole sum of the variable data
  
# from functools import reduce

# a = [1,2,3,4]

# product_a = reduce(lambda x,y: x*y,  a)
# print(product_a)

