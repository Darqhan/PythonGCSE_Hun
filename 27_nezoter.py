print("\n1.feladat: Beolvasni foglaltsag és kategoria txt-t listába")

def beolvas(data):
    lista=[]
    file = open(data,"r")
    for item in file:
        lista.append(item.rstrip())
    return lista
foglaltsag = beolvas("foglaltsag.txt")
kategoria = beolvas("kategoria-4.txt")
#foglaltsag:: 15 sor X 20 szék van; X= foglalt, O=szabad
#kategoria:: 1 = 5000, 2 = 4000, 3 = 3000, 4=2000, 5 = 1500
#---------------
print("\n2.feladat: Bekérni 1 sor és székszámot, és kiírni, hogy Foglalt/Szabad.")
def user_input(min, max,data,sor_oszlop):
    result = "0"
    max=max+1
    while ((int(result)<min)or(int(result)>=max)or(result=="0")):
        result=input(sor_oszlop)
        if(result==""):
            result="0"
    return int(result)-1
sor = user_input(1,15,foglaltsag,"sor: ")
szek = user_input(1,20,foglaltsag,"oszlop: ")
if(foglaltsag[sor][szek]=="o"):
    print ("Még szabad!")
else:
    print("Már foglalt!")
#-------------------------
eladott,szaz =0,0
#összes = 15 sor x 20 szék = 300 
for item in foglaltsag:
    for szek in item:
        if(szek=="x"):
            eladott+=1
szaz = int((eladott/300)*100)
print("\n3.feladat: Az előadásra, eddig ",eladott,"jegyet adtak el, ami a nézőtér",szaz,"%-a")
#------------------------
arkat = [0,0,0,0,0]
for item in kategoria:
    for szek in item:
        if(szek=="1"):
            arkat[0]+=1
        elif (szek=="2"):
            arkat[1]+=1
        elif (szek=="3"):
            arkat[2]+=1
        elif (szek=="4"):
            arkat[3]+=1
        elif (szek=="5"):
            arkat[4]+=1 
print("\n4.feladat: A legtöbb jegyet a(z)", arkat.index(max(arkat))+1,".árkategóriában értékesítették.")
print ("\n5.feladat: Mennyi lenne a színház pillanatnyi bevétele?")
osszes,i,j = 0,0,0
arkat = [0,0,0,0,0]
for item in foglaltsag:
    j=0
    for szek in item:
        if(szek=="x"):
            if(kategoria[i][j]=="1"):
                arkat[0]+=1
            elif(kategoria[i][j]=="2"):
                arkat[1]+=1
            elif(kategoria[i][j]=="3"):
                arkat[2]+=1
            elif(kategoria[i][j]=="4"):
                arkat[3]+=1
            elif(kategoria[i][j]=="5"):
                arkat[4]+=1
        j+=1
    i+=1
osszes = arkat[0]*5000 + arkat[1]*4000 + arkat[2]*3000 + arkat[3]*2000 + arkat[4]*1500 
print ("Összes árbevétel: ",osszes," Ft")
#----------------------------------------
item_szam=[]
for item in foglaltsag:
    szam = 0
    for szek in item:
        if(szek=="o"):
            szam+=1
    item_szam.append([item, szam])
#print (*item_szam, sep="\n")
szamlal = []
for item in foglaltsag:
    szamol = 0
    for i in range(1,len(item)-1):
        if(item[i-1]+item[i]+item[i+1]=="xox"):
            szamol+=1
    if ((item[0]+item[1]=="ox")or(item[-2]+item[-1]=="xo")):
        szamol+=1
    #print(szamol)
    szamlal.append(szamol)
print("\n6.feladat: Összes egyedül maradt szabad szék: ",sum(szamlal)," darab.")
print ("\n7.feladat: Összehasonlítani a két listát, x-szám")
szabad,i,j=[],0,0
for item in foglaltsag:
    j,sor=0,""
    for szek in item:
        if(szek=="o"):
            sor+=kategoria[i][j]
        else:
            sor+=szek
        j+=1
    szabad.append(sor)
    i+=1
#------------írjam ki --------
file = open("szabad.txt","w")
for item in szabad:
    file.write(item+"\n")
file.close()




