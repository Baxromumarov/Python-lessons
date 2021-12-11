# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:21:12 2021

@author: User
"""

import time
import random

turns=5
print("Salom, men bilan so'z o'yinini o'ynasizmi "+ str(turns)+" imkoniyat")

print("")

time.sleep(0.5)

wordlist=['python','salom','maktab','tarix']
word=random.choice(wordlist)

guesses=''

while turns>0:
    wrong=0
    
    for char in word:
        if char in guesses:
            print (char),
        else:
            print("-"),
            wrong+=1
            
    print("\n")
    
    if wrong==0:
        print("Siz yutdingiz: ")
        
        break
    print
    
    guess=""
    if len(guess)<1:
        guess=input("To'g'ri harfni kiritdingiz': ")[0]
    
    guesses+=guess
    
    if guess not in word:
        turns-=1
        
        print("Xato")
        
        print("Sizda ",+turns,' imkoniyat qoldi')
        
        if turns==0:
            print("Siz yutqazdingiz!")