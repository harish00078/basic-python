# Logging is used to tracking events that occur when the software runs. This module is widely used by the developers when they work to logging.
# this is used to tell me why my software will crash ( this will show me through logggings ) 
# Logging is important for software developing, debugging, and running. If you don’t have any logging record and your program crashes, there are very few chances that you detect the cause of the problem. And if you detect the cause, it will consume a lot of time.that why we use the logging module to easily find out the problem in the software
# import logging
# logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%y %H:%M:%S') 
# logging.debug('this is a debug message')
# logging.info('this is an info message')       
# logging.warning("this a  warning message")        
# logging.error('this is an error message')        
# logging.critical('this is an critical message')        
# import main # import my other logging or created my own logging 

# import logging
# logger = logging.getLogger(__name__)


# # create a handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # level and format the handler

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning ')
# logger.error('this is error')
# this is working on jupyter notebook 


# import logging
# import traceback
# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e)  # working on jupyter notebook

# import logging
# from logging.handlers import RotatingFileHandler


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2kb, and keep backup logs app.log.1, app.log.2, etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('hello, world!')  # working on jupyter notebook or vscode jupyter notebook (having a error working on simple vscode)
