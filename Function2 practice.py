# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 13:19:12 2021

@author: User
"""


# def foydalanuvchi_info(ism,familiya,yosh,tyil,tjoy,email=None,tel=None):
#     """Foydalanuvchilarning ma'lumotlarini jamlovchi funksiya"""
#     foydalanuvchi={'ism':ism,
#         'familiya: ':familiya,
#         'yosh: ':2021-tyil,
#         'tyil: ':tyil,
#         'tjoy: ':tjoy,
#         'email:':email,
#         'tel: ':tel}
#     return foydalanuvchi
    
# print("Sizning ma'lumotlaringizni to'playmiz ")
# malumotlar=[]
# while True:
#     print("Quyidagi ma'lumotlarni kiriting: ")
#     ism=input("Ismingizni kiriting: ")
#     familiya=input("Familyangizni kiriting: ")
#     tyil=input("Tug'ilgan yilingizni kiriting: ")
#     tjoy=input("Tug'ilgan joyingizni kiriting: ")
    
#     for malumot in malumotlar:
#         if malumot['tel'] and malumot['email']:
#             tel=malumot['tel']
#             email=malumot['email']
            
#     email=input("elektron pochtangizni kiriting: ")
#     tel=input("Telefon raqamingizni kiriting: ")
        
#     savol=input("Yana biror kishining ma'lumotlarini kiritasizmi (yes/no)? ")
#     if savol=='yes':
#         continue
#     else:
#         print("Bizning xizmatimizdan foydalanganingiz uchun sizdan minnatdormiz!")
#         break

# print("Barcha ma'lumotlar saqlandi!")
# print("Ma'lumotlar:")
# for malumot in malumotlar:
#     print(f"{malumot['ism'].title()} {malumot['familiya'].title()}," 
#           f"{malumot['yosh']} yoshda, telefoni: {malumot['tel']}")






# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max



# def aylana_info(radius,pi=3.14159):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetr":2*radius*pi,
#               "yuza":pi*radius**2}
#     return aylana


# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar
    






# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))
            














































