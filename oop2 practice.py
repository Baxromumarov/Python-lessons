# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 18:47:02 2021

@author: User
"""



class Avto:
    """avtomobillar haqidagi klass"""
    
    def avto_info(self, model, rang, korobka, narx):
        """avtolar haqidagi ma'lumotlar"""
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.km=0
        
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_korobka(self):
        return self.narx
    
    def get_km(self):
        return self.km
    
def seee_methods(klass):
    return[method for method in dir (klass) if  method.startswith('__') is False]








