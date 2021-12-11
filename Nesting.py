# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:34:09 2021

@author: User
"""

# car0={
#       'model':'lacetti', 'rang':'oq',
#       'yil':2018,'narx':13_000,
#       'km':50_000,'korobka':'avtomat'
#       }
# car1={
#       'model':'Nexia 3','rang':'qora',
#       'yil':2015,'narx':9_000,
#       'km':89_000,'korobka':'mexanika'
#       }
# car2={
#       'model':'gentra','rang':'qizil',
#       'yil':2019,'narx':15_000,
#       'km':20_000,'korobka':'mexanika'
#       }

# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narx']}$")

# print(f"{cars[1]['model'].title(),} "
#       f"{cars[0]['rang']}")


# print(f"{cars[0]['rang'].title()} "
#       f"{cars[1]['model'].title()}")

# cobalts=[]
# for n in range(10):
#     new_car={
#              'model':'cobalt',
#              'rang':None,
#              'yil':2021,
#              'narx':None,
#              'km':0,
#              'korobka':'avto'
#              }
#     cobalts.append(new_car) #lug'atni ro'yxatga qo'shamiz

# for cobalt in cobalts[:3]:
#     cobalt['rang']='oq'

# for cobalt in cobalts[3:6]:
#     cobalt['rang']='qora'

# for cobalt in cobalts[6:]:
#     cobalt['rang']='qora'
#     cobalt['korobka']='mexanik'

# for cobalt in cobalts:
#     if cobalt['korobka']=='avto':
#         cobalt['narx']==10_000
#     else:
#         cobalt['narx']==9_000

# for cobalt in cobalts:
#     print(cobalt.values())

# dasturchilar={
#     'ali':['python','c++'],
#     'vali':['html','css','javascript'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()}:", end='')
#     for til in tillar:
#         print(f"{til.upper()} ", end='')


hamkasblar={
    'baxrom':{'familiya':"umarov",
           'tyil':2004,
           'malumot':'oliy',
           'tillar':['python','nodejs']
           },
    'firdavs':{'familiya':'boltayev',
               'tyil':2003,
               'malumot':'o\'rta maxsus',
               'tillar':['html','css','javascipt']},
    'ramazon':{'familiya':'jamolov',
               'tyil':2002,
               'malumot':'oliy',
               'tillar':['c++','c#','delphi']}
     }
for ism,info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yil tug'ilgan.\n"
          f"Ma'lumoti: {info['malumot']}.\n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
    
    
    
    
    
    
    
