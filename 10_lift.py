print("\n2009.május - LIFT")
print("\n1.feladat: A file beolvasása")
file = open ("igeny.txt","r")
data = []
for items in file:
    data.append(items.rstrip())
data=data[3:]
def from_int_to_string(data):
    '''
    file sorainak split-telése, array in array lesz
    utána pedig integerre konvertálás, hogy számokkal dolgozhassak
    '''
    for i in range(len(data)):
        data[i]=data[i].split()
        data[i]=[int(data[i][0]),int(data[i][1]),int(data[i][2]),int(data[i][3]),int(data[i][4]),int(data[i][5])]
    return data
data = from_int_to_string(data)

print ("\n2.feladat: Kérjük be az induló szintet. level_input() funkció kéri be")
print("100 szintet adhatunk meg, helyett szint = 10 lesz")
def level_input():
    '''
    Ez a funkció addig kér be számot, amig az 1-100 közé nem esik
    '''
    x="0"
    while ((x[0] not in '123456789')or(int(x)>100)):
        x = input("add meg az aktuális szintet:")
        print(x)
print ("\n3.feladat: Az utolsó kérés után hol kell legyen a lift")
print ("A lift a ", data[-1][-2:],".szinten áll az utolsó igény teljesítése után")
print("\n4.feladat: a legkisebb és legnagyibb érintett SZINT")
def levels_done():  
    '''
    Ez a funkció a beolvasott file data listáját szedi szét
    az utolsó két szám kell nekünk, az induló és érkező szint
    A második ciklus számmá alakítja az outputot
    '''
    levels = []
    for i in range(len(data)):
        levels.append(data[i][-2:])
    return levels

def max_levels(levels):
    '''
    A levels_done outputját adjuk be.
    A 0.,1. közül a nagyobbat hasonlítom a max-szal
    '''
    maximum = 0
    for i in range(len(levels)):
        if (max(levels[i])>maximum):
            maximum = max(levels[i])
    return maximum
def min_levels(levels):
    '''
    A levels_done outputját adjuk be.
    A 0.,1. közül a kisebbiket hasonlítom a min-nel
    '''
    minimum = 100
    for i in range(len(levels)):
        if (min(levels[i])<minimum):
            minimum = min(levels[i])
    return minimum
levels = levels_done()
print (max_levels(levels),".szint volt  a legmagasabb érintett szint. ")
print (min_levels(levels),".szint volt  a legalacsonyabb érintett szint. ")
print("\n5.feladat: Mennyiszer indul felfelé a lift, utassal és mennyiszer indul felfelé utas nélkül.")
print ("először írassuk ki a felfelé indulókat simán")
def fel_le(data): 
    '''
    írjuk egy tömbbe, a data listából az utolsó két eredményt, ami a indulás-érkezés
    '''
    level_counter = []
    for i in range(len(data)):
        level_counter.append(data[i][-2])
        level_counter.append(data[i][-1])
    return level_counter 
def igen_nem(data):
    '''
    a megkapott adatokat, a fel_le() fny-ből
    nézzük meg, hogy fel vagy le mennek-e
    '''
    felfele_lefele = [0,0]
    for i in range(0,len(data)-1):
        if (data[i]>data[i+1]):
            felfele_lefele[1]+=1
        else:
            felfele_lefele[0]+=1
    return felfele_lefele

honnan_hova = igen_nem(fel_le(data))
print ("felfelé: ", honnan_hova[0]," alkalommal, míg lefele: ", honnan_hova[1],"alkalommal  történt mozgás")
print("\n6.feladat: Mely csapatok nem lifteztek (tudjuk, hogy 50 csapat van)")
def nem_liftezok_viadala(data):
    '''
    1-50 közt készítek egy listát, amiből leszedem a data[3] alapján a csapatokat, ha léteznek még
    '''
    result=[]
    for i in range(1,51):
        result.append(i)
    for i in range(len(data)):
        if (data[i][3] in result):
            result.remove(data[i][3])
    return result
akik_nem_lifteztek = nem_liftezok_viadala(data)
print(*akik_nem_lifteztek, sep = ", ")  
print ("\n7.feladat: generálj egy csapatszámot(3-s?), gyalogolt-e")
def csapatok_szam_szerint(data):
    '''
    készítsünk listát a csapatok számával, utazásonként
    '''
    result=[]
    for i in range(len(data)):
        result.append(data[i][3])
    return result
'''
készítsünk véletlenszámot, ami benne van az csapataink közt, akik télleg közlekedtek
1-50 közé eső szám
keressük meg a csapatlista
'''
import random
csapat_inspekt = 0
x=csapatok_szam_szerint(data)
while (csapat_inspekt not in x): 
    csapat_inspekt = random.randint(1,50)
print (csapat_inspekt,"az ellenőrzött csapat száma", )
#my_index = x.index(csapat_inspekt)
'''
az adott csapat kiírása a data állományból csapat_mozgas-ba
'''
csapat_mozgas = []
for i in range(len(data)):
    if(data[i][3]==csapat_inspekt):
        csapat_mozgas.append(data[i])
print (csapat_mozgas)
#*******************
bizonyithato = False
for j in range(1,len(csapat_mozgas)-1):
    '''
    Ha az új kiindulás == az előző érkezéssel, akkor nem csalt
    '''
    if (csapat_mozgas[j+1][-2]!=csapat_mozgas[j][-1]):
        bizonyithato = True
        break
if (bizonyithato):
    print ("csalás!", csapat_mozgas[j+1][-2],csapat_mozgas[j][-1])
else:
    print ("nem bizonyitható csalás")

print ("\n8.feladat: A generált csapatnak, blokkoló kártya előállítása")
print ("")
def blokkolas (data): 
    '''
    Előállítani a megadott formátumot a 8-as feladatban
    data = csapat_mozgas
    '''
    import random
    def siker():
        '''
        mivel a feladat elég ellentmondásos,
        ezért input helyett simán random dobáltatom ki,
        amúgy while (1, vagy 2) ahol 1 befejezett, 2 befejezetlen lenne az input
        '''
        x = random.randint(1,2)
        if (x==1):
            return "befejezett"
        else:
            return "befejezetlen"
    new_file = open("blokkol.txt","a")
    for i in range(len(data)):
        new_file.write("\nindulási emelet: "+str (data[i][-2])+"\ncélemelet:       "+str(data[i][-1])+"\nfeladatkód:      "+str(random.randint(1,99))+"\nBefejezés ideje: "+str(data[i][0])+":"+str(data[i][1])+":"+str(data[i][2])+"\nSikeresség:      "+siker()+"\n-----------------------------")
    new_file.close()
blokkolas(csapat_mozgas)

