# process: an insatance of a program (e.g a python interpreter)
###
# +takes advantage of multiple cpus and cores
# +separate memory space --> memory is not shared between processes
# +great for cpu-bound processing
# +new process is stated independently from other processes
# +processes are interruptable/killable
# +one gil for each process -> avoids gil limitation

# -heavyweight
# -starting a process is slower than starting a thread
#--more memory
# -IPC (inter-process communication) is more complicated###




