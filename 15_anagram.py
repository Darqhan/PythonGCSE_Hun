print ("\n1.feladat: Bekérni egy szót, és kiírni karaktereket és milyen hosszú")
def szo_bekerese ():
    '''
    konzolos adatbekérés 2-30 közti szöveget kérünk be
    '''
    szo=''
    while (len(szo)>30)or(len(szo)<2):
        szo = input ("Adja meg a szöveget:")
    return szo
def karakterek(szo):
    '''
    Két lista elemeit kell összehasonlítani,
    és ha egyezés van, akkor az elemhez rendelt számlálót növelni+1
    ehhez a karaktereket kell kiszedni, duplikátum nélkül
    lehetne egy másik algoritmussal, de van erre függyvény
    '''
    #duplikátumok kihagyása, a lista készletét kapjuk vissza apafa > paf
    karakter = ''.join(set(szo))
    #ide tesszük majd a az eredményt: ['a',1] formátumban
    result = []
    for elem in karakter:
        counter = 0
        for i in range(len(szo)):
            if (elem == szo[i]):
                counter +=1
        result.append([elem, counter])
    return result
def elso_feladat(szo):
    '''
    írassuk ki szépen a karakterek() eredményét a képernyőre
    '''
    result = ''
    for i in range(len(szo)):
        for elem in szo[i]:
            result += str(elem)+" "
        result += "\n"
    return result
#----------------------------------------------------------
#konzolos input
#szo = szo_bekerese()
szo = "ssd"
print ("A bekért szó:",szo,"hossza: ", len(szo))
#szétszedni karakterekre, és azokból mennyi van
karakter = karakterek(szo)
#lista sorbarendezése abc szerint
karakter.sort()
print ("ezek a karakterek vannak benne, ennyiszer: ")
print(elso_feladat(karakter))
#----------------------------------------------------------
print ("\n2.feladat: Beolvasni a szotar.txt-t szotar listába")
def beolvas():
    file = open("szotar.txt","r")
    lista = []
    for items in file:
        lista.append(items.rstrip())
    return lista
szotar = beolvas()
#--------------------------------------------------------
print ("\n3.feladat/minden szó karakterét abc-be tenni, majd kiírni abc-txt-be")

def atiratas (data):
    result = []
    def split(word):
        '''
        A beépített .split(par) fny csak szeparátorral működik
        be kell járni a stringet és úgy listába dobni minden elemet
        '''
        return [char for char in word]
    def characters(word):
        '''
        Szó szétszedése listába
        list rendezése
        lista szövegbe fűzése
        '''
        karakter = split(word)
        karakter.sort()
        karakter = "".join(karakter)
        return karakter

    
    for i in range(len(data)):
        '''
        A stringet-t betűire szedni, listában
        utána abc-be tenni a listát
        majd a listát újra stringgé tenni
        '''
        a = data[i]
        a = characters(a)
        result.append(a)
    return result
def fileba (data):
    '''
    itt íratom ki a file-ba a listát elemenként megegyező sorrendben
    '''
    file = open ("abc.txt","w")
    for item in data:
        file.write(item+"\n")
    file.close()
harmadik = atiratas(szotar)
fileba(harmadik)
#--------------------------------------------------------------------
print ("\n4.feladat: Bekérni 2 szót, Anagramma/nem")
#szo_bekeres() fny-nyel kell bekérni konzolról feladat szerint
elso_szo = "baba"
masik_szo = "abba"
def szavak(szo):
        '''
        Előző feladatban felhasznált fny-t írom újra
        '''
        def split(word):
            return [char for char in word]

        karakter = split(szo)
        karakter.sort()
        karakter = "".join(karakter)
        return karakter
def is_Anagram(a,b):
    if (a==b):
        print ("Anagramma")
    else:
        print("Nem anagramma")
print (elso_szo, "anagrammája: ", szavak(elso_szo),"; ", masik_szo,"anagrammája",szavak(masik_szo))
is_Anagram(szavak(elso_szo), szavak(masik_szo))
#--------------------------------------------------------------------
print ("\n5.feladat: Bekérni egy szót, a szótárból kikeresni az anagrammáit.")
print ("találatokat egymás alá kiírni, vagy nincs a szótárban anagramma")
#hadartam, ez lesz a bekért szó
proba = szotar[5]
#ezt kell anagramma formába tenni és az abc.txt-ben kikeresni
print ("A szavam:",proba,"Anagramma: ", szavak(proba))
#Az abc.txt az a harmadik nevű listában van tárolva

def is_Anagramma():
    result = []
    for i in range(len(harmadik)):
        vizsgalt = szavak(proba)
        if (vizsgalt == harmadik[i]):
            #abc, szotar és harmadik sorrendje megegyezik
            result.append(szotar[i])
    if (len(result)==0):
        print ("Nincs a szótárban angramma")
    else:
        for i in range(len(result)):
            print(result[i])
        
print("Megoldás:")
is_Anagramma()
#--------------------------------------------------------------------
print("\n6.feladat: Szotar.txt-ben melyik a leghosszabb szó. Anagramma szerint sorrendben")
def lh_szoveg():
    '''
    először kikeresem melyik szöveg a leghosszabb(melyik utolsó szó a listában)
    '''
    leghosszabb = ""
    for i in range(len(szotar)):
        if (len(leghosszabb)<=len(szotar[i])):
            leghosszabb = szotar[i]
    return(leghosszabb)

def lh_szavak(lh):
    '''
    Akik ugyanolyan hosszúak mint a legutolsó leghosszabb szó
    azok kerüljenek egy listába
    '''
    result = []
    for i in range(len(szotar)):
        if(len(lh) == len(szotar[i])):
            result.append(szotar[i])
    return result

# egy listát kapok vissza a leghosszabb szavakkal, még rendezni kell őket
eredmeny = lh_szavak(lh_szoveg())

def rendezd(): 
    result=[]
    for i in range(len(eredmeny)):
        result.append ([szavak(eredmeny[i]), eredmeny[i]])
    return result    

def kiiratas_kepernyore():
    result = []
    for i in range(len(vegso)):
        result.append(vegso[i][1])
    result.sort()
    for item in (result):
        print (item)
vegso = rendezd()
vegso.sort()
kiiratas_kepernyore()
#--------------------------------------------------------------------------
print ("\n7.feladat: rendezés 3 feltétel szerint:")
print("---Egyforma hosszú és angramma: 1 sorba, szóközzel")
print ("--- Egyforma hosszú és nem anagramma: külön sorba")
print ("---Nem ugyanolyan hosszú és nem anagramm: külön sorba, üres sorral")
#először keressük ki az anagrammákat, és zárjuk list-in-list-be
#szotar, harmadik >>
def hosszak():
    '''
    ezzel szétszedem a listámat INDEX alapján, csoportokra
    0-30 közt vizsgálom, kinek annyi a hossza
    az egy allistába kerül, a üres lista nem kerül be !=[]
    '''
    hossz =0
    result=[]
    while(hossz<30):
        darab = []
        for i in range(len(harmadik)): 
            if (len(harmadik[i]) == hossz):
                darab.append(i)
        if (darab!=[]):
            result.append(darab)
        hossz+=1
    return result

def hosszak_neve(data):
    '''
    A hosszak() eredményét fejti vissza INDEX-ből SZAVAK-ra
    Hossz szerint maradnak alcsoportokban (array-in-array)
    '''
    result = []
    for i in range(len(data)):
        darab=[]
        for j in range(len(data[i])):
            darab.append(szotar[data[i][j]])
        result.append(darab)
    return result
#Ebben a változóban az egyforma hosszúak lesznek eltéve array-in-array, index száma
indx_hossz = hosszak()
hosszusagok = hosszak_neve(hosszak())
# list-in-list-in-list lesz belőle
def atalakito(data,x):
    '''
    ez fésüli össze a számokat
    ilyen formában: [['aajk', 'ajak'], ['aajk', 'ajka']... 
    '''
    my_result = []
    for i in range(len(data)):
        current_index = indx_hossz[x][i]
        my_result.append([harmadik[current_index],data[i]])
    my_result.sort()
    return my_result
#--------

def kiiratos (data): 
    hasonl=data[0][0]
    osszes = []
    for i in range(0,len(data)):
        if(data[i][0]==hasonl):
            darab = data[i][1]
            #print(data[i][1])
        else:
            darab = "\n"+data[i][1]
            hasonl = data[i][0]
            print ("--")
            #print(data[i][1])
        osszes.append(darab)
    for elem in osszes:
        print(elem, end=" " )
    return osszes
to_file = []
for i in range(len(hosszusagok)): 
    my_result = atalakito(hosszusagok[i],i)
    to_file.append(kiiratos(my_result))
#már csak ki kell iratni +1 \n-nel:
new_file = open("rendezve.txt","a")
for i in range(len(to_file)):
    for j in range(len(to_file[i])): 
        new_file.write(to_file[i][j]+" ")
    new_file.write("\n\n")
new_file.close()
    
    
    
