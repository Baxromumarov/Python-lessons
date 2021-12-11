# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:56:55 2021

@author: User
"""

import turtle

t=turtle.Turtle()

t.color('Brown')

for i in range(4):
    t.forward(50)
    t.left(90)


t.penup()
t.left(90)
t.forward(50)
t.pendown()

t.right(30)
t.forward(50)
t.right(120)
t.forward(50)
