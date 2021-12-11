# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:32:07 2021

@author: User
"""

# while True:
#   yosh=input("Yoshingizni kiriting: ")
#   try:
#     yosh=int(yosh)
#     # print(f"Siz {2021-yosh}-yilda tug'ilgansiz")
#   except:
#     print("Butun son kiritmadingiz!")
#   else:
#     print(f"Siz {2021-yosh}-yilda tug'ilgansiz")

#   stop=input("Agar dasturni to'xtatmoqchi bo'lsangiz stop deb yozing!\nAgar dastur davom etishini xohlasangiz 'Enter' tugmasini bosing! ")
  

#   if stop.lower()=='stop':
#       break
#   else: 
#       continue
        


# yosh= input("Yoshingizni kiriting: ")
# try:
#     yosh=int(yosh)
# except ValueError:
#     print("Butun son kiritmadingzi! ")
# else:
#     print(f"Siz {2021-yosh}-yilda tug'ilgansiz. ")
    
        
# x,y=5,10
# try:
#     c=y/(x-5)
# except:
#     print("Nolga bo'lib bo'lmaydi!")



# mevalar=['olma','anor','uzum','banan']
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos! ")



# user={
#       'username':'baxromumarov',
#       'status':'developer',
#       'email':'sdsd@gmail.com',
#       'phone': 900809760
#       }
# key='tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas! ")


# fayl='data.txt'
# try:
#     f=open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas! ")




# n=input('Butun son kiriting: ')
# try:
#     n=int(n)
#     x=20/n
# except ValueError:
#     print("Butun son kiritmadingiz! ")
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas! ")
# else:
#     print(f"x={x}")



# user={
#       'username':'baxromumarov',
#       'status':'developer',
#       'email':'sdsd@gmail.com',
#       'phone': 900809760
#       }

# key='tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     pass




# yosh=21
# if yosh<20:
#     pass
# else:
#     pass



# yosh=input("Yoshingizni kiriting: ")
# try:
#     yosh=int(yosh)
#     print(f"Siz {2021-yosh}-yilda tug'ilgansiz")
# except:
#     print("Butun son kiritmadingiz! ")





# while True:
#     yosh=input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh=int(yosh)
#         break
# print(f"Siz {2021-yosh}-yilda tug'ilgansiz ")





while True:
    yosh=input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh=int(yosh)
        print(f"Siz {2021-yosh}-yil tug'ilgansiz!")   
        
        savol=input("Dastur yana davom etsinmi(ha/yo'q)?: ")
        if savol=='ha':
            continue
        else:
            break
        
    else:
        print("Butun son kiritmadingiz! ")
       


# while True:
#     x=int(input("Son kiriting: "))
#     y=int(input("Yana son kiriting: "))
#     try:
#         print(x, '/', y, '=',x/y)
#     except ValueError:
#         print("Butun son kiritmadingiz! ")
#     except ZeroDivisionError:
#         print("Nolga bo'lish mumkin emas! ")
  
#     savol=input("Dasturni to'xtatishni istaysizmi (ha/yo'q)? ")
#     if savol.lower()=='ha':
#         print("Dastur to'xtadi! ")
#         break
#     else:
#         continue

























