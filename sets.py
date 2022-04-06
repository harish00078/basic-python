# sets: unordered , mutable , no duplicates
# myset = {1,2,3,1,2}  
# print(myset)

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)

# print(myset.pop())

# print(myset)

# for x in myset:
#     print(x)

# if 1 in myset:
#     print("yes")


# (union(u) and intersection(^))
# from re import I


# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}

# u = odds.union(evens)
# # print(u)



# i = odds.intersection(primes)
# print(i)

# i = evens.intersection(primes)
# print(i)


# seta = {1,2,3,4,5,6}
# setb = {1,2,3}

# diff = seta.difference(setb)
# print(diff)

# diff = setb.difference(seta)
# print(diff)

# diff = setb.symmetric_difference(seta)
# print(diff)

# seta.update(setb)
# print(seta)

# seta.intersection_update(setb)
# print(seta)

# seta.difference_update(setb)
# print(seta)

# seta.symmetric_difference_update(setb)
# print(seta)

# seta = {1,2,3,4,5,6}
# setb = {1,2,3}
# setc = {7,8}

# print(seta.issubset(setb))
# print(setb.issubset(seta))

# print(seta.issuperset(setb))
# print(setb.issuperset(seta))

# print(seta.isdisjoint(setb))
# print(setb.isdisjoint(seta))

# print(seta.isdisjoint(setc))


# seta = {1,2,3,4,5,6}

# setb = seta.copy() # use for copy a one in other if we donot use this our variables will link together
# setb = set(seta)                 # use for copy a one in other if we donot use this our variables will link together
 

# setb.add(7)
# print(setb)
# print(seta)

# a = frozenset([1,2,3,4])

# a.add(2)
# a.remove(2)


# print(a)