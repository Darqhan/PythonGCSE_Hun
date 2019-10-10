file = open ("musor.txt","r")
new_array = []
for item in file: 
    new_array.append(item.rstrip())
GLOBAL = new_array[0]
new_array = new_array[1:]

print ("\n1.feladat: fájl beolvasása és eltárolása")
print ("\n".join(new_array))
''' ********************************************************************************************** '''
print ("\n2.feladat: Melyik csatornán mennyi számot játszottak")
one, two, three = 0,0,0
for i in range (len(new_array)):
    if (new_array[i][0]=='1'):
        one +=1
    elif (new_array[i][0]=='2'):
        two +=2
    elif (new_array[i][0]=='3'):
        three +=3
print ("1-s csatornán: ", one," darab szám ment le.")
print ("2-s csatornán: ", two," darab szám ment le.")
print ("3-s csatornán: ", three," darab szám ment le.")
''' *************************************************************************************************'''
print("\n3.feladat: Mennyi idő telt el Eric Clapton szám vége közt")
elso_csatorna = []
for i in range (len(new_array)):
    if(new_array[i][0]=='1'):
        elso_csatorna.append(new_array[i])
prc, mprc = 0,0 
for i in range (len(elso_csatorna)):
    work_with = elso_csatorna[i].split(" ")
    prc += int(work_with[1])
    mprc += int(work_with[2])

def ido_valto (perc, masodperc):
    new_min = 0
    while masodperc > 60:
        new_min = int (masodperc/60)
        masodperc = masodperc%60
    new_hrs = 0
    new_min += perc
    while new_min > 60:
        new_hrs = int (new_min/60)
        new_min = new_min%60
    return (new_hrs,new_min, masodperc)

x = ido_valto(prc, mprc)
print (x[0]," óra", x[1]," perc ", x[2]," másodperc telt el a két szám közt.")
''' ********************************************************************************************************* '''
print ("\n3.feladat: Megtalálni Omega:Legenda számot, melyik csatorna, másik két adón adott számok")
for i in range (len(new_array)):
    x = new_array[i].split(" ")
    x = "".join(x[3:])
    if("Omega:Legenda" in x):
        omega_index = i 
        print (new_array[i][0], "-s adón volt hallható", i)

'''
A következő ciklusban minden adónak megkeresem a másodperc szerinti állását. 
'''
mpOne, mpTwo, mpThree = 0,0,0
for i in range(len(new_array)):
    mp = new_array[i].split(" ")
    mp = (int(mp[1])*60)+(int(mp[2]))
    if(new_array[i][0]=='1'):
        mpOne += mp
        new_array[i]=new_array[i]+" "+(str(mpOne))
    elif(new_array[i][0]=='2'):
        mpTwo += mp
        new_array[i]=new_array[i]+(" "+str(mpTwo))
    elif(new_array[i][0]=='3'):
        mpThree += mp
        new_array[i]=new_array[i]+ " "+ (str(mpThree))
    new_array[i]=new_array[i].split(" ")

print (new_array[omega_index])
print ("\nA másik két adón a legközelebbi szám:")
elso_csat = []
mas_csat = []
for i in range (len(new_array)):
    if(new_array[i][0]=='1'):
        elso_csat.append(new_array[i])
    elif(new_array[i][0]=='2'):
        mas_csat.append(new_array[i])


j=0
while (int(elso_csat[j][-1])<int(new_array[omega_index][-1])):
    j+=1
print (elso_csat[j-1])

k=0
while ((int(mas_csat[k][-1])<int(new_array[omega_index][-1]))and(k<len(mas_csat)-1)):
    k+=1
print (mas_csat[k-1])
print ("Ez a feladat sem jó, mert az egyik csatornán akkor már nincs is adás, vagy nem idő szerint, hanem hely szerint kéne egyezzenek.")
print ("\4.feladat: beolvasni karakter sort, és megnézni, hogy mely számcímekben szerepel")
szoveg = input("Mire keressek a számokban:")
''' ********************************************************************************* *'''
"""
Az egyik rádióműsorban sms-ben, telefonon, de akár képeslapon is kérhető szám. Ám a
sokszor csak odafirkált kéréseket olykor nehéz kibetűzni. Előfordul, hogy csak ennyi olvasható: „gaoaf”,
tehát ezek a betűk biztosan szerepelnek, mégpedig pontosan ebben a
sorrendben. Annyi biztos, hogy először a szerző neve szerepel, majd utána a szám címe.
Olvassa be a billentyűzetről a felismert karaktereket, majd írja a keres.txt állományba
azokat a számokat, amelyek ennek a feltételnek megfelelnek. Az állomány első sorába a
beolvasott karaktersorozat, majd utána soronként egy zeneszám azonosítója kerüljön! A
feladat megoldása során ne különböztesse meg a kis- és a nagybetűket!
"""
keres = []
for i in range(len(new_array)):
    x = new_array[i][3:-1]
    x = "".join(x)
    x = x.lower()
    x = x.replace(":","")
    x = x.replace("/","")
    keres.append(x)

keres_file = open ("keres.txt","a")
keres_file.write(szoveg)

for i in range(len(keres)):
    if (szoveg in keres[i]):
        w="\n"+str(i)
        keres_file.write(w)
keres_file.close()
''' *********************************************************************************** '''
print("\n4.feladat: külön fájl")
