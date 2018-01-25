#!/usr/bin/env python
#nightlight with binary

import unicornhat as unicorn
from random import randint
from time import sleep
import datetime
import time

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.3)

#random patterns
def random():
  x = randint(0, 7)
  y = randint(0, 3)
  r = randint(1, 255)
  g = randint(1, 255)
  b = randint(1, 255)
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

#white
def white():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 200
  g = 200
  b = 200
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

#red
def red():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 255
  g = 0
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

#green
def green():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 0
  g = 255
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

#blank
def blank():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 0
  g = 0
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

#night pattern: random colors then random blanking
def night():
  for i in range(30):
    random()
    sleep(1)
  for i in range(45):
    blank()
    sleep(0.5)

#morning pattern: white then random blanking
def morning():
  for i in range(30):
    white()
    sleep(1)
  for i in range(45):
    blank()
    sleep(0.5)

#green then blanking
def warm_up():
  for i in range(30):
    green()
    sleep(1)
  for i in range(45):
    blank()
    sleep(0.5)

def binary():
    while 1:
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

      unicorn.show()
      time.sleep(1)

#scheduler of what happens at what time
def schedule():
  currenttime = time.localtime()
  currenthour = currenttime.tm_hour
  currentmin = currenttime.tm_min
  localtime = time.asctime( time.localtime(time.time()) )

  timestamp = datetime.datetime.now().time()

  start = datetime.time(0, 1)
  end = datetime.time(6, 0)
  if(start <= timestamp <= end):
    print("night " + str(timestamp))
    binary()

  start = datetime.time(6, 1)
  end = datetime.time(8, 0)
  if(start <= timestamp <= end):
    print("Green " + str(timestamp))
    warm_up()

  start = datetime.time(8, 1)
  end = datetime.time(18, 14)
  if(start <= timestamp <= end):
    unicorn.clear()
    unicorn.show()

  start = datetime.time(18, 15)
  end = datetime.time(19, 29)
  if(start <= timestamp <= end):
    print("Binary " + str(timestamp))
    binary()

  start = datetime.time(19, 30)
  end = datetime.time(23, 59)
  if(start <= timestamp <= end):
    print("night " + str(timestamp))
    binary()

while True:
  schedule()
  time.sleep(0.5)
