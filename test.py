#!/usr/bin/env python

from time import sleep
import date 
import datetime
import time
import unicornhat as unicorn

def binary():
  
  decimal = time.strftime("%H%M%S")
  decimal_list = list(decimal)

  for x in xrange(0, 6):
    binary = bin(int(decimal_list[x]))[2:].rjust(4, '0')
    binary_list = list(binary)

    for y in xrange(0, 4):
      if binary_list[y] == '1':
        unicorn.set_pixel(x+1,y,255,255,255)
      else:
        unicorn.set_pixel(x+1,y,0,0,0)

def tree():
    timestamp = datetime.datetime.now().time()
    start = datetime.time(0, 1)
    end = datetime.time(12, 0)
    print(str(timestamp))

    if start <= timestamp <= end:
        print('hello Remi')
        binary()
    if timestamp >= end:
        print('break loop')
        

while True:
    tree()
    sleep(1)
