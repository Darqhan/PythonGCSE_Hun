def mpbe(o,p,mp):
    return 3600*o+60*p+mp
def beolvas():
    file = open("hivas.txt","r")
    lista = []
    for item in file:
        #szétszedni space-közt, majd integerré tenni
        elem=(item.split())
        elem = list(map(int, elem))
        lista.append(elem)
    return lista
lista=beolvas()
szamol = []
for item in lista:
    szamol.append(item[0])
#szamol = az órák neveit adja vissza, a lista alapján
szamol = list(dict.fromkeys(szamol)) 
ennyiszer = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(szamol)):
    item = szamol[i]
    for elem in lista:
        if (item==elem[0]):
            ennyiszer[i]+=1
print("\n3.feladat")
for i in range(len(szamol)):
    print (szamol[i]," óra ", ennyiszer[i], " hívás")
print ("\n4.feladat: A leghosszabb ideig a vonalban lévő hívó")

legh,indx = 0,0
for i in range(len(lista)): 
    kezdet = mpbe(lista[i][0], lista[i][1], lista[i][2])
    vege = mpbe (lista[i][3], lista[i][4], lista[i][5])
    if (legh <vege-kezdet):
        legh = vege-kezdet
        indx = i
print (indx,". sorban szerepel és a hívás hossza: ",legh,"másodperc")
#-  ------------------
#5.feladat
def ido_bekeres():
    ora="0"
    perc="60"
    mp="60"
    while ((int(ora)<lista[0][0])or(int(ora)>lista[-1][0])or(int(ora)>11)or(int(ora)<8)):
    # 6-18 közt lehet >> nem igaz, 8.00-12.00-ig fogad hívást
        ora = input("óra: ")
        if(ora==""):
            ora = "0"
    while (int(perc)>59):
        perc = input("perc: ")
        if(perc==""):
            perc = "0"
    while (int(mp)>59):
        mp = input("másodperc: ")
        if(mp==""):
            mp = "0"
    ido = [int(ora),int(perc),int(mp)]
    return ido
idopont=ido_bekeres()
idopont_ertek = 3600*idopont[0]+60*idopont[1]+idopont[2]
print (*idopont, sep=":")
print (idopont_ertek)
job_done = 0
varakozik = -1
for item in lista:
    kezdo = item[0]*3600 + item[1]*60 + item[2]
    vegzo = item[3]*3600 + item[4]*60 + item[5]
    if ( (kezdo<idopont_ertek  )and (vegzo>idopont_ertek)):
        print ("várt & beszélt:",item)
        varakozik +=1
    elif((kezdo<idopont_ertek)and(vegzo<=idopont_ertek)):
        job_done+=1
print ("ennyivel beszélt eddig:", job_done)
print ("ennyi várakozik: ", varakozik)
def hossza(ora,perc,mp):
    return ora*3600+perc*60+mp
elkezdte = hossza(lista[job_done-1][0],lista[job_done-1][1],lista[job_done-1][2])
befejezte = hossza(lista[job_done-1][3],lista[job_done-1][4],lista[job_done-1][5])
print ("utoljára beszélt: ", lista[job_done-1], "azonosító:", job_done, "időtartam:", befejezte-elkezdte, " másodperc")
print ("\n7.feladat: Az összes sikeres hívás: itt nm vok biztos a logikában")
munkaidoben=[]
for i in range(1,len(lista)):
    item = lista[i]                                         #adott elem, amit vizsgálok
    if ((lista[i][3]>=8)and(lista[i][0]<12)):
        munkaidoben.append(item)
sikeres = []
for i in range(0,len(munkaidoben)):
    v_kezdo = hossza (munkaidoben[i][0],munkaidoben[i][1],munkaidoben[i][2])  #vizsgált elem kezdete
    v_vegzo = hossza (munkaidoben[i][3],munkaidoben[i][4],munkaidoben[i][5])  #vizsgált elem vége
    talalt = 0
    for j in range(0,len(munkaidoben[i])):
        vv_kezdo = hossza (munkaidoben[j][0],munkaidoben[j][1],munkaidoben[j][2])
        vv_vegzo = hossza (munkaidoben[j][3],munkaidoben[j][4],munkaidoben[j][5])
        if (v_vegzo>vv_vegzo):
            if (v_kezdo<vv_vegzo): 
                #print ("siker", i,  munkaidoben[i],munkaidoben[j])
                talalt=i
    if(talalt>0):
        sikeres.append([talalt, munkaidoben[talalt]])

file = open("sikeres.txt","w")
for item in sikeres:
    add=str(item[0])+" "
    for i in range(len(item[1])):
        add+=str(item[1][i])+" "
    file.write(add+"\n")
file.close()
#A logika tuti nem jó benne, sem az ahogy csináltam, sem ahogyan megadták
