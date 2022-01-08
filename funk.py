# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:04:56 2021

@author: User
"""



def get_sonlar(son1,son2,son3):
    if son1>son2 and son1>son3:
        return son1
    if son2>son1 and son2>son3:
        return son2
    if son3>son1 and son3>son2:
        return son3


def get_matn(matn):
    return matn.title()    



def get_juft(numbers):
    sonlar=[]
    for number in numbers:
        if number%2==0:
            sonlar.append(number)
        else:
            pass
    return sonlar



    