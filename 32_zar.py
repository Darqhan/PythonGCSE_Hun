def beolvas ():
    lista = []
    file = open("ajto.txt","r")
    for item in file:
        lista.append(item.rstrip())
    return lista
lista = beolvas()
def bekeres():
    szam = ""
    while((len(szam)<1)or(len(szam)>10)):
        szam = input("Adj meg, mi nyitja a zárat, egy 1-10 számjegyű kódot! ")
        if (szam[:1] not in "123456789"):
            szam=""
    return szam
print ("\n2.feladat")
kodszam = bekeres()
kodszam = "239451" 
print("\n3.feladat")
talalt=[]
for i in range(len(lista)):
    if(lista[i]==kodszam):
        talalt.append(i+1)
print("A nyitó kódszámok sorai: ", end = " ")
print(*talalt, sep=", ")
ismetles = []
for i in range(len(lista)):
    for e in range(len(lista[i])-1):
        if (lista[i][e]==lista[i][e+1]):     
            ismetles.append(i)
if (len(ismetles)==0):
    ismetles = "nem vol ismétlődő számjegy"
else: 
    ismetles = min(ismetles)
print ("\n4.feladat: Az első ismétlődést tartalmazó sorszáma:", ismetles+1)
def ujszam(regiszam):
    import random
    elem=""
    for i in range(len(regiszam)): 
        elem += str(random.randint(1,10))
    return (elem)
randomCode = ujszam(kodszam)
print ("\n5.feladat: Egy ", len(randomCode)," hosszú kódszám:",randomCode)
#- -    -----
def nyit(jo,proba):
    egyezik = (len(jo)==len(proba))
    if(egyezik):
        #ciklus és elteres értékadása fel vannak cserélve a feladatban 
        for i in range(2,len(jo)):
            elteres=int(jo[i])-int(proba[i])
            #hehe, itt rossz a feladat: önmagából kivonva moduló az mindig 0%10 lesz
            if (elteres%10!=0):
                egyezik = False
        return egyezik
#-----------
output = open("siker.txt","w")
for item in lista:
    if (nyit (kodszam, item)):
        print (item+" sikeres")
        output.write(item+" sikeres\n")
    elif (len(kodszam)!=len(item)):
        print(item+" hibás hossz")
        output.write(item+" hibás hossz\n")
    elif (len(kodszam)==len(item)):
        print (item+" hibás kódszám")
        output.write(item+" hibás kódszám\n")
output.close()

