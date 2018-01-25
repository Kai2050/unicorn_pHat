#!/usr/bin/env python

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.5)
unicorn.rotation(180)

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
