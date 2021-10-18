# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:02:44 2021

@author: User
"""

davlatlar=["O'zbekiston","Rossiya","AQSh","Xitoy"]
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)

#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print("Alifbo bo'yicha: ",davlatlar)
#davlatlar.sort(reverse=True)
#print("Alifboga teskari tartibda: ",davlatlar)

sonlar=list(range(120,1200))
#print(sonlar)
#print("Sonlar yig'indisi: ",sum(sonlar))
#print("Eng katta va eng kichik sonlar ayirmasi: ",max(sonlar)-min(sonlar))
#print(len(sonlar))

#print("Boshidan 20 ta son: ",sonlar[:20])
#print("O'rtasidan 20 ta: ",sonlar[540:560])
#print("Oxiridan 20t ason: ",sonlar[-20:])

taomlar=['Osh',"Lag'mon","Non kabob","Chuchvara","Norin"]
nonushta=taomlar[:]
nonushta.remove("Lag'mon")
nonushta.remove("Non kabob")
nonushta.remove("Chuchvara")
nonushta.append('Quymoq')
nonushta.append('Sut')
#print("Ertalabgi ovqatlar: ",nonushta)
#print("Kuchli ovqatlar: ",taomlar)
#nonushta[0]="qaymoq va non"
#nonushta=tuple(nonushta)
#print(nonushta)
