from time import sleep
import datetime
import time

timestamp = datetime.datetime.now().time()
start = datetime.time(0, 1)
end = datetime.time(6, 0)

if(start <= timestamp <= end):
print("binary " + str(timestamp))
