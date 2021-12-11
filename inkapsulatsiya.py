# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:09:24 2021

@author: User
"""



from uuid import uuid4

class Talaba:
    """Talaba klassi"""
    
    def __init__(self,nomi,talabalar):
        self.nomi=nomi
        self.talabalar=[]
    son_talaba=0
    
    def __init__(self,ism,familiya,kurs,tyil,yosh=None):
        """Talaba ma'lumotlari"""
        self.ism=ism
        self.familiya=familiya
        self.kurs=kurs
        self.tyil=tyil
        self.hyil=2021
        self.yosh=yosh
        self.__id=uuid4()
        Talaba.son_talaba +=1
        
        
    def get_ism(self):
        """Ism qaytaruvchi funksiya"""
        return self.ism.title()
    
    def get_familiya(self):
        """Familiya qaytaruvchi funksiya"""
        return self.familiya.title()
    
    def get_kurs(self):
        """Talaba bosqichi"""
        return self.kurs
    
    def get_tyil(self):
        """Talaba yili"""
        return self.tyil
    
    
    def get_id(self):
        """Talaba id kodi"""
        return self.__id
    
    def get_info(self):
        """Talaba ma'lumotlarini chiqaruvchi funksiya"""
        malumot = f"Talabaning ismi:{self.get_ism}\nFamiliyasi:{self.get_familiya}\nBosqichi:{self.get_kurs}\n"
        malumot+= f"Talaba tug'ilgan yil:{self.get_tyil}\n"
       
        return malumot
    
    def get_t_id(self):
        id_kod = f"Talabaning id kodi: {self.get_id}"
        
        return id_kod
    
    def get_malumot(self):
        return [talaba.get_info() for talaba in self.talabalar]
    
    
    
talaba1=Talaba("baxrom","umarov",1,2004, )
talaba2=Talaba("shavkat","mardonov",2, 2003)
talaba3=Talaba("akbar","sobirov",4, 2003)

talabalar=[talaba1, talaba2,talaba3]   
# while True:
#     savol1 = input("Talabalar haqidagi ma'lumotlarni ko'rishni xohlaysizmi (yes/no)? ")
#     if savol1 == "yes":
#         print("Ma'lumotlar turini tanlang ")
#         savol2 = int(input("Talaba haqidagi ma'lumotlar: (1) "))
#         savol3 = int(input("Talaba id kodi: (2)"))
#         savol4 = int(input("Talabalar soni: (3)"))
        
#         if savol2 == 1:
#             savol5 = int(input("Talaba tartib raqamini kiriting: "))
            
#             if savol5 == 1:
#                 print(talaba1.get_info())
#             if savol5 == 2:
#                 print(talaba2.get_info())
#             if savol5 == 3:
#                 print(talaba3.get_info())
                
#         else:
#             print("Xato!")
#             continue
    
#         if savol3 == 2:
#             savol6=int(input("Talaba tartib raqamini kiriting: "))
            
#             if savol5 == 1:
#                 print(talaba1.get_t_id())
#             if savol5 == 2:
#                 print(talaba2.get_t_id())
#             if savol5 == 3:
#                 print(talaba3.get_t_id())
                
#         else:
#             print("Xato!")
#             continue
        
#         if savol == 4:
#             print(Talaba.son_talaba)
            
#         else:
#             print("Xato!")
#             continue
    
#     else:
#         savol7=input("Dastur tugashini xohlaysimzi (yes/no)?")
#         if savol7 == 'yes':
#             break
#         else:
#             pass
    
    
    
    
    
    
    
    
    
    