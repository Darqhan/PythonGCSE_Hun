file = open ("musor.txt","r")
new_array = []
for item in file: 
    new_array.append(item.rstrip())
GLOBAL = new_array[0]
new_array = new_array[1:]


''' ********************************************************************************************** '''
print ("\n6.feladat: ")
'''
Először szedjük szét az arrayt. Nekem csak a perc, mp kell, ami [1][2]
'''
one = []
for i in range (len(new_array)):
    if (new_array[i][0]=='1'):
        appendthis = new_array[i].split(" ")
        one.append(appendthis)

'''
csak az egyes számok hossza másodpercben + 60 mp előszó
'''
csak_a_hossz = []
for i in range(len(one)):
    hossz = (int(one[i][1])*60) + int(one[i][2]) + 60    
    csak_a_hossz.append(hossz)
'''
Másik tömbbe tenni, ami 3600 mp alatt van, ne felejtsem el a 180 mp óránkéntit
'''
start = 0
counter = []
for i in range (len(csak_a_hossz)):
    if ((sum(csak_a_hossz[start:i])+180)>=3600):
        counter.append(csak_a_hossz[start:(i-1)])
        start = i-1
        
print (len(counter),":",int(sum(counter[-1])/60),":",sum(counter[-1])%60)
