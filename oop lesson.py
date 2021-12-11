# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
        
        def set_bosqich(self, bosqich):
            """Talabaning kursini yangilovchi metod"""
            self.bosqich=bosqich
            
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytiradi """
        self.bosqich+=1
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
talaba1=Talaba("Baxrom", "Umarov", 2004)


class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
        
        def add_student(self,talabalar):
            """fanga talabalar qo'shildi"""
            self.talabalar.append(talaba)
            self.talabalar_soni+=1
            
        def get_name(self):
            """Fan nomi"""
            return self.nomi
        
        def get_students(self):
            """Fanga yozilgan talabalar haqida ma'lumot"""
            return [talaba.get_info() for talaba in self.talabalar]
        
        def get_students_num(self):
            """Fanga yozilgan talabalar soni"""
            return self.talabalar_soni

fan1=Fan("Matematika")
            
































