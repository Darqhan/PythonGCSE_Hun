def beolvas():
    lista =[]
    file = open("szavazatok-1.txt","r")
    for item in file:
        item = item.rstrip()
        item=item.split()
        for i in range(len(item)):
            if (i==0)or(i==1):
                item[i]=int(item[i])                
        lista.append(item)
    return lista
lista = beolvas()
# [5, 19, 'Ablak', 'Antal', '-']
# [0] = Válsztókör
# [1] = Szavazat
# [2] = Vezetéknév
# [3] = Keresztnév
# [4] = Párt
print ("\n1.feladat: Beolvasni a szavatok.txt-t, lista nevű arrayba")
print ("\n2.feladat: Mennyi képviselőjelölt indult?")
jeloltek = []
for item in lista:
    neve = item[2]+" "+item[3]
    jeloltek.append(neve)
jeloltek = list(dict.fromkeys(jeloltek))
print (" A helyhatósági választáson ",len(jeloltek), " képviselőjelölt indult")

print ("\n3.feladat: Kérj be egy vez.+xnevet, és írd ki indul e")
def bekeres(uzenet):
    neve = ""
    while (len(neve)==0):
        neve=input(uzenet)
    return neve
vezetek = bekeres("Vezetéknév: ")
kereszt = bekeres("Keresztnév: ")
nev = vezetek+" "+kereszt
if (nev in jeloltek):
    print ("Név elfogadva")
else:
    print ("ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
print ("\n4.feladat: Mennyien adtak le szavazatot. Részvételi arány. ")
osszeg = 0
for item in lista:
    osszeg += item[1]
Reszvetel = (osszeg / 12345)*100
print("A választásokon ",osszeg,"állampolgár, a jogosultak ","%.2f" %Reszvetel,"%-a vett részt.")
print ("\n5.feladat: Egyes pártokra leadott szavazat, %")
gyep, hep, tisz, zep, fj = 0,0,0,0,0
for item in lista:
    if (item[4] == "GYEP"):
        gyep+=item[1]
    if (item[4] == "HEP"):
        hep+=item[1]
    if (item[4] == "TISZ"):


        tisz+=item[1]   
    if (item[4] == "ZEP"):
        zep+=item[1]
    if (item[4] == "-"):
        fj+=item[1]
teljes_szavazat = gyep+hep+tisz+zep+fj
gyep_szazalek = gyep/teljes_szavazat*100
hep_szazalek  = hep/teljes_szavazat*100
tisz_szazalek = tisz/teljes_szavazat*100
zep_szazalek  = zep/teljes_szavazat*100
fj_szazalek   = fj/teljes_szavazat*100

print ("Gyümölcsevők Pártja :","%.2f" %gyep_szazalek,"%")
print ("Húsevők Pártja      :","%.2f" %hep_szazalek,"%")
print ("Tejivók Szövetsége  :","%.2f" %tisz_szazalek,"%")
print ("Zöldségevők Pártja  :","%.2f" %zep_szazalek,"%")
print ("Független jelöltek  :","%.2f" %fj_szazalek,"%") 

print ("\n6.feladat: melyik képviselő kapta a legtöbbet. Név/párt")
legnagyobb = 0
legjobbak = []
for item in lista:
    if(item[1]>=legnagyobb):
        legnagyobb = item[1]
for item in lista:
    if(item[1] == legnagyobb):
        if(item[-1]=="-"):
            print(item[2]," ",item[3],", független")
        else: 
            print(item[2]," ",item[3],",",item[-1])
print ("\n7.feladat: Kik lettek képviselők az egyes kerületekben!")

keruletek=[]
for item in lista:
#kerületek megszámolása
#eredmény = 1-8
    keruletek.append(item[0])
keruletek = list(dict.fromkeys(keruletek))
keruletek.sort()
kerulet_nyert = []
for item in lista:
    if(item[-1]=="-"):
        item[-1] = "független"
for i in range(len(keruletek)):
    legtobb,nyertes = 0,""
    for item in lista: 
        if (keruletek[i]==item[0]):
            if (legtobb<item[1]):
                legtobb = item[1]
                nyertes = item
    nyertes.append("\n")
    kerulet_nyert.append(nyertes)
file = open ("kepviselok.txt","w")
for item in kerulet_nyert:
    eredmeny = str(item[0])+" "+str(item[1])+" "+item[2]+" "+item[3]+" "+item[4]+item[5]
    file.write(eredmeny)
file.close()
