# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# import pickle
import json

data = {
        "model" : "malibu",
        "rang" : "qora",
        "yil" : 2020,
        "narx": 40_000}

data_json = json.dumps(data)
# print(data_json)

talaba_json = """ {"ism":"Hasan","familiya":"Husanov","tyil":2000} """
# talaba = json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']}")


# with open("fayl.json",'w') as f:
#     json.dump(data_json,f)
    
# with open("fayl1.json",'w') as f:
#     json.dump(talaba_json,f)
    



# with open("talaba.json", 'w') as f:
#     json.dump(talaba,f)



with open('talaba.json','w') as f:
    json.dump(talaba,f)








