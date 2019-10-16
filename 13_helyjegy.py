def beolvasas():
    data = []
    file = open("eladott.txt","r")
    for lines in file:
        data.append(lines.rstrip())
    for i in range(len(data)):
        data[i]=data[i].split(" ")
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    return data
lista = beolvasas()
print ("\n1.feladat: File beolvasása, eltároltam a lista nevű tömbben")
#---------------------------------------------
print ("\n2.feladat:: legutolsó jegyvásárló ülése, távolság")
print (lista[-1][0], "-s ülésen", abs(lista[-1][2]-lista[-1][1])," km-t tett meg")
#---------------------------------------------
print("\n3.feladat: kik utazták végig a teljes utat! utasok sorszáma kell (lista[i])")
def vegigutaztak():
    result = ''
    for i in range(len(lista)):
        if ((lista[i][1]==0) and (lista[i][2]==172)):
            result+=str(i)+' '
    return result
print("ezek az utasok utazták végig:", vegigutaztak())
#----------------------------------------------
print ("\n4.feladat: meghatározni a teljes jegybevételt")
def kerekites(szam):
    '''
    minden megkezdett 10 km 71 ft
    de nem szorozhatom csak úgy össze, mert 5-re meg 10-re kerekít a sofőr
    ezért kell ez a kis sniplet
    '''
    kerekitendo = int(szam%10)
    if (str(kerekitendo) in '3467' ):
        kerekitendo = 5
    elif (str(kerekitendo) in '12'):
        kerekitendo = 0
    elif (str(kerekitendo)in'89'):
        kerekitendo = 10
    szam = (szam-(szam%10))+kerekitendo
    return szam
    
def teljes_jegybevetel():
    '''
    fele ilyen hosszan elegánsabb lenne
    de láttatni akarom a lépéseket
    '''
    utazott_km, jegy_km = [],[]
    for i in range(1,len(lista)):
        utazott = lista[i][2]-lista[i][1]
        #az utazott_km változó elhagyható, csak ellenőrzés miatt hagytam itt
        utazott_km.append(utazott)
        if (utazott%10==0):
            jegy_km.append(int(utazott/10))
        else:
            jegy_km.append((int(utazott/10)+1))
    for i in range(len(jegy_km)):
        #ezt is meg lehetne lépni az előző ciklusban
        jegy_ara = jegy_km[i]*71
        jegy_km[i] = kerekites(jegy_ara)
    return jegy_km

jegybevetel = sum(teljes_jegybevetel())
print (jegybevetel,",- a teljes bevétel a járaton a társaság számára")
#---------------------------------------------------------------------
print("\n5.feladat: végállomás előtti állomáson mennyien szálltak le és fel")
print ("nem egyértelmű feladat, de akkor keressük meg a max-10 km körüli értékeket")
for i in range(1,len(lista)):
   # if(lista[i][2]==172):
   if(lista[i][1]>160):
        print ("leszálló", lista[i])
#----------------------------------------------------------------------
print ("\n6.feladat: Hány helyen állt meg a busz, az indulás és cél közt")
def megallok_szam():
    '''
    Először szedjük ki a megállókat
    utána szedjük a listát sorrendbe
    vegyük ki a duplikátumokat
    a lista hossza a válasz a kérdésre
    
    '''
    megallok = []
    for i in range(1,len(lista)):
        megallok.append (lista[i][1])
    megallok.sort()
    megallok = list(dict.fromkeys(megallok))
    return len(megallok)
print ("Megállók száma:", megallok_szam())
#---------------------------------------------------------------------
print("\n7.feladat: a, Kérjük be a km-t amit vizsgálunk  b, ülések sorszámában kiírni")
def adat_bekeres():
    '''
    adatbekérés konzolról
    kizárva hogy ABC, 0, vagy 172-től nagyobb szám
    '''
    my_input = input("1-172 közt adj egy állomást: ")
    while((my_input.isalpha())or(int(my_input)>172)or(int(my_input)==0)): 
        my_input = input("Helló, adj egy számot 1-172 közt")
    return int(my_input)
my_input = adat_bekeres()

def helyzet(milestone):
    '''
    milestone = my_input
    Ettől a helytől kisebb leszálló, de nagyobb felszálló
    ülés, felszáll, leszáll
    milestone < leszall, milestone >=  felszall
    továbbra sem világos mit ért megálló alatt a feladat
    '''
    result = []
    for i in range(1,len(lista)):
        #ezt is lehet rövidebben
        felszall = lista[i][1]
        leszall = lista[i][2]
        if((leszall>milestone)and(felszall<=milestone)):
            x = lista[i]
            x.append(i)
            result.append(x)
    return result

eredmeny = (helyzet(my_input))
#az első érték az ülésszám, ami alapján sorba kell rendezni
eredmeny.sort()

def ulesek(data):
    '''
    végig kell menni a 48 ülésen, ahol nincs egyezés: üres
    ahol van, ott a székszám, utasszám
    végén listát kiadni mind a 48 ülésre
    '''
    new_data=[]
    for j in range(1,49):
        rovid_szoveg = str(j)+".ülés: üres\n"
        new_data.append(rovid_szoveg)
        for i in range(len(data)):
            if(data[i][0]==j):
                szoveg = str(data[i][0])+" ülésen a "+str(data[i][-1])+". utas\n"
                new_data[j-1]=szoveg
    return new_data

hetes = ulesek(eredmeny)

def array_to_file(data):
    '''
    listát kiíratni file-ba
    soronként = \n 
    '''
    new_file = open("kihol.txt","w")
    for items in data:
        new_file.write(items)
    new_file.close
    
array_to_file(hetes)

