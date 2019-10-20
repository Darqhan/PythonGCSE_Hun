print("\n1.feladat: Olvasd be a verseny-1.txt-t listába")
def beolvas():
    lista=[]
    file = open("verseny-1.txt","r")
    for item in file:
        lista.append(item.rstrip())
    return lista[1:]
lista = beolvas()
#----------------
print ("\n2.feladat: Azon versenyzők rajtszáőma, akiknek legalább 2 lövése talált:")
for item in lista:
    if("++"in item):
        print (lista.index(item),end=", ")
#----------------
print ("\n3.feladat: Mely versenyző(k) adták le a legtöbb lövést")
legn,indx = 0,0
for item in lista:
    if(legn<len(item)):
        legn = len(item)
        #ha lenne több egyforma, akkor listába kellene tenni, utána ciklussal kiíratni
        indx = lista.index(item)
print (legn+1,". rajtszámú versenyző adta le a legtöbb lövés:", lista[indx])
#-----------------
print ("\n4.feladat: függvény elkészítése")
def loertek(sor):
    aktpont,ertek = 20,0
    for i in range(0,len(sor)):
        if ((aktpont>0)and(sor[i]=="-")):
            aktpont -= 1
        else:
            ertek+=aktpont
    return ertek 
#print (lista[0])
#print (loertek(lista[0]))
#-------------
print ("\n5.feladat: Bekérjük 1 versenyző sorszámát")
def versenyzo_sorszam(data):
    bekeres="0"
    while(bekeres=="0")or(int(bekeres)>len(data)):
        bekeres = input("Add meg a versenyző sorszámát:")
        if (bekeres ==""):
            bekeres ="0"
    return int(bekeres)
print ("Bekért versenyző sorszáma")
versenyzo=versenyzo_sorszam(lista)-1
def celt_ert(data):
    result=[]
    for i in range(len(data)):
        if(data[i]=="+"):
            result.append(i+1)
    return result
def talalt(data):
    result=0
    for i in range(len(data)):
        if(data[i]=="+"):
            result += 1
    return result
def leghosz(data):
    result = 0
    lh = 0
    for item in data:
        if(item=="+"):
            result+=1
        else:
            if(lh<result):
                lh = result
                result = 0
    return lh

print ("\t5.a.feladat: Célt érő lövések:", *celt_ert(lista[versenyzo]), sep=" ")
print ("\t5.b.feladat:Az eltalált korongok száma:",talalt(lista[versenyzo]))
print ("\t5.c.feladat: A leghosszabb hibatlan sorozat hossza:",leghosz(lista[versenyzo]))
print ("\t5.d.feladat: A versenyzo pontszama:",loertek(lista[versenyzo]))
#print(lista[versenyzo])
#-----------------------
print ("\n6.feladat: sorrend.txt-be írni: helyezés, rajtszám, pontszám| TAB-bal")
adatok,i = [],0
for item in lista:
    pontszam = loertek(item)
    print (item, pontszam,i+1)
    adatok.append([pontszam,i+1])
    i+=1
adatok.sort(reverse=True)
print(*adatok, sep="\t\n")

def file_kiiras():
    file = open("sorrend.txt","w")
    i = 1
    for item in adatok:
        file.write(str(i)+"\t"+str(item[1])+"\t"+str(item[0])+"\n")
    file.close()
file_kiiras()
