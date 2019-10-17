print ("\n2012 Október Érettségi")
print ("\n1.feladat: Beolvasni a kép.txt-t egy lista állományban, array és int")
def beolvas():
    lista=[]
    file = open ("kep.txt","r")
    for item in file:
        item=item.rstrip()
        item=item.split()
        for i in range(len(item)):
            item[i] = int(item[i])
        lista.append(item)
    return lista
lista = beolvas()
print ("\n2.feladat: Bekérni egy RGB kódot konzolról, van-e ilyen szín a listában i/n")
def bekeres():
    kod = ["-1","-1","-1"]
    #rgb 0-255
    for i in range(3):
        while((int(kod[i])>255)or(int(kod[i])<0)):
            rgb = "RGB kód "+str(i)+"/3:"
            kod[i]=int(input(rgb))
            if (kod[i]==""):
                kod[i]="-1"
    return kod
user_kod = bekeres()

for j in range(len(lista)):
    if ((user_kod[0]==lista[j][0])and(user_kod[1]==lista[j][1])and(user_kod[2]==lista[j][2])):
        print ("találat: ", j)
print ("\n3.feladat: A kép 35.sor8.képpontja mennyiszer van a 35.sorban / 8.oszlopban")
#35.sor 8.oszlopa = 1707 index
darab_sor,darab_oszlop = 0,0
for i in range(34*50,35*50):
    if(lista[i][0]==lista[1707][0])and(lista[i][1]==lista[1707][1])and(lista[i][2]==lista[1707][2]):
        darab_sor +=1
for i in range (7,2500,50):
    if(lista[i][0]==lista[1707][0])and(lista[i][1]==lista[1707][1])and(lista[i][2]==lista[1707][2]):
        darab_oszlop +=1
print ("Válasz:", "sorban:",darab_sor,"oszlopban:",darab_oszlop)

RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

darab_red, darab_green, darab_blue = 0,0,0
for i in range (len(lista)):
    if(lista[i][0]==RED[0])and(lista[i][1]==RED[1])and(lista[i][2]==RED[2]):
        darab_red +=1
    elif(lista[i][0]==GREEN[0])and(lista[i][1]==GREEN[1])and(lista[i][2]==GREEN[2]):
        darab_green+=1
    elif(lista[i][0]==BLUE[0])and(lista[i][1]==BLUE[1])and(lista[i][2]==BLUE[2]):
        darab_blue+=1
szin_talalat = [darab_red, darab_green, darab_blue]
szinnevek = ["vörös","zöld","kék"]
print ("r:",darab_red,", g:",darab_green,", blue:",darab_blue)
print("A legtöbb: ", max(szin_talalat),",ami a :", szinnevek[szin_talalat.index(max(szin_talalat))])

print ("\n5.feladat: Fekete keret készítése: 3 képpont széles, fekete [0,0,0]")
#alul:3 sor, teljes: len (lista)-150től len(lista-ig)
#felül: 3 sor,teljes: 0-50+51-100+101-150
#bal:0,1,2| 50,51,52 >> 0tól, len(lista)-ig, 50esével: i+0-t ,i+1-t,i+2-t
#jobb: 48,49,50 | 98,99,100 >> 48-tól, lenlista-ig, 48-sával i+0, i+1, i+2
def fekete_keret():
    for i in range(0,150,1):
        #felső keret, mind
        for j in range(len(lista[i])):
            lista[i][j] = 0
    for i in range (len(lista)-150,len(lista),1):
        #alsó keret, mind
        for j in range(len(lista[i])):
            lista[i][j]=0
    for i in range (0, len(lista),50):
        #bal oldal
        for j in range(len(lista[i])):
            lista[i][j] = 0
            lista[i+1][j] = 0
            lista[i+2][j] = 0
    for i in range (0, len(lista),48):
        #jobb oldal
        for j in range(48,len(lista[i]),50):
            lista[i][j] = 0
            lista[i+1][j] = 0
            lista[i+2][j] = 0           
fekete_keret()


print ("\n6.feladat: Írd ki a keretes.txt-be, szóköz")
file = open("keretes.txt","w")
for item in lista:
    to_write = str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n"
    file.write(to_write)
file.close()


print ("\n7.feladat: sárga (255,255,0) téglalap megtalálása")


yellow = [255,255,0]
darab_y = 0
elso,i = 0,0
elso_talalt = 0
while (elso==0): 
    if(lista[i][0]==yellow[0])and(lista[i][1]==yellow[1])and(lista[i][2]==yellow[2]):
        elso_talalt = i
        elso = 1
    i+=1
utolso = 0

for i in range (len(lista)):
    if(lista[i][0]==yellow[0])and(lista[i][1]==yellow[1])and(lista[i][2]==yellow[2]):
        darab_y +=1
        utolso = i


print ("Kezd: sor", int(elso_talalt/50) ," oszlop", int (elso_talalt%50)) # legkisebb sor, első oszlopa
print ("Vége: sor", int(utolso/50)," oszlop ",int(utolso%50)) # legnagyobb sor, utolsó oszlopa
print ("Képpontok száma: ",darab_y)


































