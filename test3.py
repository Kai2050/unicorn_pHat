#!/usr/bin/env python

import datetime
import time
import unicornhat as unicorn
from random import randint

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.3)

unicorn.clear()

def blank():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 0
  g = 0
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

#random patterns
def random():
  x = randint(0, 7)
  y = randint(0, 3)
  r = randint(1, 255)
  g = randint(1, 255)
  b = randint(1, 255)
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

def green():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 0
  g = 255
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()
  
def red():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 255
  g = 0
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()  
  
def blue():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 0
  g = 0
  b = 255
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

def green_blank():
  for i in range(30):
    green()
    time.sleep(1)
  for i in range(45):
    blank()
    time.sleep(0.5)  

def red_blank():
  for i in range(30):
    red()
    time.sleep(1)
  for i in range(45):
    blank()
    time.sleep(0.5)

def random_blank():
  for i in range(30):
    random()
    time.sleep(1)
  for i in range(45):
    blank()
    time.sleep(0.5)

def binary():
  unicorn.clear()
  decimal = time.strftime("%H%M%S")
  decimal_list = list(decimal)

  for x in xrange(0, 6):
    binary = bin(int(decimal_list[x]))[2:].rjust(4, '0')
    binary_list = list(binary)

    for y in xrange(0, 4):
      if binary_list[y] == '1':
        unicorn.set_pixel(x+1,y,0,0,255)
      else:
        unicorn.set_pixel(x+1,y,0,0,0)

  unicorn.show()
  time.sleep(1)



print('binary nightlight started')
    
def schedule():
    timestamp = datetime.datetime.now().time()
    #print(str(timestamp))

    red_start = datetime.time(19, 00)
    red_end = datetime.time(19, 29)
    binary_start = datetime.time(19, 30)
    binary_end = datetime.time(23, 59)
    binary_start2 = datetime.time(0, 0)
    binary_end2 = datetime.time(6, 0)
    random_start = datetime.time(6, 0)
    random_end = datetime.time(7, 30)
    clear_start = datetime.time(7, 30)    
    clear_end = datetime.time(19, 30)
    
    
    if red_start <= timestamp <= red_end:
        red_blank()
    if binary_start <= timestamp <= binary_end:
        #print('binary')
        binary()
    if binary_start2 <= timestamp <= binary_end2:
        #print('binary')
        binary()
    if random_start <= timestamp <= random_end:
        #print('green')
        random_blank()
    if clear_start <= timestamp <= clear_end:
        #print('clear')
        unicorn.clear()
        unicorn.show()
    
while True:
    schedule()
#    time.sleep(1)
