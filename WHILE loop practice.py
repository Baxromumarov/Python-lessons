# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:08:36 2021

@author: User
"""



# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
# print('Rahmat!')       





# print("Sevimli kitoblaringizni kiriting ",end='')
# print("(to'xtatish uchun 'stop' deb yozing') : ")
# books=list()
# while True:
#     savol=input('Kitob nomi: ')
#     books.append(savol)
#     if savol=='stop':
#         break
    
# print('Siz kiritgan kitoblar',books)





# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif yosh<18:
#         narh = 3000
#     elif yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")





savol="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol+="Musbat son kiriting"
savol+="(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat=input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz=float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng.")













    
    
