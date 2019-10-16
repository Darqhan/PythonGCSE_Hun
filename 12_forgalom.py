def file_to_array():
    '''
    file megnyitás olvasásra
    soronként listához adni, és a \n és whitespace leszedésével
    '''
    file = open("forgalom.txt","r")
    data = []
    for lines in file:
        data.append(lines.split())
    return data

def list_to_number (data):
    '''
    A meglévő nyers listából a szöveget számmá alakítani
    '1','22','33','44','A' >> 1,22,33,44,'A' formájú legyen
    '''
    for i in range(1,len(data)):
        for j in range(0,len(data[i])-1):
            data[i][j] = int(data[i][j]) 
    return data
#--------------------------------------------------------------
print ("\n1.feladat: Beolvasni a fájlt listába")
data = file_to_array()
list_to_number(data)
print ("\n2.feladat: Bekérni egy számot 1-1105 (data[0]) közt")
def szam_bekeres(data):
    '''
    konzolról bekér egy stringet, ami legyen szám, és data[0]-0 közé essen
    '''
    bekeres = ""
    while ((not bekeres.isdigit())or(int(bekeres)<=0)or(int(bekeres)>int(data[0][0]))):
        bekeres = input ("adj egy számot")
    return (int(bekeres))
bekerve = szam_bekeres(data)
print ("Ezt a számot adatad meg: ",bekerve)
def irany(data):
    '''
    A feladat szerint F/A Felső- és Alsójózsa játszik 
    '''
    data = data[-1]
    if (data=="F"):
        return "Felsőjózsából jött Alsójózsa felé"
    else: 
        return "Alsójózsából jött Felsőjózsa felé"
print (data[bekerve],"\n",irany(data[bekerve]))
#---------------------------------------------------------------
print ("\n3.feladat: Felső város irányába (A) menő 2 utolsó, időbeli különbség")

def talald_meg_ket_utolsot(data): 
    ketto,i = 0,len(data)-1
    idobeli_elteres = []
    while (ketto!=2):
        if (data[i][-1]=="A"):
            idobeli_elteres.append(data[i])
            i-=1
            ketto+=1
        else:
            i-=1
    return idobeli_elteres
harmadik = talald_meg_ket_utolsot(data)

ora = abs(harmadik[0][0]-harmadik[1][0])
perc = abs(harmadik[0][1] - harmadik [1][1])
masodperc = abs(harmadik[0][2]-harmadik[0][2])
masodperc = (ora*3600)+(perc*60)+masodperc
print(masodperc," másodperc")
#---------------------------------------------------------------
print ("\n4.feladat: 1 órában, mennyi A/F")
def orankent_AF(data):
    '''
    0-24 óra alatt ha A > A+1, ha F>F+1
    Ez két lista, óránként
    '''
    hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    F= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range (24):
        for i in range(1,len(data)-1):
            if(data[i][0]==hours[x]):
                if (data[i][-1]=='A'):
                    A[x]+=1
                else:
                    F[x]+=1
    return [A]+[F]

D = orankent_AF(data)
for i in range(len(D[0])):
    if (D[0][i]>0):
        print (i,". órában,",D[0][i],": A,",D[1][i],": F")
#---------------------------------------------------------------
print ("\n5.feladat: 10 leggyorsabb jármű; kiírni: belépési iő, A/F, m/s")
new_data = data[1:]
#--------------------------------------------------------
def myFunc(new_data):
    '''
    A lista 3-s eleme alapján való sort-olást teszi lehetővé
    '''
    return new_data[3]
new_data.sort(key=myFunc)

def kiiratas_kepernyore(): 
    for i in range (10):
        '''
        időpont, sebesség m/s, és kiíratás
        '''
        belepesi_ido=str(new_data[i][0])+":"+str(new_data[i][1])+":"+str(new_data[i][2])
        sebesseg = 1000/new_data[i][3]
        print (belepesi_ido, "-kor ", new_data[i][-1]," felé, ", ("%.1f" % sebesseg), " m/s sebességgel")
#kiiratas_kepernyore()
#--------------------------------------------------------
print ("\n6.feladat: Az A felé tartók (=F) elhagyták az utat: időpont+idő")

def only_F(data):
    '''
    Az alap listából kiszedni az F-seket
    és másik listába tenni
    '''
    f_data = []
    for i in range(1,len(data)):
        if(data[i][-1]=='F'):
            f_data.append(data[i])
    return f_data

def masodpercek(data):
    '''
    csinálok egy listát, ami csak másodpercben tárolja
    feloldása: Also_varos_fele_tartok[-1] = ellenorzes[-1]
    16:22:43 + 160 = 59123
    '''
    mp = []
    for i in range(len(data)):
        masodperc = (data[i][0]*3600)+(data[i][1]*60)+(data[i][2]+data[i][3])
        mp.append(masodperc)
    return mp
def fileba_iras (data):
    new_file = open('also.txt','a')
    for i in range(len(data)):
        x = data[i]
        ora = int(x / 3600)
        perc = int((x%3600)/60)
        masodperc = (x%3600)%60
        ezt_iratom = str(ora)+" "+str(perc)+" "+str(masodperc)+"\n"
        new_file.write(ezt_iratom)
    new_file.close()     
Also_varos_fele_tartok = only_F(data)
ellenorzes = masodpercek(Also_varos_fele_tartok)
fileba_iras(ellenorzes)
