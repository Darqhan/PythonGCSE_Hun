def beolvas():
    file = open("penztar.txt","r")
    lista=[]
    for item in file:
        lista.append(item.rstrip())
    new_list = []
    elem = ""
    for item in lista:
        if (item=="F"):
            new_list.append([elem.rstrip()])
            elem=""
        else:
            elem +=item+","
    return new_list
lista =beolvas()
print ("\n2.feladat: Mennyiszer fizettek a pénztárnál: ",len(lista))
print ("\n3.feladat: Az első vásárlónak, ",len(lista[0]),"darab árucikk volt a kosarában.")
#------------------------
def bekeres_szam(maximum,txt):
    usr_inpt = "0"
    while((int(usr_inpt)<=0)or(int(usr_inpt)>maximum)):
        usr_inpt=input(txt)
        if((usr_inpt =="")or (usr_inpt[0] not in "123456789")):
            usr_inpt ="0"
    return int(usr_inpt)
def elerheto_aruk():
    #szorgalmi függvény a létező árukról
    new = []
    for i in range(len(lista)):
        elem = []
        for j in range(len(lista[i])):
            elem=(lista[i][j].split(","))
            for mind in elem:
               new.append(mind)
    new=list(dict.fromkeys(new))
    new.sort()
    return new[1:]
def ellenorzes(arucikk,elerheto_aruk):
    isTrue = False
    for item in elerheto_aruk:
        if (arucikk == item):
            isTrue = True
    return isTrue
def bekeres_txt():
    usr_inpt=""
    while ((len(usr_inpt)<=0)or (ellenorzes(usr_inpt,elerheto_aruk)==False)):
        usr_inpt=input ("Add meg egy árucikk nevét: ")
        if (usr_inpt[0] in "1234567890"):
            print ("ez szám!")
            usr_inpt=""
    return usr_inpt
elerheto_aruk = elerheto_aruk()
print ("\n4. feladat: adatbekérés")
sorszam = bekeres_szam(1000, "Adj egy sorszámot 1-1000 közt:")
print (*elerheto_aruk, sep=" ")
arucikk = bekeres_txt()
darab = bekeres_szam(20, "Adj egy darabszámot 1-20 közt:")
print ("\n5.feladat: ÁRUCIKK: első és utolsó vásárlás, összesen vásárolt alkalom")
def otos_feladat(arucikk):
    elso, utolso,osszes=0,0,0
    for i in range(len(lista)):
        if(arucikk in lista[i][0]):
            osszes +=1
            if (elso==0):
                elso =i+1
            if(utolso<i):
                utolso=i+1
    valasz = "Először vettek a "+arucikk+"-ből "+str(elso)+" vásárláskor, utoljára: "+str(utolso)+" , összesen: "+str(osszes)+" alkalommal vettek."
    return valasz

van = ellenorzes(arucikk, elerheto_aruk)
print (otos_feladat(arucikk))

#-------------------------
def ertek(darab):
    aruk_ara = 0
    for i in range(1,darab+1):
        aruk_ara+=400
        if (i==1):
            aruk_ara+=100
        elif (i==2):
            aruk_ara+=50
    return aruk_ara
print ("\n6.feladat:" ,darab, "darab után fizetendő: ",ertek(darab)," huf")
def benne_vannak(data):
    vannak =[0,0,0,0,0,0,0,0,0,0]
    for item in lista[data]:
        cuccok =item.split(",")
        for i in range(len(elerheto_aruk)): 
            for elem in cuccok: 
                if(elem==elerheto_aruk[i]):
                    vannak[i]+=1
    return vannak
data=sorszam-1
vannak = benne_vannak(data)

def aaru_darab(vannak):
    aru_per_darab = []
    for i in range(len(vannak)):
        if (vannak[i]>0):
            #print(vannak[i], elerheto_aruk[i])
            aru_per_darab.append([vannak[i],elerheto_aruk[i], ertek(vannak[i])])
    return aru_per_darab
eredmeny = aaru_darab(vannak)
# eredmeny = [[2, 'HB ceruza'], [2, 'colostok'],
#8.feladat
utolso_feladat = []
for i in range(len(lista)):
    utolso_feladat.append(aaru_darab(benne_vannak(i)))
file = open("osszeg.txt","w")
j=0
for item in utolso_feladat:
    osszeg=0
    for i in range(len(item)):
        osszeg+=int(item[i][2])
    j+=1
    file.write(str(j)+": "+str(osszeg)+"\n")
file.close()



    
