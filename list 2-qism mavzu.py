# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 12:04:41 2021

@author: User
"""

cars=['audi','bmw','caddy','damas','ford']
avto_lar=['nissan','gmc','tayota','lexus','prado']
#cars.sort()
#cars.sort(reverse=True)
#avto_lar.sort(reverse=False)
#print(avto_lar)

mehmonlar=['Botir','Ahmad','Farrux','Rustam']
#print("sorted() bilan ishlangan ismlar: ",sorted(mehmonlar))
#print("Asl jadval quyidagicha edi: ",mehmonlar)
#print("Teskari tartib: ",sorted(mehmonlar,reverse=True))

ages=[34,21,89,0.54,7,8,-96]
#print("O'sish tartibida: ",sorted(ages))
#print("Kamayish tartibida: ",sorted(ages,reverse=True))

mevalar=['olma','uzum','gilos',"anjir","nok","olxo'ri"]
#mevalar.reverse()
#print(mevalar)
#cars.reverse()
#print(cars)
#avto_lar.reverse()
#print(avto_lar)

#print("Mehmonlar soni: ",len(mehmonlar))
#print("Mashinalar soni: ",len(cars))
#print("Avtolar soni: ",len(avto_lar))
#print("Mevalar soni: ",len(mevalar))
#print("Yoshlar soni: ",len(ages))

sonlar=list(range(0,10))
sonlar1=list(range(23,54))
sonlar2=list(range(34,40))
#print(sonlar)
#print(sonlar1)
#print(sonlar2)

just_sonlar=list(range(0,20,2))
toq_sonlar=list(range(1,20,2))
sonlar0=list(range(10))
#print("Juft sonlar: ",just_sonlar)
#print("Toq sonlar: ",toq_sonlar)
#print("10 gacha sonlar: ",sonlar0)

numbers=[12000,3000,65000,24000,312,90,-5,-72]
#print("sonlarning eng kichigi: ",min(numbers))
#print("Sonlarning eng kattasi: ",max(numbers))
#print("Sonlarning yi'g'indisi: ",sum(numbers))
#print("Eng kattasi: ",max(numbers),\
#".Eng kichigi",min(numbers),\
#".Yig'indisi",sum(numbers))

#print(cars)
#my_cars=cars[0:2]
#print(my_cars)
#s_cars=cars[2:]
#print(s_cars)
#t_cars=cars[:]
#print(t_cars)

raqamlar=[1,2,3,4,5,6]
raqamlar2=raqamlar[:]
raqamlar2.append(7)
raqamlar2.append(8)
#print("Bu raqamlar-dagi sonlar: ",raqamlar)
#print("Bu raqamlar2-dagi sonlar:",raqamlar2)

toys=('dino','lizard','tortoise','spider')
toys=list(toys)
toys.append('car')
toys.insert(0,'teddy')
toys=tuple(toys)
#print(toys)
#print(toys[0])
#print(toys[-1])