# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:01:04 2021

@author: User
"""



def ism_yosh(ism,yosh):
    """Foydalanuvchi ismi va yoshini aniqlovchi dastur"""
   
    print(f"{ism.title()} siz {2021-yosh}-yilda tug'ilgansiz! )
    
ism_yosh(ism=input("Ismingizni kiriting: "),yosh=int(input("Yoshingizni kiriting: ")))


# while True:
#     def kvadrat_kub(son):
#         """Sonning kvadratini va kubini hisoblaydigan funksiya"""
#         print(f"Sonning kvadrati-{son**2}\nkubi-{son**3}")

#     kvadrat_kub(son=float(input("Sonni kiritting: ")))
    



# def toq_juft(son):
#      """Sonning juft yoki toqligini aniqlaydigan dastur"""
#      if son%2==0:
#             print(f"Kiritgan {son} soningiz juft ekan!")
#      else:
#             print(f"Kiritgan {son} soningiz toq ekan!")
    
# toq_juft(son=int(input("Son kiriting: ")))

   


# def katta_kichik(son1,son2):
#     """Sonlarning kattasini chiqaruvchi funksiya"""
#     if son1>son2:
#         print(f"{son1}>{son2}")
#     elif son1==son2:
#         print("Sonlar teng ekan!")
#     else:
#         print(f"{son1}<{son2}")


# katta_kichik(son1=float(input("1-sonni kiriting: ")),son2=float(input("2-sonni kiriting: ")))




# def son_darajasi(x,n):
#     """X ning n-darajasini chiqaruvchi funksiya"""
#     print(f"X ning n-darajasi--{x**n} ga teng")

# son_darajasi(x=float(input("x ni kiriting: ")),n=float(input("darajani kiriting: ")))




# def son_kv(x,n=2):
#     """X ning kvadratini hisoblaydigan funksiya"""
#     print(f"X ning kvadrati-- {x**n}")

# son_kv(x=float(input("x ninig qiymatini kiriting: ")))







# def qold_bol(son):
#     """ soning qoldiqsiz bo'linuvchilarini chiqaruvchi funksiya"""
  
#     for n in range(2,11):
#        if not son%n:
#             print(f"{son} ni {n} ga qoldiqsiz bo'linadi")
#        else:
#             print(f"{son} ni {n} ga bo'linmaydi!")
         

# qold_bol(son=int(input("Son kiriting: ")))





