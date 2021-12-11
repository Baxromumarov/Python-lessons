# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 06:02:39 2021

@author: User
"""



# filenomi='bugun.txt'
# with open(filenomi,'w') as file:
#     file.write('with funksiya, open ochish uchun, read o\'qish uchun')


# with open('bugun.txt') as file:
#     bugun=file.read()
#     print(bugun)

with open('pi_million_digits.txt') as file:
    pi_million_digits=file.read()
    # print(pi_million_digits)


# yil=input("Yilingizni kiriting: ")

# if yil in pi_million_digits:
#     print("ha")
# else:
#     print("yo'q")

# bdate = '07042004'
# print(bdate in pi_million_digits)


# import pickle

# with open('pi_million_digits.txt') as file:
#     pi = file.read()
# pi = pi.rstrip() 
# pi = pi.replace('\n','') 
# pi = pi.replace(' ','')



# pi = float(pi) 

# with open('amaliyot/pi_float.dat','wb') as file:
#      pickle.dump(pi, file)



while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')

with open('books.txt') as file:
    books=file.read()
    print(books)










