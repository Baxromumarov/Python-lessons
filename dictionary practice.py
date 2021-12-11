# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:18:09 2021

@author: User
"""

otam={'ism':'qahramon','t_yil':1976,'kasb':'haydovchi','millat':'tojik'}
onam={'ism':'lutfiya','t_yil':1976,'kasb':'o\'qituvchi','millat':'tojik'}
akam={'ism':'rustam','t_yil':2001,'kasb':'talaba','millat':'o\'zbek'}
print(f"{otam['ism'].title()},{otam['t_yil']}-yilda tug\'ilgan,kasbi-{otam['kasb']}")
print(f"{onam['ism'].title()},{onam['t_yil']}-yilda tug\'ilgan,kabi-{onam['kasb']}")
print(f"{akam['ism'].title()},{akam['t_yil']}-yilda tug\'ilgan,kasbi-{akam['kasb']}")

taomlar={
      'akam':'osh',
      'otam':'kabob',
      'o\'zim':'shashlik',
      'onam':'sho\'rva',
      'buvim':'norin'
       }
taom=taomlar['akam']
print('Akam ',taomlar['akam'],'ni yaxshi ko\'radi')
print('Oyim',taomlar['onam'],'ni yaxshi ko\'radi')
print('otam',taomlar['otam'],'ni yaxshi ko\'radi')
print(f"{taom.title()}")







izohli_lugat={
    'integer':'Butun sonlar qiymatini qabul qiladi',
    'float':'o\'nli kasr qiymatli sonlarni qabul qiladi',
    'string':'matn qiymatlarni qabul qiladi',
    'if':'agar deb tarjima qilinadi.Shart operatori',
    'else':'aks holda dev tarjima qilinadi.If ning davomi',
    'elif':'agar,aks holda deb tarjima qilinadi.shart operatori',
    'print()':'chiqarish operatori',
    'input()':'foydalanuvhi bilan muloqot qilish operatori',
    '.lower()':'matndagi barcha harflarni kichik qiladi',
    '.upper()':'matndagi barcha harflarni katta qiladi'
    }
        # 1-usul
qiymat=input('Biror qiymat kiriting: ').lower()
qiymat=izohli_lugat.get(qiymat,'Bunday so\'z mavjud emas ')
print(qiymat)


        # 2-usul
        
        
qiymat= input("Kalit so'z kiriting:").lower()
mano =izohli_lugat.get(qiymat)
if mano==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{qiymat.title()}--{mano} ")
    
    
         # 3-usul
         
         
qiymat= input("Kalit so'z kiriting:").lower()
mano =izohli_lugat.get(qiymat)
if not mano in izohli_lugat:
    print("Bunday so'z mavjud emas")
else:
    print(f"{qiymat.title()}--{mano} ")



























    
