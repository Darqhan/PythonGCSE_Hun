#1.Betölteni az aminosav.txt-t, megynitni a file-t, soronként olvasni
def open_my_file (open_this_file): 
        filepath = open_this_file
        with open(filepath) as file:
            lines = file.readlines()
        new_line = [line.rstrip('\n') for line in open(filepath)]
        return new_line
#1. 7 karakter egy fehérje minőség, nem a legelegánsabb megoldás, de műxik
# így szedtem szét a nagy fájlt aminosavakra: 
def sorted_file_to_array(new_line): 
        final_line=[]
        starter = int(int(len(new_line))/7)
        for i in range(starter):
                start=7*i
                end = start+7
                add_this="".join(new_line[start:end])
                final_line.append(add_this)
        return final_line

def rendezo(final_array): 
        strt = 0
        end = 7
        my_new_array=[]
        for i in range(int(len(final_line)/7)):
                my_new_array.append(final_array[strt:end])
                strt = end
                end += 7
        return my_new_array

final_line=open_my_file("aminosav.txt")
my_array=rendezo(final_line)
print ("\n1. feladat \nFájl megnyitás, beolvasás, használhatóvá tétele tömbben (my_array): ")
for lines in my_array: 
        print (lines)
#****************************************************************************
#2.feladat:
def sorted_by_weight(array_to_hack):
# ilyen formátumot ad vissza: [['Gly', 24, 5, 32, 14, 0, 75],
# rövidítés, név, C,H,O,N,S, össztömeg
#Tömeg Cx12 Hx1 Ox16 Nx14 Sx32
        starter = int(len(array_to_hack))
        C, H, O, N, S, weight = [], [], [], [], [], []
        combined = []
        for i in range (starter):
            #Cx12 > 5
            C.append(int(array_to_hack[i][2])*12)
            #Hx1 > 6
            H.append(int(array_to_hack[i][3])*1)
            #Ox16 > 
            O.append(int(array_to_hack[i][4])*16)
            #Nx14 > 8
            N.append(int(array_to_hack[i][5])*14)
            #Sx32 > 9
            S.append(int(array_to_hack[i][6])*32)
            #tömege
            weight.append( C[i]+H[i]+O[i]+N[i]+S[i])
            myfinal = [array_to_hack[i][1],array_to_hack[i][0],C[i],H[i],O[i],N[i],S[i],weight[i]]
            combined.append(myfinal)
        return combined

multiplied_by_weight = sorted_by_weight(my_array)

'''
print ("\n2.feladat")
print ("Aminosavak relatív tömege(utolsó oszlop száma)")
print ("Röv. / név / C---H---O---N--S/összes")
for lines in multiplied_by_weight:
        print(lines)
'''
#*************************************************************************
#3.feladat
#Növekvő sorrendbe tenni az aminosav:tömeg szerint | b, kiírni fájlba
weight_aminos=[]
for lines in range(len(multiplied_by_weight)):
        item = [multiplied_by_weight[lines][1],multiplied_by_weight[lines][7]]
        weight_aminos.append(item)
'''
print ("\n3.feladat: atomtömegek kiírása, nagyságrendbe szedve, névvel")
weight_aminos.sort(key = lambda x:x[1])
for lines in range(len(weight_aminos)): 
        print (weight_aminos[lines])
print ("\n3.feladat: ugyanez kiírása fájlba: eredmeny.txt AAA_1111")
'''
new_file = open ("eredmeny.txt","w")
new_file.write("3.feladat\n")
for lines in range(len(weight_aminos)):
        new_file.write(weight_aminos[lines][0])
        new_file.write(" ")
        new_file.write(str(weight_aminos[lines][1]))
        new_file.write("\n")
new_file.close()
#*************************************************************************
#4.feladat
# megnyitni és beolvasni a bsa.txt-t
# CHONS - H2O*aminosav szám
# C:11111 H:11111 O:11111 N:11111 S:1111
# eredmeny.txt-e ezt is ki kell iratni
print ("\n4.feladat")
bsa = open_my_file("bsa.txt") 
bsa_count = []
for i in range(len(list(zip(*multiplied_by_weight))[0])):
        elem = list(zip(*multiplied_by_weight))[0][i]
        addendum = [elem, bsa.count(elem)]
        bsa_count.append(addendum)
print ("\nbsa aminosavjai (bsa_count)")
print(*bsa_count, sep='\n')
print ("\nbsa fehérje összegképlete CHONS darabszám")
C, H, O, N, S = [], [], [],[], []
for p in range(len(bsa_count)):
         C.append((int(bsa_count[p][1]))*(int(my_array[p][2])))
         H.append((int(bsa_count[p][1]))*(int(my_array[p][3])))
         O.append((int(bsa_count[p][1]))*(int(my_array[p][4])))
         N.append((int(bsa_count[p][1]))*(int(my_array[p][5])))
         S.append((int(bsa_count[p][1]))*(int(my_array[p][6])))
minus = len(bsa)-1
H.append(-1*(minus*2))
O.append(minus)
print ("C----H-----O----N---S")
print (sum(C), sum(H),sum(O), sum(N),sum(S))

new_file = open ("eredmeny.txt","a")
new_file.write("\n4.feladat\n")
new_file.write("C ")
new_file.write(str(sum(C))+"\n")
new_file.write("H ")
new_file.write(str(sum(H))+"\n")
new_file.write("O ")
new_file.write(str(sum(O))+"\n")
new_file.write("N ")
new_file.write(str(sum(N))+"\n")
new_file.write("S ")
new_file.write(str(sum(S))+"\n")
new_file.close()
print ("\n5.feladat: Kimotripszin enzim hasít: Y, W, F")
#átalakítom teljes stringgé
bsa_chain=''.join(bsa)
#megnézzük, hol vannak a metszéspontok, mindegy melyik
bsa_count=[]
for i in range(len(bsa_chain)):
        if ((bsa_chain[i]=="Y")or(bsa_chain[i]=="W")or(bsa_chain[i]=="F")):
                bsa_count.append(i)
#összeszámolom a hosszát a daraboknak
bsa_counted=[bsa_count[0]+1]
for  j in range(1,len(bsa_count)):
        bsa_counted.append(bsa_count[j]-bsa_count[j-1])
        
#leghosszabb metszés:
my_max = max(bsa_counted)
#ennek a helye a darabok közt:
my_index_in_bsa_count = bsa_counted.index(max(bsa_counted))
print ("\nA leghosszabb darab:",my_max," egység hosszú")
#a tömbben hanyadik helyen van+1, ennyit vágjunk le a tömmből 
my_result_array = bsa_count[0:(my_index_in_bsa_count+1)]
valami = (max(bsa_counted))
strtd=((bsa_counted.index(valami)))

print ("\n Kezdet helye: ", bsa_count[strtd-1], "Vége: ",bsa_count[strtd])
#******************************************************************
# 6. feladat
# Factor IX: HA (R) ÉS ((RA) VAGY (RV)) itt az elsőt kell megtalálni
print("\n6.feladat: RA vagy RV van hamarabb?\n")
if ((bsa_chain.find('RV'))<( bsa_chain.find('RA'))):
        print ("RA: ",bsa_chain.find('RA'))
else:
        print("RV: ", bsa_chain.find('RV'))
print("Ennyi Cisztein van ebben a darabban: ", bsa_chain[0:205].count("C"))
