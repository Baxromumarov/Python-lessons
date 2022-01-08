# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:03:18 2022

@author: User
"""



import unittest
from soztop import get_word

class soztop_test(unittest.TestCase):
    
    def test_word(self):
        self.assertIsNotNone(get_word)
      
  
unittest.main()