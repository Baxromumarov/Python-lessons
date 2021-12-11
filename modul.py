# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:29:34 2021

@author: User
"""



def avto_info(kompaniya, model, rang, korobka, yil, narxi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rang,
          'korobka':korobka,
          'yil':yil,
          'narx':narxi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar
    haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    
    avtolar=[]
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting: ")
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rang=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narxi=input("Narxi: ")
        
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narxi))
        
        javob=input("Yana avto qo'shasizmi (yes/no)? ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan 
    lug'atni konsolga chiqaruvchi funksiya"""
    
    print(f"{avto_info['rang'].title()} "
          f"{avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()} "
          f"{avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narx']} $")













































