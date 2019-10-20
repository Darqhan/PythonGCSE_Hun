print ("\n1.feladat: Olvasd be a ip.txt-t listába")
def beolvas():
    file = open("ip.txt","r")
    lista=[]
    for item in file:
        lista.append(item.rstrip())
    return lista
lista = beolvas()
print ("\n2.feladat:",len(lista)," adatsor van a file-ban.")
print ("\n3.feladat: legalacsonyabb ip cím:")
eredmeny = []
for item in lista:
    item=item.split(":")
    atvaltas = []
    for szamok in item:
        atvaltas.append(int(szamok, 16))
        
    eredmeny.append(atvaltas)
eredmeny.sort()
legk=[]
for item in eredmeny[0]:
    legk.append(hex(item).split('x')[-1])
print (*legk,sep=":")
dokument, globegy, helyegy = 0,0,0 
for item in lista:
    if(item[:9]=="2001:0db8"):
        dokument +=1
    elif (item[:7]=="2001:0e"):
        globegy += 1
    elif((item[:2]=="fc")or(item[:2]=="fd")):
        helyegy+=1
print ("\n4.feladat. Mennyi darab van egyes ip címekből")
print ("dokumentációs címek:",dokument,"darab, globális egyedi címek:", globegy,"darab, helyi egyedi címek", helyegy," darab.")
#5.feladat: 18-nál több 0st kiírni fájlba
my_result = []
for item in lista:
    szamol=0
    for i in range(len(item)):
        if(item[i]=="0"):
            szamol+=1
    if(szamol>=18):
        my_result.append(str(lista.index(item))+" "+item)
file = open("sok.txt","w")
for item in my_result:
    file.write(item+"\n")
file.close()
print ("\n6.feladat: Bekér sorszám, hosszú - rövid alak egymás alá, bevezető 0 elhagyása")

def user_input(hossz):
    sorszam="-1"
    while ((int(sorszam)<0)or(int(sorszam)>hossz)):
        sorszam=input("Kérek egy sorszámot: ")
        if(sorszam==""):
            sorszam="-1"
    return int(sorszam)
newindex=user_input(len(lista))
print (lista[newindex])

ipcim = lista[newindex]
ipcim = ipcim.split(":")
ipcim_egysz = []
for item in ipcim:
    vizsgalt = item
    while((len(vizsgalt)>1)and(vizsgalt[0]=="0")): 
        vizsgalt = vizsgalt[1:]
    ipcim_egysz.append(vizsgalt)
print (*ipcim_egysz, sep=":")

ipcim_megegysz = []
for item in ipcim:
    vizsgalt = item
    while((len(vizsgalt)>0)and(vizsgalt[0]=="0")): 
        vizsgalt = vizsgalt[1:]
    ipcim_megegysz.append(vizsgalt)
egyik, masik = 0,0
for i in range(8):
    egyik+=len(ipcim_egysz[i])
    masik+=len(ipcim_megegysz[i])

if(egyik==masik):
    print ("Nem rövidíthető tovább")
else: 
    print (*ipcim_megegysz, sep=":")
