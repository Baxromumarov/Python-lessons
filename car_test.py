# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 05:03:11 2021

@author: User
"""



import unittest
from cars import Car

class Cartest(unittest.TestCase):
    """Car klasini tekshirish uchun"""
    def setUp(self):
        make = "Gm"
        model = "malibu"
        year = 2020
        self.price = 40_000
        self.km = 10_000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)
        
    def test_create(self):
        # Qiymatlar mavjudligini tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini tekshirish
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini tekshiramiz
        self.assertEqual(0,self.avto1.get_km())
        # avto2 narxini tekshiramiz
        self.assertEqual(self.price,self.avto2.price)
        
    def test_set_price(self):
        self.avto2.set_price(self.price)
        self.assertEqual(self.price,self.avto2.price)
        
    def test_add_km(self):
        #Musbat qiymat beramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        #Manfiy qiymat beramiz
        new_km = -5_000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error),ValueError)
            
    def test_get_info(self):
        avto1_info = "GM Malibu,2020-yil, 0 km yurgan."
        self.assertEqual(avto1_info,self.avto1.get_info())
        # avto1 narxi va km ni o'zgartiramiz
        self.avto1.set_price(50_000)
        self.avto1.add_km(20_000)
        avto1_info = "GM Malibu,2020-yil, 20000 km yurgan. Narxi: 50000"
        self.assertEqual(avto1_info,self.avto1.get_info())
        
unittest.main()
                