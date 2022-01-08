# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:14:02 2021

@author: User
"""



import datetime as dt
import re

hozir = dt.datetime.now()

bugun= dt.date.today()
# soat = hozir.hour
# sekund = hozir.second
# minut = hozir.minute
# print(hozir)
# print(soat)
# print(bugun)
# print(minut)
# print(sekund)

# bugun = dt.date.today()
# week = dt.date(2022,1,5)
# bday = dt.date(2022,4,7)
# print(f"{bday-bugun}  left")


andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
matn = "Telefon raqamingizni to'liq kiriting: "

while True:
    number = input(matn)
    if re.match(andoza,number):
        print("Raqamingiz qabul qilindi!")
        break
    else:
        print("Xato! Qaytib urinib ko'ring")