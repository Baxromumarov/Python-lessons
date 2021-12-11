# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:06:06 2021

@author: User
"""

python_izohli_lugat={
    'integer':'butun qiymat qabul qiladi',
    'float':'o\'nli kasr qiymat qabul qiladi',
    'string':'matn qiymatlarini qabul qiladi',
    'print':'chiqarish operatori',
    'boolean':'mantiqiy qiymat qabul qiladi',
    'if':'agar deb tarjima qilinadi. Shart operatori',
    'else':'aks holda deb tarjima qilinadi.',
    'input':'kiritish operatori',
    'for':'sikl',
    'tuple':'o\'zgamas ro\'yxat'
    }
# for key, value in sorted(python_izohli_lugat.items()):
#     print(f"{key.title()} - {value}")

davlat_poytaxt={
    "o\'zbekiston":"toshkent",
    "rossiya":"moskva",
    'aqsh':'vashington',
    'xitoy':'pekin',
    'tojiiston':'dushanbe',
    'italiya':'rim'
    }
# print('Dunyo davlatlari:')
# for key in sorted(davlat_poytaxt.keys()):
#     if key=='aqsh':
#         print(key.upper())
#     else:
#         print(f"{key.title()}")
# print('\n')
# print('Dunyo davlatlarining poytaxtlari:')
# for value in sorted(davlat_poytaxt.values()):
#     print(value.title())


# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlat_poytaxt.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.title()}ning poytaxti {capital.title()} shahri")


menyu={
        'lavash':20_000,
        'shashlik':45_000,
        'qozonkabob':35_000,
        'osh':18_000,
        "lag'mon":25_000,
        'norin':8_000,
        'somsa':5_000,
        'kfc':30_000,
        'gamburger':12_000,
        'kartoshka fri': 9_000
          }


print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menyu:
        print(f"{buyurtma.title()} {menyu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")



















