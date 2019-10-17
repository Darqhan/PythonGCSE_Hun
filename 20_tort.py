print ("\n2012 Május")
#--------------------------------
  #
 ##
# #
  #     #
#####
#--------------------------------
print ("\n1.feladat: Bekérni nevező/számláló; eldönteni egész-e")
def bekeres(): #adatbekérés minden számhoz
    szam = "0"
    while (szam == "0"):
        szam = input("Add meg a számot: ")
        if (szam==""):
            szam = "0"
    return int(szam)
def eldontes(szamlalo,nevezo): #egész szám jön e ki ha elosztjuk a kettőt
    if (szamlalo%nevezo==0):
        return 1
    else:
        return 0

szamlalo = bekeres()
nevezo = bekeres()
if (eldontes(szamlalo, nevezo)==0):
    print ("Nem egész: ",szamlalo, "/", nevezo)
else:
    print ("Eredmény:",int(szamlalo / nevezo))
#-----------------------------
    #####
        #
    #####
    #       #
    #####
#------------------------------
def lnkoszto(a,b):
    if (b==0):
        return a
    else:
        return lnkoszto(b,a%b)
a = 60
b = 48
print ("\n2.feladat: Legnagyobb közös osztó:", lnkoszto(szamlalo,nevezo),"[", szamlalo,"/",nevezo,"]")
#----------------------------
    #####
        #
    #####
        #   #
    #####
#----------------------------
print ("\n3.feladat: Bekért számok szebb alakba tevése.")
print (" Nevező: ", nevezo, "Számláló: ",szamlalo)
kozos_oszto = lnkoszto(szamlalo,nevezo)
if (szamlalo%nevezo==0):
    print (szamlalo, "/",nevezo, "=",int(szamlalo/nevezo))
else:
    print (szamlalo, "/",nevezo, "=",int(szamlalo/kozos_oszto),"/",int(nevezo/kozos_oszto))
#-----------------------------
    #
    #   #
    #####
        #
        # #
        #
#-----------------------------
print ("\n4.feladat: Bekérni még 1 törtet ")
elso = [szamlalo, nevezo]
szamlalo = bekeres()
nevezo = bekeres() 
masodik = [szamlalo, nevezo]
lnko = lnkoszto(elso[0],masodik[0])
sz_sz =int(elso[0]*masodik[0]/lnko)
n_sz = int(elso[1]*masodik[1]/lnko)
print ("Az első tört: ",*elso,sep="/")
print ("A második tört: ",*masodik,sep="/")
print ("A két tört szorozva:", elso[0]*masodik[0],"/", elso[1]*masodik[1],"=",sz_sz, "/", n_sz)
#------------------------------
    #####
    #
    #####
        # #
    #####
#------------------------------
print ("\n5.feladat: Két közönséges tört LNKO, LKK")
def lkktoszto(a,b,lnko):
    return int(a*b/lnko)
lnko= lnkoszto(elso[1],masodik[1])
lkkt=lkktoszto(elso[1], masodik[1],lnko)
def egyszerusito(a,b,oszto): 
    if (a%b==0):
        return [int(a/b),1]
    else:
        return (int(a/oszto),int(b/oszto))

print ("lkkt: ",lkkt, "lnko: ",lnko)
print ("\n6.feladat: A két bekért tört összegének meghatározása")

kozosNevezo = int(elso[1]*masodik[1])
kozosEgyik = int (elso[0]*masodik[1])
kozosMasik = int (masodik[0]*elso[1])
def eredmeny (egyik, masik, nevezo):
    if ((egyik+masik)/nevezo==0):
        return str((egyik+masik)/nevezo)
    else:
        lnko = lnkoszto(egyik+masik, nevezo)
        egyik = int(egyik/lnko)
        masik = int(masik/lnko)
        nevezo = int (nevezo/lnko)
        return (str(egyik+masik)+"/"+str(nevezo))
def eredmeny_szorzo (egyik, masik, nevezo):
    if ((egyik+masik)/nevezo==0):
        return str((egyik*masik)/nevezo)
    else:
        lnko = lnkoszto(egyik+masik, nevezo)
        egyik = int(egyik/lnko)
        masik = int(masik/lnko)
        nevezo = int (nevezo/lnko)
        return (str(egyik*masik)+"/"+str(nevezo))      
print (elso[0],"/",elso[1],"+",masodik[0],"/",masodik[1],"=",kozosEgyik,"/",kozosNevezo,"+",kozosMasik,"/",kozosNevezo, "=", kozosEgyik+kozosMasik,"/",kozosNevezo,"=", eredmeny(kozosEgyik, kozosMasik, kozosNevezo))
#----------------------------------
######
    #
   #
  # #
 # 
#----------------------------------
print ("\n7.feladat: Beolvasni adat.txt-t, beirni az eredmeny.txt-be az eredményeket")
lista = []
file = open("adat.txt","r")
for item in file:
    item=item.split()
    for i in range(0,len(item)-1):
        item[i]=int(item[i])
    lista.append(item)
new_file = open("eredmeny.txt","a")
for item in lista:
    elso = [item[0],item[1]]
    masodik = [item[2],item[3]]
    kozosNevezo = int(elso[1]*masodik[1])
    kozosEgyik = int (elso[0]*masodik[1])
    kozosMasik = int (masodik[0]*elso[1])
    if(item[-1]=="+"):
        eredmeny_most = str(elso[0])+"/"+str(elso[1])+"+"+str(masodik[0])+"/"+str(masodik[1])+"="+str(kozosEgyik)+"/"+str(kozosNevezo)+"+"+str(kozosMasik)+"/"+str(kozosNevezo)+"="+str(kozosEgyik+kozosMasik)+"/"+str(kozosNevezo)+"="+eredmeny(kozosEgyik, kozosMasik, kozosNevezo)+"\n"
        new_file.write(eredmeny_most)
    elif(item[-1]=="*"):
        eredmeny_most = str(elso[0])+"/"+str(elso[1])+"*"+str(masodik[0])+"/"+str(masodik[1])+"="+str(kozosEgyik)+"/"+str(kozosNevezo)+"*"+str(kozosMasik)+"/"+str(kozosNevezo)+"="+str(kozosEgyik+kozosMasik)+"/"+str(kozosNevezo)+"="+eredmeny_szorzo(kozosEgyik, kozosMasik, kozosNevezo)+"\n"
        new_file.write(eredmeny_most)

new_file.close()




