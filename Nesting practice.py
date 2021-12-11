# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:53:49 2021

@author: User
"""

# ma_shaxs0={
#     'ism':'musk',
#     'familiya':'elon',
#     't_joy':'afrika',
#     'kompaniya':'tesla'
#     }
# ma_shaxs1={
#     'ism':'bill',
#     'familiya':'gates',
#     't_joy':'amerika',
#     'kompaniya':'microsoft'
#     }
# ma_shaxs2={
#     'ism':'steve',
#     'familiya':'jobs',
#     't_joy':'amerika',
#     'kompaniya':'apple'
#     }
# ma_shaxs3={
#     'ism':'jack',
#     'familiya':'ma',
#     't_joy':'xitoy',
#     'kompaniya':'aliexpress'
#     }
# ma_shaxslar=[ma_shaxs0,ma_shaxs1,ma_shaxs2,ma_shaxs3]
# print('Internet olamidagi mashhur shaxslar:')
# for ma_shaxs in ma_shaxslar:
#     print(f"{ma_shaxs['ism'].title()} {ma_shaxs['familiya'].title()}. "
#     f"{ma_shaxs['t_joy'].title()}da tug'ilgan. "
#     f"Asos solgan kompaniyasi--{ma_shaxs['kompaniya'].upper()}")

# ma_shaxs0['y_kitob']='musk'
# ma_shaxs1['y_kitob']='bill'
# ma_shaxs2['y_kitob']='steve'
# ma_shaxs3['y_kitob']='jack'

# for shaxs in ma_shaxslar:
#     print(f"{shaxs['ism'].title()}-{shaxs['y_kitob'].upper()} kitobining muallifi hamdir")


# kinolar={
#     'shavkat':['maktab','terminator','avengers'],
#     'sardor':['oblivion','cobra kai','forsaj'],
#     'nasullo':['titanic','terra nova','mortal combat']
#     }
# for ism,film in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in film:
#         print(kino)




davlatlar={
    'o\'zbekiston':{
        'poytaxt':'toshkent',
        'pul_birligi':'so\'m',
        'millat':'o\'zbek'
        },
    'rossiya':{
        'poytaxt':'moskva',
        'pul_birligi':'rubl',
        'millat':'rus'
        },
    'xitoy':{
        'poytaxt':'pekin',
        'pul_birligi':'von',
        'millat':'mandarin'
        },
    'angliya':{
        'poytaxt':'london',
        'pul_birligi':'funt sterling',
        'millat':'ingliz' 
        }
    }
# for davlat,malumot in davlatlar.items():
    # print(f"\n{davlat.upper()} haqida ma'lumotlar:")
    # print(f"Poytaxti-{malumot['poytaxt'].title()}")
    # print(f"Pul birligi-{malumot['pul_birligi']}")
    # print(f"Millati-{malumot['millat']}")

davlat=input('Qaysi davlat haqida ma\'lumot olmoqchisiz? ').lower()
if davlat in davlatlar:
    malumot=davlatlar[davlat]
    print(f"\n{davlat.upper()} haqida ma'lumotlar:")
    print(f"Poytaxti-{malumot['poytaxt'].title()}")
    print(f"Pul birligi-{malumot['pul_birligi']}")
    print(f"Millati-{malumot['millat']}")
else:
    ('Kechirasiz, bizda bu davlat haqida ma\'lumot yo\'q')
    

