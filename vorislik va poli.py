class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        
    def get_info(self):
            """Shaxs haqida ma'lumot"""
            info=f"{self.ism} {self.familiya}."
            info+=f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
            return info
        
    def get_age(self,yil):
            """Shaxsning yoshini qaytaruvchi metod"""
            return yil-self.tyil
        
class Talaba(Shaxs):
    """Talabaning klassi"""
    def __init__(self,ism,familiya,passport,tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__init__(ism, familiya, passport, tyil)
        self.idraqam=id
        self.bosqich=1
        
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
        
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info=f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()}-bosqich. ID:{self.idraqam} "
        return info
    
    def fanga_yozil(Fan):
        """Fan obyektini o'zlashtirish"""
        return self.fanlar.append(fanga_yozil)
    
    def remove_fan(self):
        """Fanlarni o'chirish"""
        return fanlar.remove(fan)
    
    
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
        
    def get_manzil(self):
        """Manzil ko'rinishi"""
        manzil=f"{self.viloyat} viloyati, {self.tuman} tumani,"
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

    def __init__(self,fanlar):
        self.fanlar=fanlar
    
    def get_fanlar(self):
        """Fanlar"""
        fan=self.fanlar=[]
        return fan

class Fan:
    """Fanlar klassi"""
    def __init__(self,fan0,fan1,fan2):
        """Fanlar jamlanmasi""" 
        self.fan0=fan0
        self.fan1=fan1
        self.fan2=fan2
        
    def get_fan0(self):
        """Fan0"""
        return self.fan0
    
    def get_fan1(self):
        """Fan1"""
        return self.fan1
    
    def get_fan2(self):
        """Fan2"""
        return self.fan2
    

            