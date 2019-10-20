print("2015 érettségi")
print("\n1.feladat: beolvasni a tancrend.txt-t, listába")
def beolvas():
    lista = []
    file = open("tancrend.txt","r")
    for item in file:
        lista.append(item.rstrip())
    return lista
lista = beolvas()
print("\n2.feladat: Első tánc: ", lista[0],"utolsó tánc:",lista[-3])
print("\n3Mennyi pár sambá-zott?")
count=0
for item in lista:
    if(item=="samba"):
        count+=1
print(count," pár sambázott.")
print("\n4.feladat: Vilma mely táncokban szerepelt?", end=" ")
for i in range(len(lista)):
    if(lista[i]=="Vilma"):
        print(lista[i-1], end=" ")
#-------------------------F--------
def tanc_neve():
    szo=input("\n\nAdd meg mely táncot vizsgáljam:")
    return szo

tanc, tancolte = tanc_neve(), False
for i in range(len(lista)):
    if(lista[i]=="Vilma"):
        if(lista[i-1]==tanc): 
            print("\n","A "+lista[i-1]+" bemutatóján Vilma párja "+lista[i+1]+" volt.")
            tancolte = True
if(tancolte==False):
    print ("\nnem tancolt ilyet")
#-------------------------------
#5.feladat
lanyok, fiuk = [],[]
for i in range(1,len(lista),3):
    lanyok.append(lista[i])
lanyok = list(dict.fromkeys(lanyok))
lanyok.sort()
for j in range(2,len(lista),3):
    fiuk.append (lista[j])
fiuk = list(dict.fromkeys(fiuk))
fiuk.sort()
print (*fiuk, sep = ", ")
print (*lanyok, sep =", ")
#-------------------------------
print ("\n7.feladat: Legtöbbet szereplő lány és fiu.")
#len(fiuk)
szamol_ff=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(2,len(lista),3):
    for j in range(len(fiuk)):
        if (fiuk[j]==lista[i]):
            szamol_ff[j]+=1
legn = 0
for item in szamol_ff:
    if (item>legn):
        legn = item
legtobbet_szereplo_fiu  = []
for i in range(len(szamol_ff)):
    if(szamol_ff[i]==legn):
        legtobbet_szereplo_fiu.append(fiuk[i])
print ("A legtöbbet szereplő fiúk: ", end=" ")
print( *legtobbet_szereplo_fiu, sep=", ")
#---------------------------------
#len(lanyok)
szamol_l=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(lista),3):
    for j in range(len(lanyok)):
        if (lanyok[j]==lista[i]):
            szamol_l[j]+=1
legn = 0
for item in szamol_l:
    if (item>legn):
        legn = item
legtobbet_szereplo_lanyok  = []
for i in range(len(szamol_l)):
    if(szamol_l[i]==legn):
        legtobbet_szereplo_lanyok.append(lanyok[i])
print ("A legtöbbet szereplő lányok: ", end=" ")
print( *legtobbet_szereplo_lanyok, sep=", ")
