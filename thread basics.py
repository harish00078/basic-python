###
# thread: an entity with in a process that can be scheduled (also known as "leight weight process)
# a process can spawn multiple threads
# 
# 
# +all threads with in a process share the same memory
# +leight weight
# +starting a thread is faster than starting a process
# +great for i\o-bound tasks
# 
# 
# -threading is limited by gil: only one thread at a time 
# -no effect for cpu-bound tasks 
# -not interruptable/killable
# -care with race conditions###