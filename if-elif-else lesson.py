# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:17:56 2021

@author: User


"""
# son=float(input("O'ylagan soningizni kiriting: "))
# if son>0:
#     print("Kiritgan soningiz musbat ekan!")
# elif son<0:
#     print("Kiritgan soningiz manfiy ekan!")
# else:
#     print("Kiritgan soningiz nol ekan!")
    
# 2-variant.Yuqoridagi dastur uchun

# yosh=int(input("yoshingizni kiriting: "))
# if yosh<=4:
#     narx=0
# elif yosh<=12:
#     narx=5000
# else:
#     narx=10_000
# print(f"Sizga kirish narxi {narx} so'm")




# yosh=int(input("yoshingizni kiriting: "))
# if yosh<=4:
#     narx=0
# elif yosh<=12:
#     narx=5_000
# elif yosh<50:
#     narx=10_000
# else:
#     narx=8_000
# print(f"Sizga kirish narxi {narx} so'm")




# kun=input("Bugun qaysi kun: ")
# if kun.lower()=='dushanba':
#     print("Bugun dars 13:30 da. \n1-Jismoniy tarbiya\n2-MKG\n3-MKG")
# elif kun.lower()=='seshanba':
#     print("Bugun dars 11:30 da. \n1-Rus tili \nEnglish \nMKG(leksiya)")
# elif kun.lower()=='chorshanba':
#     print("Bugun dars 13:30 da. \n1-Oliy Matematika (amaliy) \n2-English")
# elif kun.lower()=='payshanba':
#     print("Bugun dars 11:30 da. \n1-Fizika(laboratoriya) \n2-Oliy matematika(Leksiya) \n3-MKG" )
# elif kun.lower()=='juma':
#     print("Bugun dars 13:30 da. \n1-Fizika(leksiya.Yavkacheva) \n2-Rus tili")
# else:
#     print("Bugun dam olish kuni. Vaqtingizni shaxsiy rivojlanishingiz uchun sarflang!")





# kun=input("Bugun qaysi kun?>>> ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print('Bugun ish kuni.')





# print(True or False)
# print(True or True)
# print(False or False)





# kun=input("Bugun qaysi kun? ")
# harorat=float(input("Havo harota qanday? "))
# if (kun.lower()=="yakshanba" or kun.lower()=='shanba') and harorat>30:
#     print("Kettik dachaga boramiz!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print("Uyda dam olamiz!")
# else:
#     print("Bugun ish kuni.Shuning uchun ishga borishingiz kerak!")




# yosh=int(input("iltimos,yoshingizni kiriting: "))
# kun=input("Bugun qaysi kun? ")
# if (yosh<7 or yosh>55) and kun.lower()=="seshanba":
#     print("Bugun siz uchun kirish bepul!")
# else:
#     print("Chipta narxi 5000 so'm")




# narx=15_000
# choy=True #true ni o'rniga 1 qo'yish mumkin
# salat=False #false ni o'rniga 0 qo'yish mumkin
# if choy and salat:
#     narx=narx+10_000
# elif choy or salat:
#     narx=narx+5_000
# print(f"To'lov miqdori: {narx}")    




# narx=15_000
# choy=True
# salat=False
# non=True
# kompot=True
# assorti=False

# if choy:
#     print("Mijoz choy oldi")
#     narx=narx+3_000
# if salat:
#     print("Mijoz salat oldi")
#     narx=narx+5_000
# if non:
#     print("Mijoz non oldi")
#     narx=narx+2_000
# if kompot:
#     print("Mijoz kompot oldi")
#     narx=narx+5_000
# if assorti:
#     print("Mijoz assorti oldi")
#     narx=narx+15_000
# print(f"Jami to'lov: {narx} so'm")


# menyu=['osh', 'qozonkabob','shashlik','norin','somsa']
# print('manti' in menyu)
# print('osh' in menyu)



# menyu=['osh', 'qozonkabob','shashlik','norin','somsa']
# ovqat=input("Nima ovqat yeysiz?>>>> ")
# if ovqat.lower() in menyu:
#     print("Buyurtmangiz qabul qilindi.")
# else:
#     print("Afsuski,bizda bunday ovqat yo'q")


# menyu=['osh', 'qozonkabob','shashlik','norin','somsa']
# print('choy' not in menyu)

# menyu=['osh', 'qozonkabob','shashlik','norin','somsa']
# ovqat=input("Nima ovqat yeysiz?>>>> ")
# if ovqat.lower() not in menyu:
#     print("Afsuski,bizda bunday ovqat yo'q")
# else:
#     print("Buyurtmangiz qabul qilindi")


# menyu=['osh', 'qozonkabob','shashlik','norin','somsa']
# buyurtmalar=['osh','somsa','manti','shashlik']

# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz,menyuda {taom} yo'q")

# list1=[]
# if list1:
#     print("Ro'yxat bo'sh emas")
# else:
#     print("Ro'yxat bo'sh")

# menyu=['osh', 'qozonkabob','shashlik','norin','somsa']
# buyurtmalar=['osh','somsa','manti','shashlik']

# if buyurtmalar:
#  for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz,menyuda {taom} yo'q")

