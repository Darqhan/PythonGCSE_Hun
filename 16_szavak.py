print("\n2011 május")
#print("1.feladat: Szót bekérni, és kiírni van/nincs magánhangzó benne")
def read_from_file():
    file = open("szoveg.txt","r")
    lista = []
    for item in file:
        lista.append(item.rstrip())
    file.close()
    return lista
#A listát több feladatban is használom
lista = read_from_file()

def elso_feladat():
    def szot_bekerni(): 
        szo = ""
        while((len(szo)<=1)or(len(szo)>20)):
            szo = input("1.feladat. Adjon meg egy szót: ")
        return szo
    szo = szot_bekerni()
    print ("A megadott szó: ",szo)
#_____________________
    def maganhangzo(szo):
        betuk = list(szo)
        van_benne = 0
        for item in betuk:
            if (item in "aeoui"):
                van_benne +=1
        if(van_benne>0):
            return "Van benne magánhangzó"
        else:
            return "Nincs benne magánhangzó"
    print (maganhangzo(szo))
#elso_feladat()
def masodik_feladat():
    print("\n2.feladat: melyik a leghosszabb szó a szoveg.txt-ben, mennyi karakter")
    def leghosszabb():
        leghosszabb = ""
        for item in lista:
            if(len(leghosszabb)<len(item)):
                leghosszabb=item
        return leghosszabb

    lh = leghosszabb()
    print("Válasz: ",lh, len(lh))

#masodik_feladat()

def harmadik_feladat():
    print ("\n3.feladat: Megkeresni: -- ahol tobb a mgh -- szóközzel kiírni ")
    print ("Utána talált szó / összes szó: x,xx %")
    def mgh_msh():
        eredmeny = []
        for i in range(len(lista)):
            betuk = list(lista[i])
            mgh, msh = 0,0
            for item in betuk:
                if (item in "aeiou"):
                    mgh+=1
                else:
                    msh+=1
            if (mgh>msh):
                eredmeny.append(lista[i])
        return eredmeny
    mgh_szavak = mgh_msh()
    print (*mgh_szavak, sep=" ")
    arany = len(mgh_szavak)/len(lista)*100
    print (len(mgh_szavak),"/",len(lista),":","%.2f" % arany,"%")
#harmadik_feladat()
def negyedik_feladat():
    print("\n4.feladat. Szólétra. a, Kiszedni az 5 betűs szavakat b, bekérni 3 betűst")
    print ("c, megkeresni azokat az ötbetűseket, aminek ez a 3 betű a közepe")
    def otbetus():
        otbetus=[]
        for i in range(len(lista)):
            if (len(lista[i])==5): 
                otbetus.append(lista[i])
        return otbetus
    otbetus = otbetus()
    '''
    def szot_bekerni(): 
        szo = ""
        while((len(szo)<3)or len(szo)>3):
            szo = input("1.feladat. Adjon meg egy szót: ")
        return szo
    szo = szot_bekerni()    
    '''
    teszt = "obo"
    def tesztel ():
        result=[]
        for item in otbetus:
            if(teszt in item):
                result.append(item)
        return result
    t_list= tesztel()
    print(*t_list, sep=" ")
#negyedik_feladat()
def otodik_feladat():
    print("\n5.feladat: Ötbetűs szavakból, kicsoportosítani a 3betűs egyformákat")
    print ("kiíratni őket a letra.txt-be, külön sorban, két kül. közt \\n legyen")
    #_________________________
    def otbetus():
        otbetus=[]
        for i in range(len(lista)):
            if (len(lista[i])==5): 
                otbetus.append(lista[i])
        return otbetus
    otbetus = otbetus()
    #print(otbetus[:10])
    #___________________________
    def harombetusek(data):
        harom = []
        for i in range(len(data)):
            harom.append(data[i][1:4])
        return harom
    h = harombetusek(otbetus)
    h=list(set(h))
    h.sort()
    #___________________________
    def letra():
        def index_re(keresem):
            talalt_index = []
            for i in range(len(otbetus)):
                if(keresem in otbetus[i]):
                    talalt_index.append(i)
            return talalt_index
        #_________________
        result=[]
        for i in range(len(h)): 
            result.append(index_re(h[i]))
        return result 
    eredmeny=letra()
    # fenti két fny, eredmény 0, h0++, és otbetus index = eredmeny 0

    def kiiratas():
        file = open("letra.txt","w")
        for i in range(len(eredmeny)):
            if(len(eredmeny[i])>1):
                for j in range(len(eredmeny[i])):
                    file.write(otbetus[eredmeny[i][j]]+"\n")
                file.write("\n")
        file.close()
    kiiratas()

otodik_feladat()
#annyi nem világos hogy x+aaa+x vagy xx+aaa/aaa+xx is jó-e? 
