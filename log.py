import logging

log_filename = 'latestlog.txt'

logging.basicConfig(filename=log_filename, level=logging.DEBUG,)

logging.info("Hi from log file")









# import time

#data = ""


#def log(kind, message):
#    global data#
#
#    localtime = time.asctime(time.localtime(time.time()))

#    data += "[" + localtime + "]" + " " + "[" + kind + "]" + " " + message
#    return data