# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:48:04 2021

@author: User
"""

kun=input("Bugun qaysi kun: ")
if kun.lower()=='dushanba':
    print("Bugun dars 13:30 da. \n1-Jismoniy tarbiya\n2-MKG\n3-MKG")
elif kun.lower()=='seshanba':
    print("Bugun dars 11:30 da. \n1-Rus tili \nEnglish \nMKG(leksiya)")
elif kun.lower()=='chorshanba':
    print("Bugun dars 13:30 da. \n1-Oliy Matematika (amaliy) \n2-English")
elif kun.lower()=='payshanba':
    print("Bugun dars 11:30 da. \n1-Fizika(laboratoriya) \n2-Oliy matematika(Leksiya) \n3-MKG" )
elif kun.lower()=='juma':
    print("Bugun dars 13:30 da. \n1-Fizika(leksiya.Yavkacheva) \n2-Rus tili")
else:
    print("Bugun dam olish kuni. Vaqtingizni shaxsiy rivojlanishingiz uchun sarflang!")