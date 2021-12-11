# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:10:10 2021

@author: User
"""



class Avto:
    __num_avto=0
    """Avtomobil klassi"""
    
    def __init__(self,make,model,rang,yil,narx):
        """Avtomovbil xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        Avto.__num_avto+=1
        
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    
avto1=Avto("GM","Malibu","Qora",2020,40_000)
# print(avto1)

class Avtosalon:
    
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len (self.avtolar)
    
    def add_avto(self,avto):
        if isinstance(avto,Avto):
            self.avtolar.append(avto)
        else:
            print("Avto obyektini kiriting: ")
salon1=Avtosalon("MaxAvto")            
avto1=Avto("GM","Malibu","Qora",2020,40_000)
avto2=Avto("GM","cobalt","Qora",2020,40_000)

for avto in [avto1,avto2]:
    salon1.add_avto(avto)
            