print ("\n1.feladat: veetel.txt megnyitása listába")
def beker():
    file = open("veetel.txt","r")
    lista=[]
    for item in file:
        lista.append(item.rstrip())
    return lista
lista = beker()
# NAP(1-11) RÁDIÓS-sorszáma(1-20)
# 90 karakter:: $=üres, #=nem azonosítható
# farkast látott: szám(felnőtt)/szám(kölyök) szókösz
#------------------
print ("\n2.feladat")
elso = lista[0].split(" ")
masik = lista[-2].split(" ")
print("Az első üzenet rögzítője: ", elso[1])
print("Az utolsó üzenet rögzítője: ", masik[1])
#-------------------
print("\n3.feladat: összes nap/sorszám, ahol a \"farkas\" szó szerepel")
for i in range(1,len(lista),2):
    if("farkas" in lista[i]):
        adat = lista[i-1].split(" ")
        print(adat[0]+". nap "+adat[1]+". rádióamatőr")
#------------------
print ("\n4.feladat: Statisztika: melyik napon, mennyi rádiós volt, vagy 0.")
napok = [0,0,0,0,0,0,0,0,0,0,0]
nap_index= [[],[],[],[],[],[],[],[],[],[],[]]
for i in range(0,len(lista),2):
    data= lista[i].split(" ")
    if (data[0]=="1"):
        napok[0]+=1
        nap_index[0].append(i)
    elif (data[0]=="2"):
        napok[1]+=1
        nap_index[1].append(i)
    elif (data[0]=="3"):
        napok[2]+=1
        nap_index[2].append(i)
    elif (data[0]=="4"):
        napok[3]+=1
        nap_index[3].append(i)
    elif (data[0]=="5"):
        napok[4]+=1
        nap_index[4].append(i)
    elif (data[0]=="6"):
        napok[5]+=1
        nap_index[5].append(i)
    elif (data[0]=="7"):
        napok[6]+=1
        nap_index[6].append(i)
    elif (data[0]=="8"):
        napok[7]+=1
        nap_index[7].append(i)
    elif (data[0]=="9"):
        napok[8]+=1
        nap_index[8].append(i)
    elif (data[0]=="10"):
        napok[9]+=1
        nap_index[9].append(i)
    elif (data[0]=="11"):
        napok[10]+=1
        nap_index[10].append(i)
for i in range(1,12): 
    print(i,". nap: ", (napok[i-1])," rádióamatőr")
#--------------------
print("\n5.feladat:Naponként helyreállítani az üzenetet")
def megfejtes(lista,nap):
    uzenet = lista[0]
    for i in range(1,len(lista)-1,1):
        napok_radiosok = lista[i].split(" ")
        #print(lista[i+1])
        for j in range(len(lista[i+1])):
            if ((uzenet[j]=="#")and(lista[i+1][j]!="#")):
                uzenet=(uzenet[:j])+(lista[i+1][j])+(uzenet[(j+1):])
    return uzenet
#print(*nap_index, sep="\n")
adaas = []
for i in range(len(nap_index)):
    current_list = []
    for j in range(len(nap_index[i])):
        #nap-rádiós | szöveg | index
        #print (lista[nap_index[i][j]]+"\n"+lista[nap_index[i][j]+1])
        current_list.append(lista[nap_index[i][j]+1])
    index = lista[nap_index[i][j]].split(" ")
    current_list.append("\nhelyreállított üzenet:\n"+megfejtes(current_list,index[0])+"\n")
    adaas.append(current_list)
#----------------------------iírni fájlba -------
def kiiras():
    file = open("adaas.txt","w")
    for item in adaas:
        for uzenet in item:
            file.write(uzenet+"\n")
    file.close()
kiiras()
#-------------------------------------------------
def szame(szo):
    valasz = True
    for i in range(len(szo)):
        if((int(szo[i])<0)or(int(szo[i])>9)):
            valasz = False
    return valasz
#-------------------------------------------------
print("\n7.feladat: Add meg a napot, és a rádiós számát, vissza: egyedek")
def beolvas(maximum,text):
    napok = "0"
    while((napok=="0")or(int(napok)<1)or(int(napok)>maximum)):
        napok = input(text)
        if(napok==""):
            napok="0"
    return napok
naps = beolvas(11,"Adja meg a nap sorszámát: ")
radio = beolvas(20,"Adja meg a rádióamatőr sorszámát: ")
x=""
radios = False
for i in range(0,len(lista),2):
    nap_radios=lista[i].split()
    if(nap_radios[0]==naps):
        if(nap_radios[1]==radio):
            radios = True
            print(lista[i+1])
            szo=lista[i+1].split(" ")
            szo = szo[0]
            if (("/" not in szo)or("#"in szo)):
                print ("Nincs információ")
            elif("/"in szo):
                szamok = szo.split("/")
                if (szo[0] not in "012345667891011121314")and(szo[1] not in "01234567891011121314"):
                    print ("Nincs ilyen feljegyzés")
                else:
                    szo = szo.split("/")
                    if(szame(szo)):
                        print ("megfigyelt egyedek száma:", szo[0],"felnőtt és ",szo[1]," kölyök")
if(radios==False): 
    print ("nincs ilyen rádiós ezen a napon")
