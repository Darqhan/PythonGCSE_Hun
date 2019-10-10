'''
5.feladat
2008_október robot.txt feladatsorhoz
bekérem az új formátumú szöveget, és visszafejtem a régi formába
'''

def bekeres():
    xyz=""
    while ((len(xyz)>199)or (len(xyz)==0)):
        xyz = input("új formátumú szöveg: ")
    return xyz


proba_txt = "4KND3EKND2E"
i=0
vissza_txt = ""
while( i < len(proba_txt)):
    if (proba_txt[i] in '23456789'):
        vissza_txt += (proba_txt[i+1]*int(proba_txt[i]))
        i+=2
    else:
        vissza_txt += (proba_txt[i])
        i+=1
print (vissza_txt)
    
