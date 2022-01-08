# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:08:55 2022

@author: User
"""



from docxtpl import DocxTemplate

anketa = DocxTemplate("anketa.docx")

info = {'ism' : "Alijon",
        'familiya' : "Valiyev",
        'otasi' : "Boqiyevich"}

anketa.render(info)
anketa.save("yangi_anketa.docx")
