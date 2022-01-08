import unittest
from Shaxs import Talaba
from Shaxs import Shaxs

class talabatest(unittest.TestCase):
    """Talaba klassini tekshirish"""
    def setUp(self):
        ism = "Baxrom"
        familiya = "Umarov"
        tyil = 2004
        bosqich = 1
        self.talaba1 = Talaba(ism,familiya,tyil,bosqich)

    def test_get_fullname(self):
        talaba1_info="Baxrom Umarov"
        self.assertEqual(talaba1_info,self.talaba1.get_fullname())
    
    def test_getInfo(self):
        full_info = "Baxrom Umarov. 1-bosqich talabasi "
        self.assertEqual(full_info,self.talaba1.get_info())
    
    def test_voris(self):
        
        self.assertNotIsInstance(Shaxs,Talaba)



unittest.main()