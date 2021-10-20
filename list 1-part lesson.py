# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:28:42 2021

@author: User
"""
mevalar=['olma','anor','banan','shaftoli']
narxlar=[12_000,8_000,23_500,2_000]
sonlar=[1,2,3,"to'rt","besh"]
ismlar=[]


#print("Birinchi meva: ",mevalar[0])
#print("Ikkinchi meva: ", mevalar[1])
#print("Uchinchi meva: ",mevalar[2])
#print("Oxirgi meva: ",mevalar[-1])
# yoki
#print("Oxirgi meva: ",mevalar[3])


#print("Birinchi meva: ",mevalar[0].upper())
#print("Ikkinchi meva: ", mevalar[1].capitalize())
#print("Uchinchi meva: ",mevalar[2].title())
#print("Oxirgi meva: ",mevalar[-1].upper())
# yoki
#print("Oxirgi meva: ",mevalar[3].capitalize())


#print(narxlar[0]+narxlar[-1])
#print(narxlar[1]-narxlar[2])
#print(narxlar[1]+mevalar[0])

#narxlar[0]=7_000
#narxlar[-1]=6_500 #narxlarga yangi qiymat kiritadi


#mevalar.append('ananas') #mevalarga ananas qo'shadik
#print(mevalar)


cars=[]
cars.append('malibu')
cars.append('spark')
cars.append('nexia')

cars.insert(0,"Tucson")
cars.insert(3,'Sonata')
#print(cars)

#del mevalar[0]
#mevalar.insert(0,'Mango')
#print(mevalar)

#del narxlar[2]
#narxlar.insert(2,4_000)
#print(narxlar)


mevalar.remove("shaftoli")
cars.remove("Tucson")
cars.remove("Sonata")
narxlar.remove(12_000)
sonlar.remove("besh")
sonlar.remove("to'rt")
#print(mevalar)
#print(narxlar)
#print(cars)
#print(sonlar)

#hayvonlar=["it","mushuk","sigir","ot"]
#yoq=hayvonlar.pop(-1)
#print("Menda "+str(hayvonlar)+" bor")
#print("Yaqinda "+str(yoq)+" sotib olmoqchiman")


numbers=[1,2,3,4,5]
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
