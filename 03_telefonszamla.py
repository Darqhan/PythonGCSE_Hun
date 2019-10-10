def openFile():
    file = open("HIVASOK.txt")
    telefon = []
    for items in file:
            telefon.append(items.rstrip())
    return telefon
#olvassk be a fájlt, majd külön elteszem a telószámot és a hívásidő kezdet/véget.
telefon=openFile()
hivasido= telefon[::2] 
telefonszam = telefon[1::2]

def new_phone_IN(): 
    uj_telefonszam = ""
    while (uj_telefonszam.isdigit()==False):
        uj_telefonszam = input("adj egy telószámot(9 számjegy): ")
        uj_telefonszam = uj_telefonszam.rstrip()
    return uj_telefonszam[:10]

def is_mobil(szam):
    if (("39" in szam)or("41"in szam)or("71" in szam)):
        return(True)
    else:
        return False
def time_input(myStr):
    time_now=''
    while ((time_now.isdigit()==False)or(not(len(time_now)==6))):
        time_now = input(myStr)
    return time_now
'''
#bekérek egy számot (nem kell validáltatni, azért validáltatom)
szamom =(new_phone_IN()) 
#a bekért számról eldönteni, hogy mobil vagy vezetékes,ami 39,41,71 !!!!!!
print(is_mobil(szamom))
#bekérni kezdeti-hívás vége időpont (óóppmm) Kiírni mennyi perc volt!
kezdete = time_input("Hívás kezdete(óóppmm): ")
vége = time_input("Hívás vége(óóppmm): ")
ktsg_ora = abs((int(vége[0:2])-int(kezdete[0:2])))*60
#mert minden megkezdett másodperc is számít
ktsg_perc = abs((int(vége[2:4])+ktsg_ora-int(kezdete[2:4])))+(int(vége[4:6])>0)
print("ennyi megkezdett perc volt: ", ktsg_perc)
'''

ktsg_ora=[]
ktsg_perc=[]
for i in range(len(hivasido)):
    #meghatározni az óra-perc-mp-ket
    kezdete_ora = int((hivasido[i].split(" "))[0])
    kezdete_perc= int((hivasido[i].split(" "))[1])
    kezdete_mp = int((hivasido[i].split(" "))[2])
    vége_ora = int((hivasido[i].split(" "))[3])
    vége_perc = int((hivasido[i].split(" "))[4])
    vége_mp = int((hivasido[i].split(" "))[5])
    #számolás
    ktsg_ora.append((abs(kezdete_ora - vége_ora)))
    ktsg_perc.append( abs(vége_perc+ktsg_ora[i]-kezdete_perc)+(int(vége_mp>0)))
    #print (ktsg_perc[i]," ",telefonszam[i])

'''
    # fájlba kellene kiírni ilyen formában
    new_file = open("percek.txt","a")
    argz = (str(ktsg_perc[i]))+" "+(str( telefonszam[i])+"\n")
    new_file.write(argz)
'''
#4.feladat: csúcsidőben hívások | csúcsidőn kívül hívások száma
# csúcsidő: 7.00-18.00 a kezdete számít
csucsido, csucsidon_kivul=0,0
fizetendo_mobil, fizetendo_vezetékes = 0,0
for i in range(len(hivasido)):
        if (int((hivasido[i].split(" "))[0])>7) and (int((hivasido[i].split(" "))[0])<18):
            csucsido+=1
            if is_mobil(telefonszam[i]): 
                fizetendo_mobil += int(ktsg_perc[i])
            else: 
                fizetendo_vezetékes += int(ktsg_perc[i])
        else:
            csucsidon_kivul+=1
mobil_percek = fizetendo_mobil
vezetek_percek = fizetendo_vezetékes

fizetendo_mobil =   fizetendo_mobil*69.175
fizetendo_vezetékes = fizetendo_vezetékes * 30

print (" csúcsidős hívások darabszáma: ",csucsido,"\n","csúcsidőn kívüli hívások darabszáma:", csucsidon_kivul)
print (" csúcsidős mobil hívások díja: ", fizetendo_mobil,"\n","csúcsidős vezetékes díja: ", fizetendo_vezetékes)
print (" csúcsidős mobil hívások perce: ", mobil_percek,"\n","csúcsidős vezetékes hívások perce: ", vezetek_percek)

# számok nem egyformák vszeg máshogy vonták ki őket egymásből, ill. a megkezdett percet is máshogy számolják
#az üzletilogika nem lett letisztázva
