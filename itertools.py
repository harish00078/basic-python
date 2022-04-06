# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators


# itertool = Itertool is a module of Python which is used to creation of iterators which helps us in efficient looping in terms of space as well as time 
# itertool = is basically used for efficent looping 
# from itertools import product

# a = [1,2,]
# b = [3]

# prod = product(a,b,  repeat=2) # we can repeat our loop or iteration using (repeat extension)

# print(list(prod))


# from itertools import permutations 

# meaning of the permutation is arrangement of the elements

# a = [1,2,3]
# perm = permutations(a, 2)


# print(list(perm))


# from itertools import combinations, combinations_with_replacement

# a = [1,2,3,4]

# comb = combinations(a, 2)


# print(list(comb))

# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))
  
  
# from itertools import accumulate  
#  meaning of accumulated :-returning the accumulated sum of the value of each item or running a given function on each item
# import operator
# a = [1,2,3,4]


# acc = accumulate(a,  func=operator.mul)



# print(a)

# print(list(acc))




# from itertools import groupby
# if we want to check something in group that's why we use the groupby 

# a = [1,2,3,4]
# def smaller_than_3(x):
#     return x < 3
  
    


# group_obj = groupby(a, key=smaller_than_3)
 
# for key, value in group_obj:
#     print(key, list(value))

# from itertools import groupby

# anoher example of the groupby

# persons = [{'name': 'tim', 'age':25},{'name':'dan','age':26},
#            {'name':'lisa','age':27}, {'name':'claire','age':28}]


# group_obj = groupby(persons, key=lambda x: x['age'])

# for key, value in group_obj:
#     print(key, list(value))

# from itertools import count, cycle, repeat
# from re import L

# In infinite iterators we had three modules :- count, cycle, repeat 

# for x in count(10):
#     print(x)
#     if x == 15:
#         break

# a = [1,2,3]
# for x in cycle(a):
#     print(x)

# a = [1,2,3]

# for x in repeat(1, 4):  # we can also limit our data in repeat (infinite iterator)
#     print(x)
















