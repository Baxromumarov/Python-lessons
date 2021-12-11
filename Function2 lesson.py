# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:12:12 2021

@author: User
"""


# def toliq_qiymat_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism=f"{ism} {familiya}"
#     return toliq_ism

# talaba1=toliq_qiymat_yasa('baxrom','umarov')
# talaba2=toliq_qiymat_yasa('shavkat','mardonov')

# print(talaba1.title())
# print(talaba2.title())

# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")




# def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#     """ To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
        
#     return toliq_ism.title()

# talaba1=toliq_ism_yasa("baxrom",'umarov','qahramonovich')
# talaba2=toliq_ism_yasa('shavkat','mardonov')
 
# print(f"Bugun darsga kelmagan talabalar: {talaba1} va {talaba2}")




def avto_info(make,model,rangi,korobka,yili,narxi=None):
    avto={'kompaniya':make,
          'model':model,
          'rang':rangi,
          'korobka':korobka,
          'yil':yili,
        'narx':narxi}
    
    return avto

# avto1=avto_info('Gm','Malibu','Qora','Avtomat',2018)
# avto2=avto_info('Gm','Cobalt','Oq','Mexanika',2016,15_000)
# avtolar=[avto1,avto2]
# print("Onlayn do'konimizda mavjud avtomobilar: ")
# for avto in avtolar:
#     if avto['narx']:
#         narx=avto['narx']
#     else:
#         narx="Noma'lumm"
#     print(f"{avto['rang']} {avto['model']}. Narxi {narx} ")




# def oraliq(min,max,qadam=None):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     print(sonlar)

#     return sonlar

# oraliq(min=int(input("Minimal qiymatni kiriting: ")),\
    # max=int(input("Maximal qiymatni kiriting: ")),qadam=int(input("Qadamni kiriting: ")))




# print("Saytimizda avtolar ro'yxatini shakllantiramiz. ")
# avtolar=[]
# while True:
#     print("Quyidagi ma'lumotlarni kiriting",end="")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi: ")
    
#     avtolar.append(avto_info(kompaniya,model,rangi,\
#                              korobka,yili,narxi))
    
#     javob=input("Yana avto qo'shasizmi(yes/no)? ")
#     if javob=='no':
#         break
# print(f"{avtolar[0]['model']},{avtolar[0]['narx']}")















