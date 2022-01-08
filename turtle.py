# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:10:46 2021

@author: User
"""

from turtle import *


color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()