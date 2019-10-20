def fejvagyiras():
    import random
    szam = random.randint(0,1)
    if (szam==0):
        return ("F")
    elif(szam==1):
        return ("I")
print("\n1.feladat: Fej vagy írás?:", fejvagyiras())
eredmeny = fejvagyiras()
tipp=""
print("\n2.feladat")
while ((tipp!="I")and(tipp!="F")):
    tipp=input("Tippelj! Fej vagy írás? (F/I): ")
def talalt(a,b):
    if (a==b):
        return "Ön eltalálta!"
    else:
        return "Ön nem találta el!"
print ("A tipped: ", tipp, ", a dobás: ", eredmeny, ":",talalt(tipp, eredmeny))

file = open("kiserlet.txt","r")
line = file.readline()
count,fej,fuzer = 0,0,""
while (line):
    line = file.readline()
    count+=1
    fuzer+=line.rstrip()
    if (line.rstrip()=="F"):
        fej+=1
file.close()
print ("\n3.feladat: Ennyi dobásból áll a kísérlet:", count)
relgyak = (fej / count)*100
print ("\n4.feladat: Ennyiszer dobtunk fejet:", fej, ", relatív gyakoriság:","%.2f" % relgyak,"%")
print ("\n5.feladat: ")
szamol = 0
for i in range(1,len(fuzer)-2,1):
    if (fuzer[i-1]+fuzer[i]+fuzer[i+1]+fuzer[i+2]=="IFFI"):
        szamol+=1
if (fuzer[0]+fuzer[1]+fuzer[2]=="FFI"):
    szamol+=1
if (fuzer[-3]+fuzer[-2]+fuzer[-1]=="IFF"):
    szamol+=1
print ("Összesen ",szamol,"darab FF van. ")
cntr,legn=0,0
for i in range(len(fuzer)):
    if(fuzer[i]=="F"):
        cntr+=1
    else:
        if(cntr>legn):
            legn = cntr
            indx = [i-legn, i]
        cntr = 0
print ("\n6.feladat:A leghosszabb sorozat hossza:",legn,"indexe:",indx[0],"-tól,",indx[1],"-ig")
#-------------------------------------
print ("\n7.feladat: 1000x4 dobás, mennyi FFFF, FFFI volt, kiíratni")
adat = []
for i in range(1000):
    reszadat = []
    for i in range(4):
        dobas=fejvagyiras()
        reszadat.append(dobas)
    adat.append(reszadat)
forf,forfi = 0,0
for item in adat:
    vizsgald=""
    for elem in item:
        vizsgald+=elem
    if (vizsgald=="FFFF"):
        forf +=1
    elif (vizsgald=="FFFI"):
        forfi +=1

def kiiratas():
    file = open("dobasok.txt","w")
    file.write("FFFF: "+str(forf)+" FFFI: "+str(forfi)+"\n")
    for item in adat:
        irasd=""
        for elem in item:
            irasd+=elem
        file.write(irasd+" ")
kiiratas()



