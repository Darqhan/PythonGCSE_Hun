print ("\n2009.május - csokiautomata")
print ("\n1.feladat: beolvasni a vasarlas.txt., és csoki.txt-t")
def file_to_data(filename):
    '''
    file megnyitása, és listába töltése
    '''
    file = open(filename,"r")
    data = []
    for items in file:
        data.append(items.rstrip())
    return data
def str_to_int(data):
    '''
    A beolvasott fájlban "2 21 10" formában van tárolva az adat
    Nekem számok kellenek, hogy könnyen lehesenn a listával dolgozni
    Az első adat (a 0.) csak 1 szám, a többi már 3, space-szel választva
    '''
    data[0]=int(data[0])
    for i in range(1,len(data)):
        data[i] = data[i].split(" ")
        for j in range (len(data[i])):
            data[i][j] = int(data[i][j])
    return data
'''
A file_to_data() függvénnyel olvassuk be
mind a két file-t változóba, listaként
majd a str_to_int() függvénnyel konvertáljuk számmá
'''
vasarlas = str_to_int(file_to_data("vasarlas.txt"))
csoki = str_to_int(file_to_data("csoki.txt"))
#-------------------------------------
def csoki_ertekszamolos(data):
    '''
    A data = csoki nevű listaváltozó
    végig kell menni 1-től, annyiszor amennyi, a csoki[0] értéke, így a legegyszerűbb
    Az 1.és 2. szorzata adja a csoki darab*értéket
    Ezt tároljuk el egy változóban, hogy visszaadhassuk válaszként
    '''
    counter=0
    for i in range(1,data[0]+1):
        counter+=data[i][1]*data[i][2]
    return counter

print ("\n2.feladat: Milyen értékben van csoki az automtaában? ")
print("2.feladat válasz: Az automatában",csoki_ertekszamolos(csoki),"fabatka értékű csokoládé van")
#--------------------------------------
print ("\n3.feladat: Mely rekeszekből vásároltak?")

def vettek (vasarlas):
    '''
    Értelmezésem szerint a vasarlas listában:
    rekesz, darab 0,1 [0:2]
    ha darab>0 akkor rekesz
    utána duplikáltak levétele majd
    '''
    vettek_belole = []
    for i in range(1,vasarlas[0]):
        if (vasarlas[i][1]>0):
            if (vasarlas[i][0] not in vettek_belole):
                vettek_belole.append(vasarlas[i][0])
    vettek_belole.sort() 
    return vettek_belole
ezekbol_vettek = vettek(vasarlas)
#A kiíratás formátuma listából, szóközzel elválasztva, minden
print ("Az alábbi rekeszekből: ", *ezekbol_vettek, sep=" ")
#-----------------------------------------
print ("\n4.feladat: Bekérni a pénzt. Megnézni, melyik csokiból vehet 7-t. Melyik rekeszekből vehet")
def zsebpenz():
    '''
    Bekér a konzolról egy max 4 jegyű számot
    0-kat most nem ellenőrzünk
    visszaadja a zsebpénzt integer-ként
    '''
    my_input = ""
    while ((not my_input.isdigit())or(len(my_input)>4)):
        my_input = input("Add meg mennyi pénzed van: ")
    return int(my_input)

def tudok_venni (Anna_zsebpenze):
    '''
    ha van legalább 7 darab egy rekeszben, és a zsebpénz is elég 7-re
    akkor listához adni a rekesz számát
    '''
    mylist = []
    for i in range(1,csoki[0]+1):
        if(csoki[i][1]>=7):
            if(Anna_zsebpenze>=csoki[i][2]*7):
                mylist.append(csoki[i][0])
    return mylist
Anna_zsebpenze = zsebpenz()
lehetseges = tudok_venni(Anna_zsebpenze)
print ("Anna a zsebpénzéből, ami ", Anna_zsebpenze,"az alábbi rekeszekből tud 7 egyformát venni:",*lehetseges, sep=" ")
            
#---------------------------------------------
print ("\n5.feladat: Okos Peti a lehető legkevesebb pénzérmével fizetne \nRekesz sorszám, darabszám alapján kiírni mennyi érme kell")
#ezt is érdemesebb visszafelé megoldani: előbb egy fix számot szétszedni, előbb csak egy számmal
def ermeszamolos(number):
    '''
    100-tól 1-ig az érméket elosztja, és nem marad, akkor vége
    a maradék a következő osztandó szám
    result-ba tenni a mennyiszerxosztó szám, és számot(aktuális maradék)
    '''
    szam, mennyiszer,i = [number],[], 0
    result = []
    oszto_szamok = [100,50,20,10,5,2,1]
    for i in range(len(oszto_szamok)):
        mennyiszer.append(int(szam[i]/oszto_szamok[i]))
        szam.append(int(szam[i]%oszto_szamok[i]))
        result.append([szam[i],mennyiszer[i], oszto_szamok[i]])
    return result

def number_by_Peti():
    '''
    Peti adja meg a rekesz számát, 
    és hogy abból mennyit akar venni
    a csoki lista rekesszámából egységár x mennyiség = number
    '''
    rekesz = ""
    while ((not rekesz.isdigit())or(int(rekesz)>25)):
        rekesz = input("Add meg egy rekesz sorszámát: ")
    mennyiseg = ""
    while ((not mennyiseg.isdigit())or(len(mennyiseg)>3)):
        mennyiseg = input("Mennyit veszel belőle?")
    number = csoki[int(rekesz)][2]*int(mennyiseg)
    return number
#--------------------------
number = number_by_Peti()
print (number)
#--------------------------
#Bekért szám alapján, listában megkapom miből-mennyi kellett, és ezt íratom ki formátumban a lenti ciklussal
xyz = ermeszamolos (number)
for i in range(len(xyz)):
    if(xyz[i][1]!=0):
        print (xyz[i][2],"-s érméből",xyz[i][1],"darab kell")
#-------------------------
print ("\n6.feladat: Vásárlás listán végigmenni, ahol rekesz=7, ott megnézem mit fizetett")
arumennyiseg = 3
eredmeny = []
for i in range(1,vasarlas[0]):
    if(vasarlas[i][0]==7):
        darabszam = vasarlas[i][1]
        penz = ((1*vasarlas[i][2])+(2*vasarlas[i][3])+(5*vasarlas[i][4])+(10*vasarlas[i][5])+(20*vasarlas[i][6])+(50*vasarlas[i][7])+(100*vasarlas[i][8]))
        valos_ar = darabszam * 93 #itt kupuskáztam a listából a 7.rekesz egységárát
        print ("hanyadik sor: ",i,",db: ", darabszam,", fizetve: ", penz,"ennyibe került:", valos_ar, valos_ar<=penz)
        #újabb puskázás: a 7-s rekeszben 3 darab áru van
        print (arumennyiseg-darabszam)
        if ((arumennyiseg-darabszam >0) and (valos_ar<=penz)):
            eredmeny.append(str(i)+"\t"+str(darabszam)+"\n")
        elif (arumennyiseg-darabszam <=0):
            eredmeny.append(str(i)+"\t"+"kevés csoki\n")
        else:
            eredmeny.append(str(i)+"\t"+"nem volt elég pénz\n")

#Ezt kell kiíratni a feladatnak egy rekesz7.txt-be
def kiiratas ():
    new_file = open ("rekesz7.txt","a")
    for items in eredmeny: 
        new_file.write(items)
    new_file.close()
#lehetne még finomítani de a feladat is ez volt.         
