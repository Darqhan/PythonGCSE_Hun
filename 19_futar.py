print("\n2012.Május Érettségi")
###
 #
 #
 #
### #
print ("\n1.feladat: Beolvasni a tavok.txt-t egy lista változóba, számokként")
file = open("tavok.txt","r")
lista = []
for item in file:
    item.rstrip()
    lista.append([int(s) for s in item.split(' ')])
file.close()
#####
 # #
 # #
 # # 
##### #
# Mely napokon dolgozott a futár a = [2,3,4...], a 0. elem lesz a héten az első napja
ledolgozott_napok = []
for item in lista:
    ledolgozott_napok.append(item[0])
ledolgozott_napok = list (dict.fromkeys(ledolgozott_napok))
ledolgozott_napok.sort()
#----------------
#A hét bmely napja lehet az első napja: 
for item in lista:
     if (item[0]==ledolgozott_napok[0])and(item[1]==1):
         print ("\n2.feladat: ",item[2]," km volt a hét legelső útja\n")

#-------------------
# a hét utolsó napja: ledolgozott_napok [-1] , utolsó út == legnagyobb szám
legnagyobb,index = 0,0
for item in lista:
    if(ledolgozott_napok[-1]==item[0]):
        if (legnagyobb < item[1]):
            legnagyobb = item[1]
            index = lista.index(item)
print ("\n3.feladat: A hét utolsó napján a legutolsó út hossza:", lista[index][2],"km")
#-------------------
print ("\n4.feladat: mely napokon nem dolgozik a futár?")
result = []
for i in range(1,8):
    result.append(i)
    for item in ledolgozott_napok:
        if (i == int(item)):
            result.pop()
print ("válasz: ", *result, sep = " ")
#----------------------
#######
 #   #
  # #
   #   #
#######
print ("\n5.feladat: A hét melyik napján volt a legtöbb fuvar!")
fuvarszam = [0,0,0,0,0,0,0]
for item in lista:
    fuvarszam[item[0]-1]+=1
print ("Megoldás:",fuvarszam.index(max(fuvarszam))+1)
#----------------------
print ("\n6.feladat: Az egyes napokon mennyit kellett tekerni: x.nap: xxx km")
megtett_ut = [0,0,0,0,0,0,0]
for item in lista:
    megtett_ut[item[0]-1]+=item[2]
for i in range(len(megtett_ut)):
    print (i+1,".nap: ",megtett_ut[i]," km.")
#-----------------------
print ("\n7.feladat: Út hosszát bekérni, és kiírni a díjazást")
def bekeres(): 
    user_input = "0"
    while ((int(user_input)<=0) or (int(user_input)>30)):
        user_input = input("Adj meg egy tetszőleges távot 1-30 közt: ")
        if (user_input==""):
            user_input = "0"
    return int(user_input)
tavolsag = bekeres()
def kifizetendo(tav): 
    fizetseg = 0
    for i in range(1,tav+1):
        if((i==1)or(i==2)):
            fizetseg+=500
        elif ( (i>2)and(i<=5) ):
            fizetseg+=700
        elif ((i>5)and(i<=10)):
            fizetseg+=900
        elif ((i>10)and(i<=20)):
            fizetseg += 1400
        elif((i>20)and(i<=30)):
            fizetseg+=2000
    return fizetseg
print ("A megadott útért: ", tavolsag,"az alábbi díjazás ját:",kifizetendo(tavolsag)," huf") 
#--------------------
print ("\n8.feladat: Kiírni a dijazas.txt-be utanként a kifizetendőt, napi sorban")
lista.sort()
new_file = open("dijazas.txt","w")
for item in lista:
    new_file.write(str(item[0])+".nap "+str(item[1])+". út: "+str(kifizetendo(item[2]))+" Ft\n")
new_file.close()
#--------------------
print ("\n9.feldat: Egy heti munkáért mennyi pénzt kap a futár?")
heti_ber = 0
for item in lista:
    heti_ber+=kifizetendo(item[2])
print ("A futár heti bére bruttó ",heti_ber," Ft")
