print ("\n1.feladat: Beolvasni a felszam.txt-t listába.")
def beolvas():
    file = open ("felszam.txt","r")
    lista = []
    for item in file:
        lista.append(item.rstrip())
    return lista
regi_lista = beolvas()
lista = []
for i in range(0,len(regi_lista),2):
    # ilyen formában akarok vele dolgozni:
    # [1.adat,[2.lista]],
    # szöveg, [str(szám),str(szám),szöveg]
    item = regi_lista[i+1].split()
    lista.append([regi_lista[i],item])
print ("\n2.feladat: Mennyi feladatunk van? Válasz: ", len(lista))
egypontos, ketpontos, harompontos = 0,0,0
for i in range(len(lista)):
    if(lista[i][1][-1]=="matematika"):
        if(lista[i][1][1]=="1"):
            egypontos+=1 
        elif(lista[i][1][1]=="2"):
            ketpontos+=1
        elif(lista[i][1][1]=="3"):
            harompontos+=1
print ("Az adatfajlban ", int(egypontos)+int(ketpontos)+int(harompontos) ,"matematika feladat van:")
print ("         -1 pontot er ",egypontos, "feladat.")
print ("         -2 pontot er ", ketpontos,"feladat.")
print ("         -3 pontot er ",harompontos,"feladat.")
print ("\n4.feladat: mettől meddig terjed a fájlban található válaszok számértéke?")
kicsi,nagy = 100,1
for item in lista:
    if (kicsi>int(item[1][0])):
        kicsi = int(item[1][0])
    if (nagy<int(item[1][0])):
        nagy = int(item[1][0])
print ("A válaszok számértéke ",kicsi,"-től",nagy,"-ig terjed.")
temak = []
for item in lista:
    temak.append(item[1][-1])
temak = list(dict.fromkeys(temak))
print ("\nKiíratni a témaköröket.(",len(temak)," darab)")
print (*temak, sep = ", ")
print ("\n\n6.feladatok: KVÍZ")
def bekeres():
    tema = ""
    while (len(tema)==0):
        tema = input("Milyen témakörből szeretne kérdést kapni?")
        if((len(tema)==0)or(tema not in temak)):
            tema = "tortenelem"
    return tema
def kerdes(tema):
    #először kell, mennyi kérdés van a témában, és milyen indexen
    indexek = []
    import random
    for i in range(len(lista)):
        if (lista[i][1][-1]==tema): 
            indexek.append(i)
          #visszaadja az index értékét az adott témakör véletlen kérdésének  
    return (indexek[ random.randint(0,len(indexek))])

valasztas = bekeres()
my_index=kerdes(valasztas)
def megkerdezes (my_index):
    questn = input (lista[my_index][0])
    answr = lista[my_index][1][0]
    helyes = lista[my_index][1][1]+" pont"
    helytelen = "A válasz 0 pontot ér. A helyes válasz: "+answr
    if (questn==answr):
        return helyes
    else:
        return helytelen

print (megkerdezes(my_index))
print ("\n7.feladat: Generáljunk 10 feladatot")
import random
elso = random.randint(1,len(lista))
veletlen = [elso]
velszam = veletlen[0]
for i in range(9):
    while (velszam in veletlen): 
            velszam = random.randint(0,len(lista))
    veletlen.append(velszam)
veletlen.sort()

pontszam = 0
file = open("tesztfel.txt","w")
for item in veletlen:
    kiiratas = lista[item][1][0]+" "+lista[item][1][1]+" "+lista[item][0]+"\n"
    print (kiiratas)
    file.write(kiiratas)
    pontszam += int(lista[item][1][1])
file.write("A feladatsorra összesen "+str(pontszam)+" pont adható.")
file.close()




