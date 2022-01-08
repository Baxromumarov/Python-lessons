# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:10:56 2021

@author: User
"""

import unittest
from funk import get_sonlar, get_matn, get_juft


class funktest(unittest.TestCase):
    def test_sonlar(self):
        sonlar = get_sonlar(12,13,14)
        self.assertEqual(sonlar,14)

    
    def test_matn(self):
        matn = get_matn('salom baxrom, yaxshimisan?')
        self.assertEqual(matn, 'Salom Baxrom, Yaxshimisan?')
        
        
    def test_numbers(self):
        son = get_juft(list(range(0,11)))
        self.assertEqual(son,list(range(0,11,2)))
        
        
unittest.main()
        