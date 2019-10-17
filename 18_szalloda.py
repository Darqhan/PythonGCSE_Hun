print ("\n2011 OKtóber Érettségi")
    #
   ##
  # #
    #   #
   ###

def elso_feladat():
    print ("\Első feladat : beolvasni a pitypang.txt-t")
    #'1 5 3 13 1 1 Huszar_Hajnalka'
    #'0 1 2 3  4 5  6'
        # [0] foglalás sorszáma
        # [1] szoba száma 
        # [2] érkezés
        # [3] távozás
        # [4] vendégek
        # [5] kér-e reggelit 1/0 = i/n
        # [6] név - 26 karakter max.  
    def file_beolvas():#sima beolvaás, rstrip-pel
        result,my_result = [],[]
        file = open("pitypang.txt","r")
        for lines in file:
            result.append(lines.rstrip())
        file.close()
        for lines in result[1:]:
            actual = lines.split()
            for i in range(len(actual)-1): 
                actual[i] = int(actual[i]) #A számok int formában legyenek
            my_result.append(actual)
        
        return my_result
    lista = file_beolvas()
    return lista
#Első feladat megoldása >> 
adat = elso_feladat()
     ###
    #  #
      #
     #  # #
    ####
def masodik_feladat():
    print ("\n2.feladat: Leghosszabb szállodai foglalás.")
    print ("NÉV - (érkezési nap sorszáma ) - eltöltött éjszakák sorszáma")
    #név[6](érkezés[2]) : távozás[3]-érkezés[2]
    legnagyobb = 0 #ne felejtsd el iniciálni amit hasonlítasz
    for i in range(len(adat)):
        if (legnagyobb < int(adat[i][3])-int(adat[i][2])):
            legnagyobb = int(adat[i][3])-int(adat[i][2])
            neve = adat[i][6]
            szoba = adat [i][2]
    print ("Leghosszabb szállodai foglalás:",neve,"(",szoba,")"," - ",legnagyobb)
masodik_feladat()
    ####
       #
    ####
       # #
    ####
def harmadik_feladat():
    # 2 ágy (1fő = 2fő) + 1 pótágy (2.000,-)    item[4]
    # reggeli: 1100,-/fő/nap (-1nap)            item[5]
    # távozás - érkezés = éjszakák száma        item[3] - item[2]
        # 01.01-04.30 9.000,- sorszám:  01-120 
        # 05.01-08.31 10.000,-sorszám:  121-213
        # 09.01-12.31 8.000,- sorszám:  214-366 
    print("\n3.feladat: szobaszám kiírása - szoba ára")
    data = adat
    osszes = 0

    for item in data:
        szemelyek_szama = item[4]
        reggeli = item[5]
        vendegejszaka = int(item[3])-int(item[2])
        tavasz,nyar,osz = 0,0,0 
        #print(*item, sep=" ")
        #print ("ennyi fő foglalt: ",szemelyek_szama)
        #print ("kértek reggelit:  ", reggeli)
        #print ("éjszakák száma:   ", vendegejszaka)
        for i in range(int(item[2]),int(item[3])):
            if (i<=120):
                tavasz +=1
            elif ((i>120)and(i<=213)):
                nyar +=1
            elif(i>213):
                osz += 1
        idoszak =""
        if (tavasz>0):
            idoszak+=" tavasz "+str(tavasz)
        if(nyar>0):
            idoszak+=" nyár "+str(nyar)
        if(osz>0):
            idoszak+=" ősz "+str(osz)
        #print ("idoszak:        ", idoszak,"\n")
        #print ("--------------")
        def fizet():
                potagy_ara = 0
                szoba_ara = tavasz*9000 + nyar*10000 + osz*8000
                if (int(szemelyek_szama)>2): 
                    potagy_ara = ((int(szemelyek_szama)-2) * 2000)*int(vendegejszaka)
                reggeli_ara = (int(reggeli)*1100)*int(vendegejszaka)
                szamla = szoba_ara + potagy_ara + reggeli_ara
                return szamla 
        #print ("fizetendő:",fizet())
        def kiirat():
            #kiírat és fizet
            file = open("bevetel.txt","a")
            fizetve = fizet()
            file.write(str(item[0])+":"+str(fizetve)+"\n")
            file.close()
            return fizetve
        osszes = osszes+kiirat()
    print("A szálloda teljes évi bevétele", osszes)
        
    
#harmadik_feladat(
    #
    #
    #   #
    #######
        # 
        #   #
        #
def negyedik_feladat():
    print ("\n4.feladat: Statisztika. Havonta, mennyi volt a vendégéjszaka száma")
    #vendégéjszaka = összes éjszaka ()* összes személy
    #vendegejszaka = int(item[3])-int(item[2])
    #szemelyek_szama = item[4]
    #Havi lebontás: start-end|||
    #JANUÁR 1-31 FEBRUÁR 32-59 MÁRCIUS 60-90 ÁPRILIS 91-120 MÁJUS 121-151 JUNIUS 152-181
    #JÚLIUS 182-212 AUGUSZTUS 213-243 SZEPTEMBER 244-273 OKTÓBER 274-304 NOVEMBER 305-334 DECEMBER 335-365
    def countable(erkezes, honap):
        '''
        Január esetén keressük meg mennyi nap van még hónap végén a foglalt éjszakákból. 
        '''
        i = 0
        while (erkezes<=honap): 
            i+=1
            erkezes+=1
        return i
    #---------------
    def egy_honapban(honap_utolso,honap_elso):
        vendegej_per_ho=0
        #---------------
        for item in adat:
            erkezes = int(item[2])
            tavozas = int(item[3])
            vendegejszaka = tavozas - erkezes
            szemelyek_szama = item[4]

            if ((erkezes<honap_utolso)and (erkezes>honap_elso)):
                if (tavozas<=honap_utolso):
                    vendegej_per_ho += vendegejszaka*szemelyek_szama
                    #print ("érkezés:",erkezes, "távozás:",tavozas, vendegejszaka*szemelyek_szama )
                else:
                    vendegej_per_ho += countable(erkezes, honap_utolso)
                    #print(erkezes,tavozas, countable(erkezes, honap_utolso))
        return vendegej_per_ho
    #---------------
    honap = [[1,31],[32,59],[60,90],[91,120], [121,151],[152,181],[182,212],[213,243],[244,273],[274,304],[305,334],[335,365]]
    for i in range (0,12):
        honap_elso = honap[i][0]
        honap_utolso = honap[i][1]
        print (i+1,".hónapban:", egy_honapban(honap_utolso, honap_elso))

negyedik_feladat()
    #####
    #
    #####
        # #
    #####
def otodik_feladat ():
    print("\n5.feladat: Bekér dátum(szám), vendégéj(szám); visszaad: szabad szoba : szabad / nem ")
    def mikortol():
        szam = "0"
        while ((int(szam)==0)or(int(szam)>365)):
               szam = input ("add meg a foglalás kezdetét (1-365):")
               if (szam==""):
                   szam ="0"
        return int(szam)

    def meddig (mikortol):
        szam = "0"
        while ((int(szam)>365)or(int(szam)<=mikortol)):
            szam = input ("add meg a foglalás kezdetét (1-365):")
            if (szam==""):
               szam ="0"
        return int(szam)

    mikortol = mikortol()
    meddig = meddig(mikortol) # bekért szám + mikor -1
    #------------------
    foglalt_szobak = []
    for item in adat: 
        erkezes = int(item[2])
        tavozas = int(item[3])
        vendegejszaka = tavozas - erkezes
        for i in range(mikortol, meddig):
            for j in range (erkezes,tavozas):
                if (i==j):
                    #print (mikortol,"-",meddig,":",erkezes,"-", tavozas, "szobaszám:", item[1])
                    foglalt_szobak.append(item[1])
    foglalt_szobak = list(dict.fromkeys(foglalt_szobak))
    foglalt_szobak.sort()
    return foglalt_szobak
      #  if ((mikortol<erkezes)and(meddig>=erkezes)):
         #   print ("10-14:",erkezes, tavozas)
#--------------------
x = otodik_feladat()
print ("Ennyi szoba szabad a megadott időben: ", 27-len(x))
    
