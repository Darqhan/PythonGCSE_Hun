print ("\n2.feladat: Beolvasni a jarmu.txt állományt, listába")
def beolvas():
    file = open("jarmu-1.txt","r")
    lista=[]
    for item in file:
        item = item.rstrip()
        item = item.split()
        item[0]= int(item[0]) # vegyes typusú, kell a szám később
        item[1]= int(item[1])
        item[2]= int(item[2])
        lista.append([item[0],item[1],item[2],item[3]])
    return lista
lista = beolvas()
# lista[0] = óra
# lista[1] = perc
# lista[2] = másodperc
# lista[3] =
print ("\n2.feladat: Mennyi időt dolgoztak ")
legn, legk = 0,10 
for item in lista:
    if(legn < item[0]):
        legn = item[0]
    elif(legk>item[0]):
        legk = item[0]
print("Az ellenőrzést végzők ",legk,"-tól ",legn,"-ig dolgoztak", legn-legk+1," órát")
print ("\n3.feladat: Adott órában először elhaladt jármű")
eredmeny = []
for i in range(legk,legn+1):
    aktual = []
    for item in lista:
        if (item[0]==i):
            aktual.append(item)
    eredmeny.append(aktual[0])
for item in eredmeny:
    print(item[0],"óra:",item[-1])
lh, result = 0,0
for i in range(1,len(lista)):
    elso =lista[i-1][1]*60+lista[i-1][2]
    masodik = lista[i][1]*60+lista[i][2]
    if(lista[i-1][0]<lista[i][0]):
        hossz = 3600-elso+masodik
    else:
        hossz = masodik-elso
    if (hossz > lh):
        lh = hossz
        result=i
    #print (lista[i-1][:3],lista[i][:3], hossz,lh)

print ("\n4.feladat: Busz, Motor, Kamion számlálás")
busz, motor, kamion=0,0,0
for item in lista:
    if (item[-1][0]=="B"):
        busz+=1
    elif(item[-1][0]=="M"):
        motor+=1
    elif(item[-1][0]=="K"):
        kamion+=1
print ("Busz:",busz,"Motor:",motor,"Kamion:",kamion,"össz:",len(lista))

print ("\n5.feladat: Mettől meddig tartott a leghosszabb autómentes időszak?")
print (*lista[result-1][:3], sep=":",end=" ")
print ("-",end=" ")
print(*lista[result][:3], sep=":")
print ("\n6.feladat: Hiányos rendszám bekérés")
#for item in lista:
#    print (item[-1])

def keresett():
    rendszam = input ("Adja meg a 7 karakternyi rsz-t, *gal, ahol ismeretlen:")
    return rendszam


#rendszam = "FY*****"
rendszam = keresett()
szamolos = []
for i in range(len(rendszam)):
    if(rendszam[i]!="*"):
        #szamolos listába tenni [index, betű]
        szamolos.append([i,rendszam[i]])
print("ezt keressük:",szamolos)
#-----------
ujlista = []
for item in lista:
    egyezett = []
    for i in range(len(szamolos)):
        index = szamolos[i][0]
        betu = szamolos [i][1]
        if(item[-1][index] == betu):
            egyezett.append(1)
    if (egyezett !=[]): 
        ujlista.append([egyezett,item[-1]])
talalt = []
for item in ujlista:
    if(len(szamolos)==(len(item[0]))):
        talalt.append(item)
if (len(talalt)==0):
    print ("nincs ilyen a nyilvántartásban")
else:
    for thingz in talalt:
        print (thingz[-1])
print ("\n7.feladat: Közúti ellenőrzés")
# 5 perc 1 ellenőrzés = 5*60 = 300 másodperc
# az elsővel kezdik, +300, ha item>= akkor ellenőrzs += időpont
ellenorzott,kimenet = 0, []
for item in lista:
    if(item[0]*3600+item[1]*60+item[2] >= ellenorzott+300 ): 
        ellenorzott = item[0]*3600+item[1]*60+item[2]+300
        kimenet.append (item)
eredmeny = []
for item in kimenet:
    soronkent,vegul = "",""
    for i in range(3):
        if (item[i]<10):
            soronkent+="0"+str(item[i])+" "
        else:
            soronkent+=str(item[i])+" "
    vegul += soronkent+item[-1]
    eredmeny.append(vegul+"\n")
file = open("vizsgalt.txt","w")
for item in eredmeny:
    file.write(item)
file.close()
