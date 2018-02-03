from time import sleep
import datetime
import time

def tree():
    while True:
        timestamp = datetime.datetime.now().time()
        print('hello world')
        sleep(1)    
        start = datetime.time(0, 1)
        end = datetime.time(9, 0)
        if(start <= timestamp <= end):
            print("binary " + str(timestamp))
            pass

    print('put out of loop')

while True:
    tree()
