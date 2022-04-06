###
# gil: gil is a global interpreter lock
# a lock that allows only one thread at a time to execute in python 
# 
# 
# needed in cpython because memory management is not thread-safe 
# 
# 
# avoid:
# use multiprocessing 
# use a different, free-threaded python implementation (jython, ironpython)
# use python as a wrapper for third-party libraries(c/c++) ->numpy,scipy
###