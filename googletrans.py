# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 07:00:02 2022

@author: User
"""



import requests
from pprint import pprint

# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)

country = "Uzbekistan"
url = f"https://countrycode.org/Uzbekistan"
r = requests.get(url)
r_json = r.json()
print(r_json['Uzbekistan'])