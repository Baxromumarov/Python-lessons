# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:54:45 2022

@author: User
"""



from pywebio.output import put_text, put_buttons
import pywebio
from time import sleep
import random

def son_top(x=10):
    pywebio.output.clear(scope=-1)
    global quyi, yuqori, taxmin
    quyi = 1
    yuqori = x
    
    put_text(f"1 dan {x} gacha son o'ylang. \n Sizga 3 soniya vaqt!")
    
    for i in [3,2,1,"Boshladik!"]:
        put_text(str(i))
        sleep(1)
        
    def guess():
        pywebio.output.clear(scope=-1)
        global taxmin 
        taxmin = random.randint(quyi,yuqori)
        put_text(f"Siz {taxmin} sonini o'yladingiz!")
        put_buttons(['Kattaroq',"To'g'ri","Kichikroq"],
                    onclick=[katta,bingo,kichik])
        pywebio.session.hold()
        
    def kichik():
        global yuqori
        yuqori = taxmin-1
        guess()
        
    def katta():
        global quyi
        quyi = taxmin+1
        guess()
    
    def bingo():
        put_text("Men yutdim!")
    
    guess()
        