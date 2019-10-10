# lottó feladat
#1. Kérje be a felhasználótól az 52. hét megadott lottószámait!  89 24 34 11 64
#2 A program rendezze a bekért lottószámokat emelkedő sorrendbe!
# A rendezett számokat írja ki a képernyőre!
#3 kérjen be egy számot 1-51 közt, nem kell vizsgálni valid-e, majd írja ki.
#4 Írja ki a képernyőre a bekért számnak megfelelő sorszámú hét lottószámait, a
# lottosz.dat állományban lévő adatok alapján!
# 5. A lottosz.dat állományból beolvasott adatok alapján döntse el, hogy volt-e olyan
#szám, amit egyszer sem húztak ki az 51 hét alatt! A döntés eredményét (Van/Nincs) írja ki
# a képernyőre!
# 6. A lottosz.dat állományban lévő adatok alapján állapítsa meg, hogy hányszor
#volt páratlan szám a kihúzott lottószámok között! Az eredményt a képernyőre írj
# a ki!
# 7. Fűzze hozzá a lottosz.dat állományból beolvasott lottószámok után a felhasználótól
#bekért, és rendezett 52. hét lottószámait, majd írja ki az összes lottószámot a lotto52.ki
#szöveges fájlba! A fájlban egy sorba egy hét lottószámai kerüljenek, szóközzel elválasztva
#egymástól!
# 8. Határozza meg a lotto52.ki állomány adatai alapján, hogy az egyes számokat hányszor
# húzták ki 2003-ban. Az eredményt írja ki a képernyőre a következő formában: az első sor
# első eleme az a szám legyen ahányszor az egyest kihúzták! Az első sor második eleme az
# az érték legyen, ahányszor a kettes számot kihúzták stb.! (Annyit biztosan tudunk az értékekről, hogy mindegyikük egyjegyű.)
print("2005 MÁJUS")
'''
print (" 1. feladat: Kérje be a felhasználótól az 52. hét megadott lottószámait!  \n 89 24 34 11 64")
otszam=[]
for i in range(5):
    bekert = input("szám: ")
    otszam.append(int(bekert))
print ("2. feladat: 52-dik számai emelkedő sorrendben")
otszam.sort()
print (otszam)
'''
print ("3.feladat: Kérj be egy számot 1-51 közt")

def harmadik(): 
    hetszama =input("adj egy számot 1-51 közt: ") 
    hetszamIgaz = (int(hetszama)<51) and (int(hetszama)>0)
    while (hetszamIgaz==False):
        print("rossz számot adtál")
        hetszama =input("adj egy számot 1-51 közt: ")
        hetszamIgaz = (int(hetszama)<51) and (int(hetszama)>0)
    return int(hetszama) 

melyiket = harmadik()        
print ("ehetit kérted be:",melyiket)

print ("4. feladat: Ennek a sorszámnak megfelelő hét nyerőszámai. ")
file = open("lottosz.dat",'r')
hetinyeroszamok = []
for line in file:
    hetinyeroszamok.append(line)
       
print (hetinyeroszamok[melyiket-1])
print ("5.feladat: kiírni melyik szám nem fordult elő egyszer sem")
data = {}
for i in range(1,91):
    data.update({i:"none"})
paratlan=0
for i in range(len(hetinyeroszamok)):
    hetinyeroszamok[i]=hetinyeroszamok[i].split()
    for nysz in range(1, 91):
        if str(nysz) in hetinyeroszamok[i]:
            data.update({nysz : "in"})
            if (nysz%2==0):
                paratlan+=1
nemvoltbenne = []
for (key, value) in data.items():
	if (value=="none"):
		nemvoltbenne.append(key)
print ("ezek a számok nem voltak egyszer sem kihúzva: ", nemvoltbenne)
print ("6.feladat: mennyiszer húztak páratlan számot ki:", paratlan) 
print ("7.feladat: az első öt szám hozzáapsszítása és kiírás fájlba")
for i in range (len(hetinyeroszamok)):
    for j in range (0,5):
        hetinyeroszamok[i][j]= int(hetinyeroszamok[i][j]) #stringből integerré
with open('new_file.txt', 'w') as f:
    for item in hetinyeroszamok:
        f.write(' '.join(map(str,item)) + "\n") #ez nagyon genya, nem hiszem közsuliban tanítják, hogyna akkor fejből
print ("8.feladat: melyik számot mennyiszer húztak ki, egymás mellé írni a darabszámot, sorban")
mennyiszer=[]
for i in range(1,91): 
    mennyiszer.append(0)#készitek egy 0-s listát

for i in range(1,91):
    for j in range(len(hetinyeroszamok)):
        if (hetinyeroszamok[j].count(i)):
            mennyiszer[i-1]=(mennyiszer[i-1]+1)
print(' '.join(map(str,mennyiszer)))
    



        
        
