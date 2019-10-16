print ("\n1.feladat: Olvassuk be a file-t ")

def beolvasas():
    lista = []
    file = open("telkek.txt","r")
    for lines in file:
        lista.append(lines.rstrip())
    for i in range(1,len(lista)):
        lista[i]=lista[i].split(" ")
        for j in range(len(lista[i])):
            lista[i][j]=int(lista[i][j])
    return lista[1:]
lista = beolvasas()
#------------------------------------------
print ("\n2.feladat: Hány métert kell gyalogolni, aki körbegyalogolná a 2 utcát?")
'''
80 méter a két utca magassága
A szélességet a páros utca sum(szélesség) fogja adni
a megoldás = (80+szél)x2 lesz
'''
def joletsor(data):
    '''
    mivel többször kéri jólétsort számolni
    ezért külön generálom egy fny-nyel az eredeti listából
    '''
    joletsor=[]
    for i in range(len(data)):
        if(data[i][0]%2==0):
            joletsor.append(data[i])
    return joletsor
joletsor = joletsor(lista)

def szelesseg(data):
    osszeg = 0
    for i in range(len(data)):
            osszeg += data[i][1]
    return osszeg
print ("Válasz:", szelesseg(joletsor)," métert kell.")
#-------------------------------------------
print("\n3.feladat: Jólétsor(páros HSZ) 20m> telek szélest kiíratni")

def utcafront(data):
    result=0
    for i in range(len(data)):
        if data[i][1]<=20:
            result+=1
    return result

print("Jólétsoron",utcafront(joletsor),"háznál kell teljes utcafrontot beépíteni.")
#-----------------------------------------------------------------------------
print ("\n4.feladat: Gazdagsoron a legnagyob/legkisebb területű telek, mennyi ház vanköztük, házszámuk, területük")
def gazdagret(data):
    '''
    mivel többször kéri Gazdagrétet számolni
    ezért külön generálom egy fny-nyel az eredeti listából
    '''
    gazdagret=[]
    for i in range(len(data)):
        if(data[i][0]%2!=0):
            gazdagret.append(data[i])
    return gazdagret
gazdagret = gazdagret(lista)
#---------- 
def teruletek(data):
    terulet = []
    for i in range(len(data)):
        terulet.append(data[i][1]*data[i][2])
    return terulet

terulet = teruletek(gazdagret)

def koztes_telkek(data, LN, LK):
    counter=0
    for i in range(len(data)):
        if((LN>data[i][0])and(LK<data[i][0])): 
            counter+=1
    return counter
print ("Legnagyobb telek HSZ:",gazdagret[terulet.index(max(terulet))][0],"terület:", max(terulet))
print ("Legkisebb telek HSZ:", gazdagret[terulet.index(min(terulet))][0],"terület:",min(terulet))
koztes = koztes_telkek(gazdagret,gazdagret[terulet.index(max(terulet))][0], gazdagret[terulet.index(min(terulet))][0])
print("Köztük",koztes,'telek van')
#------------------------------------------------------------------------------
print ("\n5.feladat: Adózás Gazdagsoron")
#0-700 nm : 51 Fabatka / nm
#701-1000 nm: mint előbb/nm (vagyis 700x51 alap) + 39 Fabatka / nm
#1001+ nm: 700x51 + 300x39 + 200 Fabatka
#1-15m széles vagy 1-25 m hosszú = 0,8 szorzó
# 100 Fabatkás kerekítés
def adozas():
    szorzo, adoterheles,osszeg = [],[],[]
    fizetni =0
    for i in range(len(gazdagret)):
        fizetni =0
        if (terulet[i]<701):
            fizetni = terulet[i]*51
        elif(terulet[i]>700):
            if (terulet[i]<=1000):
                fizetni = ((terulet[i]-700)*39) +(700*51)    
            else:
                fizetni = ((terulet[i]-700)*39) +(700*51) +200   
        if ((gazdagret[i][1]<=15)or(gazdagret[i][2]<=25)):
            szorzo.append(0.8)
        else:
            szorzo.append(1)
        fizetni = int(fizetni*szorzo[i])
        if(fizetni%100>=50):
            fizetni = int(fizetni/100)*100+100
        else:
            fizetni = int(fizetni/100)*100
        osszeg.append(fizetni)
    return osszeg
osszeg = adozas()
osszeg = sum(osszeg)
print ("Gazdagsor önkormányzatának a bevétele: ", osszeg," Fabatka")
#-----------------------------------------------------------------------------
print("\n6.feladat: Jólétsor utolsó 3 telke. HSZ, telek távolsága, csökkenő sorr.")
joletsor.sort()
print ("Jólétsor 3 legtávolabbi telke (HSZ):", joletsor[-1][0], joletsor[-2][0], joletsor[-3][0])
def harom_tav(data):
    kezdo_tav = 0
    for i in range(len(data)-3):
        kezdo_tav+= (data[i][1])
    return [kezdo_tav, kezdo_tav+data[-3][1],kezdo_tav+data[-2][1]]

print ("Távolságuk az utca elejétől:", *harom_tav(joletsor), sep=" ")
#-----------------------------------------------------------------------------
print ("\n7.feladat: Jólétsor telkeinek a hosszúsága")
# hosszúság meghatározása Jólétsor: szembe fekvő telek t1+t2+10 = 80
# joletsor.csv-be kiírni
# HSZ;szélesség;hossz



